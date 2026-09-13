from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Institutional(SyncResource):
    def form_13f(self, cik: str, **params: Any) -> Any:
        """SEC 13F Holdings by Filer"""
        return self._get(f"/institutional/13f/{quote(str(cik))}", params)
    def form_13f_filers(self, **params: Any) -> Any:
        """Top 13F Filers"""
        return self._get("/institutional/13f-filers", params)
    def form_13f_holders(self, ticker: str, **params: Any) -> Any:
        """SEC 13F Institutional Holders of a Stock"""
        return self._get(f"/institutional/13f-holders/{quote(str(ticker))}", params)
    def fund_holders(self, ticker: str, **params: Any) -> Any:
        """Fund Institutional Holders of a Stock"""
        return self._get(f"/institutional/fund-holders/{quote(str(ticker))}", params)
    def fund_holdings(self, cik: str, **params: Any) -> Any:
        """Fund Institutional Holdings by Filer"""
        return self._get(f"/institutional/fund-holdings/{quote(str(cik))}", params)
    def portfolio(self, cik: str, **params: Any) -> Any:
        """Institutional 13-F Portfolio API"""
        return self._get(f"/institutional/portfolio/{quote(str(cik))}", params)
    def profile(self, cik: str, **params: Any) -> Any:
        """Institutional Investor Profile API"""
        return self._get(f"/institutional/profile/{quote(str(cik))}", params)
    def top_holders(self, **params: Any) -> Any:
        """Top Institutional Holders"""
        return self._get("/institutional/top-holders", params)


class AsyncInstitutional(AsyncResource):
    async def form_13f(self, cik: str, **params: Any) -> Any:
        """SEC 13F Holdings by Filer"""
        return await self._get(f"/institutional/13f/{quote(str(cik))}", params)
    async def form_13f_filers(self, **params: Any) -> Any:
        """Top 13F Filers"""
        return await self._get("/institutional/13f-filers", params)
    async def form_13f_holders(self, ticker: str, **params: Any) -> Any:
        """SEC 13F Institutional Holders of a Stock"""
        return await self._get(f"/institutional/13f-holders/{quote(str(ticker))}", params)
    async def fund_holders(self, ticker: str, **params: Any) -> Any:
        """Fund Institutional Holders of a Stock"""
        return await self._get(f"/institutional/fund-holders/{quote(str(ticker))}", params)
    async def fund_holdings(self, cik: str, **params: Any) -> Any:
        """Fund Institutional Holdings by Filer"""
        return await self._get(f"/institutional/fund-holdings/{quote(str(cik))}", params)
    async def portfolio(self, cik: str, **params: Any) -> Any:
        """Institutional 13-F Portfolio API"""
        return await self._get(f"/institutional/portfolio/{quote(str(cik))}", params)
    async def profile(self, cik: str, **params: Any) -> Any:
        """Institutional Investor Profile API"""
        return await self._get(f"/institutional/profile/{quote(str(cik))}", params)
    async def top_holders(self, **params: Any) -> Any:
        """Top Institutional Holders"""
        return await self._get("/institutional/top-holders", params)
