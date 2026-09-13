from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Charting(SyncResource):
    def compare(self, **params: Any) -> Any:
        """Multi-Symbol Compare"""
        return self._get("/charting/compare", params)
    def indicators(self, identifier: str, **params: Any) -> Any:
        """Technical Indicators"""
        return self._get(f"/charting/indicators/{quote(str(identifier))}", params)
    def ohlcv(self, identifier: str, **params: Any) -> Any:
        """OHLCV Candles"""
        return self._get(f"/charting/ohlcv/{quote(str(identifier))}", params)
    def overlay(self, identifier: str, **params: Any) -> Any:
        """Chart Overlays"""
        return self._get(f"/charting/overlay/{quote(str(identifier))}", params)
    def patterns(self, identifier: str, **params: Any) -> Any:
        """Candlestick Patterns"""
        return self._get(f"/charting/patterns/{quote(str(identifier))}", params)


class AsyncCharting(AsyncResource):
    async def compare(self, **params: Any) -> Any:
        """Multi-Symbol Compare"""
        return await self._get("/charting/compare", params)
    async def indicators(self, identifier: str, **params: Any) -> Any:
        """Technical Indicators"""
        return await self._get(f"/charting/indicators/{quote(str(identifier))}", params)
    async def ohlcv(self, identifier: str, **params: Any) -> Any:
        """OHLCV Candles"""
        return await self._get(f"/charting/ohlcv/{quote(str(identifier))}", params)
    async def overlay(self, identifier: str, **params: Any) -> Any:
        """Chart Overlays"""
        return await self._get(f"/charting/overlay/{quote(str(identifier))}", params)
    async def patterns(self, identifier: str, **params: Any) -> Any:
        """Candlestick Patterns"""
        return await self._get(f"/charting/patterns/{quote(str(identifier))}", params)
