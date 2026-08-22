from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Macro(SyncResource):
    def countries(self) -> Any:
        return self._get("/macro/countries")

    def country(self, country: str) -> Any:
        return self._get(f"/macro/country/{quote(country)}")

    def indicator(self, country: str, slug: str) -> Any:
        return self._get(f"/macro/indicator/{quote(country)}/{quote(slug)}")

    def fred_series(self) -> Any:
        return self._get("/macro/fred/series")

    def fred_observations(self, series_id: str) -> Any:
        return self._get(f"/macro/fred/observations/{quote(series_id)}")

    def ecb_series(self) -> Any:
        return self._get("/macro/ecb/series")

    def ecb_observations(self, series_key: str) -> Any:
        return self._get(f"/macro/ecb/observations/{quote(series_key)}")

    def imf_series(self) -> Any:
        return self._get("/macro/imf/series")

    def imf_observations(self, series_id: str) -> Any:
        return self._get(f"/macro/imf/observations/{quote(series_id)}")

    def worldbank_series(self) -> Any:
        return self._get("/macro/worldbank/series")

    def worldbank_observations(self, series_id: str) -> Any:
        return self._get(f"/macro/worldbank/observations/{quote(series_id)}")

    def eurostat_series(self) -> Any:
        return self._get("/macro/eurostat/series")

    def eurostat_observations(self, series_id: str) -> Any:
        return self._get(f"/macro/eurostat/observations/{quote(series_id)}")

    def search(self, query: Optional[str] = None) -> Any:
        params = {"query": query} if query else None
        return self._get("/macro/search", params)

    def latest_fred(self) -> Any:
        return self._get("/macro/latest/fred")

    def latest_ecb(self) -> Any:
        return self._get("/macro/latest/ecb")

    def calendar_properties(self) -> Any:
        return self._get("/macro/calendar/properties")

    def calendar(self) -> Any:
        return self._get("/macro/calendar")

    def country_risk(self) -> Any:
        return self._get("/macro/country-risk")


class AsyncMacro(AsyncResource):
    async def countries(self) -> Any:
        return await self._get("/macro/countries")

    async def country(self, country: str) -> Any:
        return await self._get(f"/macro/country/{quote(country)}")

    async def indicator(self, country: str, slug: str) -> Any:
        return await self._get(f"/macro/indicator/{quote(country)}/{quote(slug)}")

    async def fred_series(self) -> Any:
        return await self._get("/macro/fred/series")

    async def fred_observations(self, series_id: str) -> Any:
        return await self._get(f"/macro/fred/observations/{quote(series_id)}")

    async def ecb_series(self) -> Any:
        return await self._get("/macro/ecb/series")

    async def ecb_observations(self, series_key: str) -> Any:
        return await self._get(f"/macro/ecb/observations/{quote(series_key)}")

    async def imf_series(self) -> Any:
        return await self._get("/macro/imf/series")

    async def imf_observations(self, series_id: str) -> Any:
        return await self._get(f"/macro/imf/observations/{quote(series_id)}")

    async def worldbank_series(self) -> Any:
        return await self._get("/macro/worldbank/series")

    async def worldbank_observations(self, series_id: str) -> Any:
        return await self._get(f"/macro/worldbank/observations/{quote(series_id)}")

    async def eurostat_series(self) -> Any:
        return await self._get("/macro/eurostat/series")

    async def eurostat_observations(self, series_id: str) -> Any:
        return await self._get(f"/macro/eurostat/observations/{quote(series_id)}")

    async def search(self, query: Optional[str] = None) -> Any:
        params = {"query": query} if query else None
        return await self._get("/macro/search", params)

    async def latest_fred(self) -> Any:
        return await self._get("/macro/latest/fred")

    async def latest_ecb(self) -> Any:
        return await self._get("/macro/latest/ecb")

    async def calendar_properties(self) -> Any:
        return await self._get("/macro/calendar/properties")

    async def calendar(self) -> Any:
        return await self._get("/macro/calendar")

    async def country_risk(self) -> Any:
        return await self._get("/macro/country-risk")
