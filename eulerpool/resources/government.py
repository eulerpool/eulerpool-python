from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Government(SyncResource):
    def contracts(self, ticker: str, **params: Any) -> Any:
        """Government Contracts API"""
        return self._get(f"/government/contracts/{quote(str(ticker))}", params)
    def stats(self, ticker: str, **params: Any) -> Any:
        """Government Contract Statistics API"""
        return self._get(f"/government/stats/{quote(str(ticker))}", params)
    def treasury_auctions(self, **params: Any) -> Any:
        """Treasury Auction Results API"""
        return self._get("/government/treasury/auctions", params)
    def treasury_debt(self, **params: Any) -> Any:
        """US National Debt API"""
        return self._get("/government/treasury/debt", params)
    def treasury_yields(self, **params: Any) -> Any:
        """Daily Treasury Yield Curve API"""
        return self._get("/government/treasury/yields", params)


class AsyncGovernment(AsyncResource):
    async def contracts(self, ticker: str, **params: Any) -> Any:
        """Government Contracts API"""
        return await self._get(f"/government/contracts/{quote(str(ticker))}", params)
    async def stats(self, ticker: str, **params: Any) -> Any:
        """Government Contract Statistics API"""
        return await self._get(f"/government/stats/{quote(str(ticker))}", params)
    async def treasury_auctions(self, **params: Any) -> Any:
        """Treasury Auction Results API"""
        return await self._get("/government/treasury/auctions", params)
    async def treasury_debt(self, **params: Any) -> Any:
        """US National Debt API"""
        return await self._get("/government/treasury/debt", params)
    async def treasury_yields(self, **params: Any) -> Any:
        """Daily Treasury Yield Curve API"""
        return await self._get("/government/treasury/yields", params)
