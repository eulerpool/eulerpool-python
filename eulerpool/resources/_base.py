from __future__ import annotations

from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .._client import AsyncHttpClient, HttpClient


class SyncResource:
    def __init__(self, client: "HttpClient") -> None:
        self._client = client

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._client.get(path, params)

    def _post(self, path: str, body: Any = None, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._client.post(path, body, params)

    def _delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._client.delete(path, params)


class AsyncResource:
    def __init__(self, client: "AsyncHttpClient") -> None:
        self._client = client

    async def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._client.get(path, params)

    async def _post(self, path: str, body: Any = None, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._client.post(path, body, params)

    async def _delete(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._client.delete(path, params)
