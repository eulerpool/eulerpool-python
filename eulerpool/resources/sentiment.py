from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Sentiment(SyncResource):
    def fund_ownership(self, identifier: str, **params: Any) -> Any:
        """Fund Ownership API"""
        return self._get(f"/sentiment/fund-ownership/{quote(str(identifier))}", params)
    def insider_sentiment(self, identifier: str, **params: Any) -> Any:
        """Insider Sentiment API"""
        return self._get(f"/sentiment/insider-sentiment/{quote(str(identifier))}", params)
    def institutional_ownership(self, identifier: str, **params: Any) -> Any:
        """Institutional Ownership API"""
        return self._get(f"/sentiment/institutional-ownership/{quote(str(identifier))}", params)
    def news_sentiment(self, identifier: str, **params: Any) -> Any:
        """News Sentiment API"""
        return self._get(f"/sentiment/news-sentiment/{quote(str(identifier))}", params)
    def price_metrics(self, identifier: str, **params: Any) -> Any:
        """Price Metrics API"""
        return self._get(f"/sentiment/price-metrics/{quote(str(identifier))}", params)
    def sector_metrics(self, **params: Any) -> Any:
        """Sector Metrics API"""
        return self._get("/sentiment/sector-metrics", params)
    def social(self, ticker: str, **params: Any) -> Any:
        """Reddit Social Sentiment API"""
        return self._get(f"/sentiment/social/{quote(str(ticker))}", params)
    def social_sentiment(self, identifier: str, **params: Any) -> Any:
        """Social Sentiment API"""
        return self._get(f"/sentiment/social-sentiment/{quote(str(identifier))}", params)


class AsyncSentiment(AsyncResource):
    async def fund_ownership(self, identifier: str, **params: Any) -> Any:
        """Fund Ownership API"""
        return await self._get(f"/sentiment/fund-ownership/{quote(str(identifier))}", params)
    async def insider_sentiment(self, identifier: str, **params: Any) -> Any:
        """Insider Sentiment API"""
        return await self._get(f"/sentiment/insider-sentiment/{quote(str(identifier))}", params)
    async def institutional_ownership(self, identifier: str, **params: Any) -> Any:
        """Institutional Ownership API"""
        return await self._get(f"/sentiment/institutional-ownership/{quote(str(identifier))}", params)
    async def news_sentiment(self, identifier: str, **params: Any) -> Any:
        """News Sentiment API"""
        return await self._get(f"/sentiment/news-sentiment/{quote(str(identifier))}", params)
    async def price_metrics(self, identifier: str, **params: Any) -> Any:
        """Price Metrics API"""
        return await self._get(f"/sentiment/price-metrics/{quote(str(identifier))}", params)
    async def sector_metrics(self, **params: Any) -> Any:
        """Sector Metrics API"""
        return await self._get("/sentiment/sector-metrics", params)
    async def social(self, ticker: str, **params: Any) -> Any:
        """Reddit Social Sentiment API"""
        return await self._get(f"/sentiment/social/{quote(str(ticker))}", params)
    async def social_sentiment(self, identifier: str, **params: Any) -> Any:
        """Social Sentiment API"""
        return await self._get(f"/sentiment/social-sentiment/{quote(str(identifier))}", params)
