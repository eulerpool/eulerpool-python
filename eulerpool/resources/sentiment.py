from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Sentiment(SyncResource):
    def insider_sentiment(self, isin: str) -> Any:
        return self._get(f"/sentiment/insider-sentiment/{quote(isin)}")

    def news_sentiment(self, isin: str) -> Any:
        return self._get(f"/sentiment/news-sentiment/{quote(isin)}")

    def social_sentiment(self, isin: str) -> Any:
        return self._get(f"/sentiment/social-sentiment/{quote(isin)}")

    def price_metrics(self, isin: str) -> Any:
        return self._get(f"/sentiment/price-metrics/{quote(isin)}")

    def fund_ownership(self, isin: str) -> Any:
        return self._get(f"/sentiment/fund-ownership/{quote(isin)}")

    def institutional_ownership(self, isin: str) -> Any:
        return self._get(f"/sentiment/institutional-ownership/{quote(isin)}")

    def sector_metrics(self) -> Any:
        return self._get("/sentiment/sector-metrics")


class AsyncSentiment(AsyncResource):
    async def insider_sentiment(self, isin: str) -> Any:
        return await self._get(f"/sentiment/insider-sentiment/{quote(isin)}")

    async def news_sentiment(self, isin: str) -> Any:
        return await self._get(f"/sentiment/news-sentiment/{quote(isin)}")

    async def social_sentiment(self, isin: str) -> Any:
        return await self._get(f"/sentiment/social-sentiment/{quote(isin)}")

    async def price_metrics(self, isin: str) -> Any:
        return await self._get(f"/sentiment/price-metrics/{quote(isin)}")

    async def fund_ownership(self, isin: str) -> Any:
        return await self._get(f"/sentiment/fund-ownership/{quote(isin)}")

    async def institutional_ownership(self, isin: str) -> Any:
        return await self._get(f"/sentiment/institutional-ownership/{quote(isin)}")

    async def sector_metrics(self) -> Any:
        return await self._get("/sentiment/sector-metrics")
