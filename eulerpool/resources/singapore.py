from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Singapore(SyncResource):
    def acra(self, uen: Optional[str] = None, **params: Any) -> Any:
        """ACRA Financials by UEN"""
        if uen is not None:
            return self._get(f"/singapore/acra/{quote(str(uen))}", params)
        return self._get("/singapore/acra", params)
    def announcements(self, **params: Any) -> Any:
        """SGX Announcements API"""
        return self._get("/singapore/announcements", params)
    def corporate_actions(self, **params: Any) -> Any:
        """SGX Corporate Actions API"""
        return self._get("/singapore/corporate-actions", params)
    def economic_stats(self, **params: Any) -> Any:
        """Singapore Economic Statistics API"""
        return self._get("/singapore/economic-stats", params)
    def economic_stats_series(self, **params: Any) -> Any:
        """Singapore Economic Stats Series List"""
        return self._get("/singapore/economic-stats/series", params)
    def insider_trades(self, **params: Any) -> Any:
        """SGX Insider Trades API"""
        return self._get("/singapore/insider-trades", params)
    def mas_exchange_rates(self, **params: Any) -> Any:
        """MAS Exchange Rates API"""
        return self._get("/singapore/mas/exchange-rates", params)
    def mas_interest_rates(self, **params: Any) -> Any:
        """MAS Interest Rates API"""
        return self._get("/singapore/mas/interest-rates", params)
    def mas_money_supply(self, **params: Any) -> Any:
        """MAS Money Supply API"""
        return self._get("/singapore/mas/money-supply", params)
    def reits(self, **params: Any) -> Any:
        """S-REIT Metrics API"""
        return self._get("/singapore/reits", params)
    def reits_list(self, **params: Any) -> Any:
        """S-REIT List API"""
        return self._get("/singapore/reits/list", params)


class AsyncSingapore(AsyncResource):
    async def acra(self, uen: Optional[str] = None, **params: Any) -> Any:
        """ACRA Financials by UEN"""
        if uen is not None:
            return await self._get(f"/singapore/acra/{quote(str(uen))}", params)
        return await self._get("/singapore/acra", params)
    async def announcements(self, **params: Any) -> Any:
        """SGX Announcements API"""
        return await self._get("/singapore/announcements", params)
    async def corporate_actions(self, **params: Any) -> Any:
        """SGX Corporate Actions API"""
        return await self._get("/singapore/corporate-actions", params)
    async def economic_stats(self, **params: Any) -> Any:
        """Singapore Economic Statistics API"""
        return await self._get("/singapore/economic-stats", params)
    async def economic_stats_series(self, **params: Any) -> Any:
        """Singapore Economic Stats Series List"""
        return await self._get("/singapore/economic-stats/series", params)
    async def insider_trades(self, **params: Any) -> Any:
        """SGX Insider Trades API"""
        return await self._get("/singapore/insider-trades", params)
    async def mas_exchange_rates(self, **params: Any) -> Any:
        """MAS Exchange Rates API"""
        return await self._get("/singapore/mas/exchange-rates", params)
    async def mas_interest_rates(self, **params: Any) -> Any:
        """MAS Interest Rates API"""
        return await self._get("/singapore/mas/interest-rates", params)
    async def mas_money_supply(self, **params: Any) -> Any:
        """MAS Money Supply API"""
        return await self._get("/singapore/mas/money-supply", params)
    async def reits(self, **params: Any) -> Any:
        """S-REIT Metrics API"""
        return await self._get("/singapore/reits", params)
    async def reits_list(self, **params: Any) -> Any:
        """S-REIT List API"""
        return await self._get("/singapore/reits/list", params)
