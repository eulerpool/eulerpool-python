from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Research(SyncResource):
    def news(self, ticker: str, **params: Any) -> Any:
        """Company News"""
        return self._get(f"/research/news/{quote(str(ticker))}", params)
    def press_releases(self, ticker: str, **params: Any) -> Any:
        """Press Releases"""
        return self._get(f"/research/press-releases/{quote(str(ticker))}", params)
    def recommendations(self, ticker: str, **params: Any) -> Any:
        """Analyst Recommendations"""
        return self._get(f"/research/recommendations/{quote(str(ticker))}", params)


class AsyncResearch(AsyncResource):
    async def news(self, ticker: str, **params: Any) -> Any:
        """Company News"""
        return await self._get(f"/research/news/{quote(str(ticker))}", params)
    async def press_releases(self, ticker: str, **params: Any) -> Any:
        """Press Releases"""
        return await self._get(f"/research/press-releases/{quote(str(ticker))}", params)
    async def recommendations(self, ticker: str, **params: Any) -> Any:
        """Analyst Recommendations"""
        return await self._get(f"/research/recommendations/{quote(str(ticker))}", params)
