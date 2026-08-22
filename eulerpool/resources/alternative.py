from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Alternative(SyncResource):
    def superinvestors_list(self) -> Any:
        return self._get("/alternative/superinvestors/list")

    def superinvestors_holdings(self, slug: str) -> Any:
        return self._get(f"/alternative/superinvestors/holdings/{quote(slug)}")

    def superinvestors_top_holdings(self) -> Any:
        return self._get("/alternative/superinvestors/top-holdings")

    def superinvestors_recent_activity(self) -> Any:
        return self._get("/alternative/superinvestors/recent-activity")

    def congress_trading(self) -> Any:
        return self._get("/alternative/congress-trading")

    def investment_themes(self) -> Any:
        return self._get("/alternative/investment-themes")

    def fear_and_greed(self) -> Any:
        return self._get("/alternative/fear-and-greed")

    def cot(self, symbol: str) -> Any:
        return self._get(f"/alternative/cot/{quote(symbol)}")

    def google_trends(self, ticker: str) -> Any:
        return self._get(f"/alternative/google-trends/{quote(ticker)}")

    def wikipedia_pageviews(self, ticker: str) -> Any:
        return self._get(f"/alternative/wikipedia-pageviews/{quote(ticker)}")


class AsyncAlternative(AsyncResource):
    async def superinvestors_list(self) -> Any:
        return await self._get("/alternative/superinvestors/list")

    async def superinvestors_holdings(self, slug: str) -> Any:
        return await self._get(f"/alternative/superinvestors/holdings/{quote(slug)}")

    async def superinvestors_top_holdings(self) -> Any:
        return await self._get("/alternative/superinvestors/top-holdings")

    async def superinvestors_recent_activity(self) -> Any:
        return await self._get("/alternative/superinvestors/recent-activity")

    async def congress_trading(self) -> Any:
        return await self._get("/alternative/congress-trading")

    async def investment_themes(self) -> Any:
        return await self._get("/alternative/investment-themes")

    async def fear_and_greed(self) -> Any:
        return await self._get("/alternative/fear-and-greed")

    async def cot(self, symbol: str) -> Any:
        return await self._get(f"/alternative/cot/{quote(symbol)}")

    async def google_trends(self, ticker: str) -> Any:
        return await self._get(f"/alternative/google-trends/{quote(ticker)}")

    async def wikipedia_pageviews(self, ticker: str) -> Any:
        return await self._get(f"/alternative/wikipedia-pageviews/{quote(ticker)}")
