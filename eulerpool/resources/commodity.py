from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Commodity(SyncResource):
    def crack_spreads(self, **params: Any) -> Any:
        """Crack Spreads API"""
        return self._get("/commodity/crack-spreads", params)
    def futures_curve(self, product: str, **params: Any) -> Any:
        """Futures Term Structure API"""
        return self._get(f"/commodity/futures-curve/{quote(str(product))}", params)
    def futures_curve_history(self, product: str, **params: Any) -> Any:
        """Futures Curve History API"""
        return self._get(f"/commodity/futures-curve/{quote(str(product))}/history", params)
    def futures_settlements(self, **params: Any) -> Any:
        """Futures Settlements API"""
        return self._get("/commodity/futures-settlements", params)
    def list(self, **params: Any) -> Any:
        """Commodities List API"""
        return self._get("/commodity/list", params)
    def prices(self, symbol: Optional[str] = None, **params: Any) -> Any:
        """Commodity Prices API"""
        if symbol is not None:
            return self._get(f"/commodity/prices/{quote(str(symbol))}", params)
        return self._get("/commodity/prices", params)
    def profile(self, ticker: str, **params: Any) -> Any:
        """Commodity Profile API"""
        return self._get(f"/commodity/profile/{quote(str(ticker))}", params)
    def quotes(self, ticker: str, **params: Any) -> Any:
        """Commodity Quotes API"""
        return self._get(f"/commodity/quotes/{quote(str(ticker))}", params)


class AsyncCommodity(AsyncResource):
    async def crack_spreads(self, **params: Any) -> Any:
        """Crack Spreads API"""
        return await self._get("/commodity/crack-spreads", params)
    async def futures_curve(self, product: str, **params: Any) -> Any:
        """Futures Term Structure API"""
        return await self._get(f"/commodity/futures-curve/{quote(str(product))}", params)
    async def futures_curve_history(self, product: str, **params: Any) -> Any:
        """Futures Curve History API"""
        return await self._get(f"/commodity/futures-curve/{quote(str(product))}/history", params)
    async def futures_settlements(self, **params: Any) -> Any:
        """Futures Settlements API"""
        return await self._get("/commodity/futures-settlements", params)
    async def list(self, **params: Any) -> Any:
        """Commodities List API"""
        return await self._get("/commodity/list", params)
    async def prices(self, symbol: Optional[str] = None, **params: Any) -> Any:
        """Commodity Prices API"""
        if symbol is not None:
            return await self._get(f"/commodity/prices/{quote(str(symbol))}", params)
        return await self._get("/commodity/prices", params)
    async def profile(self, ticker: str, **params: Any) -> Any:
        """Commodity Profile API"""
        return await self._get(f"/commodity/profile/{quote(str(ticker))}", params)
    async def quotes(self, ticker: str, **params: Any) -> Any:
        """Commodity Quotes API"""
        return await self._get(f"/commodity/quotes/{quote(str(ticker))}", params)
