from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Etf(SyncResource):
    def countries(self, identifier: str, **params: Any) -> Any:
        """ETF Countries API"""
        return self._get(f"/etf/countries/{quote(str(identifier))}", params)
    def description(self, identifier: str, **params: Any) -> Any:
        """ETF Description API"""
        return self._get(f"/etf/description/{quote(str(identifier))}", params)
    def flows(self, ticker: str, **params: Any) -> Any:
        """ETF Flows API"""
        return self._get(f"/etf/flows/{quote(str(ticker))}", params)
    def holdings(self, identifier: str, **params: Any) -> Any:
        """ETF Holdings API"""
        return self._get(f"/etf/holdings/{quote(str(identifier))}", params)
    def list(self, start: str, end: str, **params: Any) -> Any:
        """ETF List API"""
        return self._get(f"/etf/list/{quote(str(start))}/{quote(str(end))}", params)
    def profile(self, identifier: str, **params: Any) -> Any:
        """ETF Profile API"""
        return self._get(f"/etf/profile/{quote(str(identifier))}", params)
    def quotes(self, identifier: str, **params: Any) -> Any:
        """ETF Quotes API"""
        return self._get(f"/etf/quotes/{quote(str(identifier))}", params)
    def sectors(self, identifier: str, **params: Any) -> Any:
        """ETF Sectors API"""
        return self._get(f"/etf/sectors/{quote(str(identifier))}", params)


class AsyncEtf(AsyncResource):
    async def countries(self, identifier: str, **params: Any) -> Any:
        """ETF Countries API"""
        return await self._get(f"/etf/countries/{quote(str(identifier))}", params)
    async def description(self, identifier: str, **params: Any) -> Any:
        """ETF Description API"""
        return await self._get(f"/etf/description/{quote(str(identifier))}", params)
    async def flows(self, ticker: str, **params: Any) -> Any:
        """ETF Flows API"""
        return await self._get(f"/etf/flows/{quote(str(ticker))}", params)
    async def holdings(self, identifier: str, **params: Any) -> Any:
        """ETF Holdings API"""
        return await self._get(f"/etf/holdings/{quote(str(identifier))}", params)
    async def list(self, start: str, end: str, **params: Any) -> Any:
        """ETF List API"""
        return await self._get(f"/etf/list/{quote(str(start))}/{quote(str(end))}", params)
    async def profile(self, identifier: str, **params: Any) -> Any:
        """ETF Profile API"""
        return await self._get(f"/etf/profile/{quote(str(identifier))}", params)
    async def quotes(self, identifier: str, **params: Any) -> Any:
        """ETF Quotes API"""
        return await self._get(f"/etf/quotes/{quote(str(identifier))}", params)
    async def sectors(self, identifier: str, **params: Any) -> Any:
        """ETF Sectors API"""
        return await self._get(f"/etf/sectors/{quote(str(identifier))}", params)
