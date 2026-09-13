from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Datasets(SyncResource):
    def catalog(self, **params: Any) -> Any:
        """Dataset Catalog"""
        return self._get("/datasets/catalog", params)
    def dcf(self, identifier: str, **params: Any) -> Any:
        """Discounted Cash Flow Valuation"""
        return self._get(f"/datasets/dcf/{quote(str(identifier))}", params)
    def eod(self, identifier: str, **params: Any) -> Any:
        """End-of-Day Quote"""
        return self._get(f"/datasets/eod/{quote(str(identifier))}", params)
    def gainers(self, **params: Any) -> Any:
        """Biggest Gainers"""
        return self._get("/datasets/gainers", params)
    def get(self, dataset: str, identifier: Optional[str] = None, **params: Any) -> Any:
        """Company Dataset"""
        if identifier is not None:
            return self._get(f"/datasets/{quote(str(dataset))}/{quote(str(identifier))}", params)
        return self._get(f"/datasets/{quote(str(dataset))}", params)
    def industry_pe(self, **params: Any) -> Any:
        """Industry PE Snapshots"""
        return self._get("/datasets/industry-pe", params)
    def key_metrics(self, identifier: str, **params: Any) -> Any:
        """Key Metrics (TTM)"""
        return self._get(f"/datasets/key-metrics/{quote(str(identifier))}", params)
    def losers(self, **params: Any) -> Any:
        """Biggest Losers"""
        return self._get("/datasets/losers", params)
    def most_active(self, **params: Any) -> Any:
        """Most Active Stocks"""
        return self._get("/datasets/most-active", params)
    def news(self, **params: Any) -> Any:
        """Market News Feed"""
        return self._get("/datasets/news", params)
    def rating(self, identifier: str, **params: Any) -> Any:
        """Company Rating"""
        return self._get(f"/datasets/rating/{quote(str(identifier))}", params)
    def ratios(self, identifier: str, **params: Any) -> Any:
        """Financial Ratios (TTM)"""
        return self._get(f"/datasets/ratios/{quote(str(identifier))}", params)
    def scores(self, identifier: str, **params: Any) -> Any:
        """Financial Scores"""
        return self._get(f"/datasets/scores/{quote(str(identifier))}", params)
    def sector_pe(self, **params: Any) -> Any:
        """Sector PE Snapshots"""
        return self._get("/datasets/sector-pe", params)


class AsyncDatasets(AsyncResource):
    async def catalog(self, **params: Any) -> Any:
        """Dataset Catalog"""
        return await self._get("/datasets/catalog", params)
    async def dcf(self, identifier: str, **params: Any) -> Any:
        """Discounted Cash Flow Valuation"""
        return await self._get(f"/datasets/dcf/{quote(str(identifier))}", params)
    async def eod(self, identifier: str, **params: Any) -> Any:
        """End-of-Day Quote"""
        return await self._get(f"/datasets/eod/{quote(str(identifier))}", params)
    async def gainers(self, **params: Any) -> Any:
        """Biggest Gainers"""
        return await self._get("/datasets/gainers", params)
    async def get(self, dataset: str, identifier: Optional[str] = None, **params: Any) -> Any:
        """Company Dataset"""
        if identifier is not None:
            return await self._get(f"/datasets/{quote(str(dataset))}/{quote(str(identifier))}", params)
        return await self._get(f"/datasets/{quote(str(dataset))}", params)
    async def industry_pe(self, **params: Any) -> Any:
        """Industry PE Snapshots"""
        return await self._get("/datasets/industry-pe", params)
    async def key_metrics(self, identifier: str, **params: Any) -> Any:
        """Key Metrics (TTM)"""
        return await self._get(f"/datasets/key-metrics/{quote(str(identifier))}", params)
    async def losers(self, **params: Any) -> Any:
        """Biggest Losers"""
        return await self._get("/datasets/losers", params)
    async def most_active(self, **params: Any) -> Any:
        """Most Active Stocks"""
        return await self._get("/datasets/most-active", params)
    async def news(self, **params: Any) -> Any:
        """Market News Feed"""
        return await self._get("/datasets/news", params)
    async def rating(self, identifier: str, **params: Any) -> Any:
        """Company Rating"""
        return await self._get(f"/datasets/rating/{quote(str(identifier))}", params)
    async def ratios(self, identifier: str, **params: Any) -> Any:
        """Financial Ratios (TTM)"""
        return await self._get(f"/datasets/ratios/{quote(str(identifier))}", params)
    async def scores(self, identifier: str, **params: Any) -> Any:
        """Financial Scores"""
        return await self._get(f"/datasets/scores/{quote(str(identifier))}", params)
    async def sector_pe(self, **params: Any) -> Any:
        """Sector PE Snapshots"""
        return await self._get("/datasets/sector-pe", params)
