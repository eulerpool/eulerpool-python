from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Alternative(SyncResource):
    def congress_trading(self, **params: Any) -> Any:
        """Congress Trading API"""
        return self._get("/alternative/congress-trading", params)
    def cot(self, symbol: str, **params: Any) -> Any:
        """Commitments of Traders (COT) API"""
        return self._get(f"/alternative/cot/{quote(str(symbol))}", params)
    def datasets(self, datasetId: Optional[str] = None, **params: Any) -> Any:
        """Get External Dataset"""
        if datasetId is not None:
            return self._get(f"/alternative/datasets/{quote(str(datasetId))}", params)
        return self._get("/alternative/datasets", params)
    def fear_and_greed(self, **params: Any) -> Any:
        """Fear & Greed Index API"""
        return self._get("/alternative/fear-and-greed", params)
    def google_trends(self, ticker: str, **params: Any) -> Any:
        """Google Trends API"""
        return self._get(f"/alternative/google-trends/{quote(str(ticker))}", params)
    def ingest(self, body: Any = None, **params: Any) -> Any:
        """Ingest External Dataset"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/alternative/ingest", body, params)
    def investment_themes(self, **params: Any) -> Any:
        """Investment Themes API"""
        return self._get("/alternative/investment-themes", params)
    def reddit_mentions(self, ticker: str, **params: Any) -> Any:
        """Reddit Stock Mentions API"""
        return self._get(f"/alternative/reddit-mentions/{quote(str(ticker))}", params)
    def social_mentions(self, ticker: str, **params: Any) -> Any:
        """Social Mentions History"""
        return self._get(f"/alternative/social-mentions/{quote(str(ticker))}", params)
    def stocktwits(self, ticker: str, **params: Any) -> Any:
        """StockTwits Sentiment API"""
        return self._get(f"/alternative/stocktwits/{quote(str(ticker))}", params)
    def superinvestors_holdings(self, slug: str, **params: Any) -> Any:
        """Superinvestor Holdings API"""
        return self._get(f"/alternative/superinvestors/holdings/{quote(str(slug))}", params)
    def superinvestors_list(self, **params: Any) -> Any:
        """Superinvestors List API"""
        return self._get("/alternative/superinvestors/list", params)
    def superinvestors_recent_activity(self, **params: Any) -> Any:
        """Superinvestor Recent Activity API"""
        return self._get("/alternative/superinvestors/recent-activity", params)
    def superinvestors_top_holdings(self, **params: Any) -> Any:
        """Superinvestor Top Holdings API"""
        return self._get("/alternative/superinvestors/top-holdings", params)
    def wikipedia_pageviews(self, ticker: str, **params: Any) -> Any:
        """Wikipedia Pageviews API"""
        return self._get(f"/alternative/wikipedia-pageviews/{quote(str(ticker))}", params)


class AsyncAlternative(AsyncResource):
    async def congress_trading(self, **params: Any) -> Any:
        """Congress Trading API"""
        return await self._get("/alternative/congress-trading", params)
    async def cot(self, symbol: str, **params: Any) -> Any:
        """Commitments of Traders (COT) API"""
        return await self._get(f"/alternative/cot/{quote(str(symbol))}", params)
    async def datasets(self, datasetId: Optional[str] = None, **params: Any) -> Any:
        """Get External Dataset"""
        if datasetId is not None:
            return await self._get(f"/alternative/datasets/{quote(str(datasetId))}", params)
        return await self._get("/alternative/datasets", params)
    async def fear_and_greed(self, **params: Any) -> Any:
        """Fear & Greed Index API"""
        return await self._get("/alternative/fear-and-greed", params)
    async def google_trends(self, ticker: str, **params: Any) -> Any:
        """Google Trends API"""
        return await self._get(f"/alternative/google-trends/{quote(str(ticker))}", params)
    async def ingest(self, body: Any = None, **params: Any) -> Any:
        """Ingest External Dataset"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/alternative/ingest", body, params)
    async def investment_themes(self, **params: Any) -> Any:
        """Investment Themes API"""
        return await self._get("/alternative/investment-themes", params)
    async def reddit_mentions(self, ticker: str, **params: Any) -> Any:
        """Reddit Stock Mentions API"""
        return await self._get(f"/alternative/reddit-mentions/{quote(str(ticker))}", params)
    async def social_mentions(self, ticker: str, **params: Any) -> Any:
        """Social Mentions History"""
        return await self._get(f"/alternative/social-mentions/{quote(str(ticker))}", params)
    async def stocktwits(self, ticker: str, **params: Any) -> Any:
        """StockTwits Sentiment API"""
        return await self._get(f"/alternative/stocktwits/{quote(str(ticker))}", params)
    async def superinvestors_holdings(self, slug: str, **params: Any) -> Any:
        """Superinvestor Holdings API"""
        return await self._get(f"/alternative/superinvestors/holdings/{quote(str(slug))}", params)
    async def superinvestors_list(self, **params: Any) -> Any:
        """Superinvestors List API"""
        return await self._get("/alternative/superinvestors/list", params)
    async def superinvestors_recent_activity(self, **params: Any) -> Any:
        """Superinvestor Recent Activity API"""
        return await self._get("/alternative/superinvestors/recent-activity", params)
    async def superinvestors_top_holdings(self, **params: Any) -> Any:
        """Superinvestor Top Holdings API"""
        return await self._get("/alternative/superinvestors/top-holdings", params)
    async def wikipedia_pageviews(self, ticker: str, **params: Any) -> Any:
        """Wikipedia Pageviews API"""
        return await self._get(f"/alternative/wikipedia-pageviews/{quote(str(ticker))}", params)
