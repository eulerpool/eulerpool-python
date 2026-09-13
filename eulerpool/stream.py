from __future__ import annotations

import json
from typing import Any, Dict, Iterator, Optional, Sequence
from urllib.parse import urlencode

from ._client import AsyncHttpClient, HttpClient


def stream_url_from_base(base_url: str, stream_url: Optional[str] = None) -> str:
    if stream_url:
        return stream_url.rstrip("/")
    root = base_url.replace("/api/1", "").rstrip("/")
    if root.startswith("https://api.eulerpool.com") or root == "https://api.eulerpool.com":
        return "wss://api.eulerpool.com/v1/subscribe"
    if root.startswith("https://"):
        return "wss://" + root[len("https://") :] + "/v1/subscribe"
    if root.startswith("http://"):
        return "ws://" + root[len("http://") :] + "/v1/subscribe"
    return "wss://api.eulerpool.com/v1/subscribe"


def _require_websockets():
    try:
        import websockets
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "client.stream requires the websockets package. "
            "Install with: pip install 'eulerpool[stream]' or pip install websockets"
        ) from exc
    return websockets


class Stream:
    """Synchronous WebSocket client for the Eulerpool tick plant."""

    def __init__(self, client: HttpClient) -> None:
        self._client = client

    def subscribe(
        self,
        tickers: Sequence[str],
        channels: Sequence[str] = ("T", "Q"),
        *,
        encoding: str = "json",
    ) -> Iterator[Dict[str, Any]]:
        """Yield ticks until the caller breaks.

        Channels: ``T`` trades, ``Q`` quotes, ``A`` 1-second bars, ``L2`` book.
        """
        ws_mod = _require_websockets()
        from websockets.sync.client import connect

        url = self._url()
        with connect(url, additional_headers={"Authorization": f"Bearer {self._client.api_key}"}) as ws:
            ws.send(json.dumps({
                "action": "subscribe",
                "params": {"tickers": list(tickers), "channels": list(channels)},
            }))
            if encoding == "binary":
                ws.send(json.dumps({"action": "format", "params": {"encoding": "binary"}}))
            for raw in ws:
                if isinstance(raw, bytes):
                    continue
                try:
                    msg = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                yield msg

    def _url(self) -> str:
        token = urlencode({"token": self._client.api_key})
        return f"{stream_url_from_base(self._client.base_url)}?{token}"


class AsyncStream:
    """Async WebSocket client for the Eulerpool tick plant."""

    def __init__(self, client: AsyncHttpClient) -> None:
        self._client = client

    async def subscribe(
        self,
        tickers: Sequence[str],
        channels: Sequence[str] = ("T", "Q"),
        *,
        encoding: str = "json",
    ):
        ws_mod = _require_websockets()
        url = self._url()
        async with ws_mod.connect(url, additional_headers={"Authorization": f"Bearer {self._client.api_key}"}) as ws:
            await ws.send(json.dumps({
                "action": "subscribe",
                "params": {"tickers": list(tickers), "channels": list(channels)},
            }))
            if encoding == "binary":
                await ws.send(json.dumps({"action": "format", "params": {"encoding": "binary"}}))
            async for raw in ws:
                if isinstance(raw, bytes):
                    continue
                try:
                    yield json.loads(raw)
                except json.JSONDecodeError:
                    continue

    def _url(self) -> str:
        token = urlencode({"token": self._client.api_key})
        return f"{stream_url_from_base(self._client.base_url)}?{token}"
