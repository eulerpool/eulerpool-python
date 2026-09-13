from __future__ import annotations

import time
from typing import Any, Dict, Optional

import httpx

from ._version import __version__
from .errors import (
    AuthenticationError,
    BadRequestError,
    EulerpoolError,
    NotFoundError,
    RateLimitError,
    ServerError,
)

_PARAM_ALIASES = {"from_": "from", "class_": "class", "global_": "global"}


def _normalize_params(params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    q: Dict[str, Any] = {}
    if not params:
        return q
    for key, value in params.items():
        if value is None:
            continue
        q[_PARAM_ALIASES.get(key, key)] = value
    return q


class HttpClient:
    """Low-level synchronous HTTP client for the Eulerpool API."""

    _BASE_URL = "https://api.eulerpool.com/api/1"

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        use_auth_header: bool = False,
        max_retries: int = 2,
        timeout: float = 30.0,
    ) -> None:
        self._api_key = api_key
        self._base_url = (base_url or self._BASE_URL).rstrip("/")
        self._use_auth_header = use_auth_header
        self._max_retries = max_retries
        self._http = httpx.Client(
            timeout=timeout,
            follow_redirects=True,
            headers={
                "Accept": "application/json",
                "User-Agent": f"eulerpool-python/{__version__}",
            },
        )

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def base_url(self) -> str:
        return self._base_url

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", path, params=params)

    def post(self, path: str, body: Any = None, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("POST", path, params=params, json_body=body)

    def delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("DELETE", path, params=params)

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "HttpClient":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Any = None,
    ) -> Any:
        url = f"{self._base_url}{path}"
        query = self._build_query(params)
        headers: Dict[str, str] = {
            "Authorization": f"Bearer {self._api_key}",
        }

        last_exc: Optional[Exception] = None
        for attempt in range(self._max_retries + 1):
            if attempt > 0:
                time.sleep(min(2 ** (attempt - 1), 8))
            try:
                resp = self._http.request(
                    method,
                    url,
                    params=query,
                    json=json_body,
                    headers=headers,
                )
                if resp.is_success:
                    if not resp.content:
                        return None
                    try:
                        return resp.json()
                    except Exception:
                        return resp.text
                error = self._make_error(resp)
                if not self._is_retryable(resp.status_code):
                    raise error
                last_exc = error
            except EulerpoolError:
                raise
            except Exception as exc:
                last_exc = exc

        raise last_exc or EulerpoolError("Request failed after retries.")

    def _build_query(self, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        q: Dict[str, Any] = {}
        if not self._use_auth_header:
            q["token"] = self._api_key
        q.update(_normalize_params(params))
        return q

    @staticmethod
    def _make_error(resp: httpx.Response) -> EulerpoolError:
        try:
            body = resp.json()
            msg = body.get("message") or body.get("error") or resp.reason_phrase
        except Exception:
            msg = resp.text or resp.reason_phrase
        status = resp.status_code
        if status == 400:
            return BadRequestError(msg)
        if status == 401:
            return AuthenticationError(msg)
        if status == 404:
            return NotFoundError(msg)
        if status == 429:
            retry = resp.headers.get("Retry-After")
            return RateLimitError(msg, retry_after=int(retry) if retry else None)
        if status >= 500:
            return ServerError(msg)
        return EulerpoolError(msg, status=status)

    @staticmethod
    def _is_retryable(status: int) -> bool:
        return status == 429 or status >= 500


class AsyncHttpClient:
    """Low-level async HTTP client for the Eulerpool API."""

    _BASE_URL = "https://api.eulerpool.com/api/1"

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        use_auth_header: bool = False,
        max_retries: int = 2,
        timeout: float = 30.0,
    ) -> None:
        self._api_key = api_key
        self._base_url = (base_url or self._BASE_URL).rstrip("/")
        self._use_auth_header = use_auth_header
        self._max_retries = max_retries
        self._http = httpx.AsyncClient(
            timeout=timeout,
            follow_redirects=True,
            headers={
                "Accept": "application/json",
                "User-Agent": f"eulerpool-python/{__version__}",
            },
        )

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def base_url(self) -> str:
        return self._base_url

    async def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._request("GET", path, params=params)

    async def post(self, path: str, body: Any = None, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._request("POST", path, params=params, json_body=body)

    async def delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._request("DELETE", path, params=params)

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> "AsyncHttpClient":
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.close()

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Any = None,
    ) -> Any:
        import asyncio

        url = f"{self._base_url}{path}"
        query = self._build_query(params)
        headers: Dict[str, str] = {
            "Authorization": f"Bearer {self._api_key}",
        }

        last_exc: Optional[Exception] = None
        for attempt in range(self._max_retries + 1):
            if attempt > 0:
                await asyncio.sleep(min(2 ** (attempt - 1), 8))
            try:
                resp = await self._http.request(
                    method,
                    url,
                    params=query,
                    json=json_body,
                    headers=headers,
                )
                if resp.is_success:
                    if not resp.content:
                        return None
                    try:
                        return resp.json()
                    except Exception:
                        return resp.text
                error = HttpClient._make_error(resp)
                if not HttpClient._is_retryable(resp.status_code):
                    raise error
                last_exc = error
            except EulerpoolError:
                raise
            except Exception as exc:
                last_exc = exc

        raise last_exc or EulerpoolError("Request failed after retries.")

    def _build_query(self, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        q: Dict[str, Any] = {}
        if not self._use_auth_header:
            q["token"] = self._api_key
        q.update(_normalize_params(params))
        return q
