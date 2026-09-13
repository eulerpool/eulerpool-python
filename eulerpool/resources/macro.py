from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Macro(SyncResource):
    def bis_credit_gap(self, **params: Any) -> Any:
        """BIS Credit Gap API"""
        return self._get("/macro/bis/credit-gap", params)
    def bis_debt_securities(self, **params: Any) -> Any:
        """BIS Debt Securities API"""
        return self._get("/macro/bis/debt-securities", params)
    def bis_property_prices(self, **params: Any) -> Any:
        """BIS Property Prices API"""
        return self._get("/macro/bis/property-prices", params)
    def calendar(self, **params: Any) -> Any:
        """Macro Calendar API"""
        return self._get("/macro/calendar", params)
    def calendar_properties(self, **params: Any) -> Any:
        """Macro Calendar properties API"""
        return self._get("/macro/calendar/properties", params)
    def countries(self, **params: Any) -> Any:
        """Available Countries API"""
        return self._get("/macro/countries", params)
    def country(self, country: str, **params: Any) -> Any:
        """Country Indicators API"""
        return self._get(f"/macro/country/{quote(str(country))}", params)
    def country_risk(self, **params: Any) -> Any:
        """Country Risk API"""
        return self._get("/macro/country-risk", params)
    def credit_spreads(self, **params: Any) -> Any:
        """Credit Spreads API"""
        return self._get("/macro/credit-spreads", params)
    def ecb_observations(self, seriesKey: str, **params: Any) -> Any:
        """ECB Observations API"""
        return self._get(f"/macro/ecb/observations/{quote(str(seriesKey))}", params)
    def ecb_series(self, **params: Any) -> Any:
        """ECB Series List API"""
        return self._get("/macro/ecb/series", params)
    def eurostat_observations(self, seriesId: str, **params: Any) -> Any:
        """Eurostat Observations API"""
        return self._get(f"/macro/eurostat/observations/{quote(str(seriesId))}", params)
    def eurostat_series(self, **params: Any) -> Any:
        """Eurostat Series List API"""
        return self._get("/macro/eurostat/series", params)
    def fred_observations(self, seriesId: str, **params: Any) -> Any:
        """FRED Observations API"""
        return self._get(f"/macro/fred/observations/{quote(str(seriesId))}", params)
    def fred_series(self, **params: Any) -> Any:
        """FRED Series List API"""
        return self._get("/macro/fred/series", params)
    def imf_observations(self, seriesId: str, **params: Any) -> Any:
        """IMF Observations API"""
        return self._get(f"/macro/imf/observations/{quote(str(seriesId))}", params)
    def imf_series(self, **params: Any) -> Any:
        """IMF Series List API"""
        return self._get("/macro/imf/series", params)
    def indicator(self, country: str, slug: str, **params: Any) -> Any:
        """Indicator Profile API"""
        return self._get(f"/macro/indicator/{quote(str(country))}/{quote(str(slug))}", params)
    def latest_ecb(self, **params: Any) -> Any:
        """ECB Latest Values API"""
        return self._get("/macro/latest/ecb", params)
    def latest_fred(self, **params: Any) -> Any:
        """FRED Latest Values API"""
        return self._get("/macro/latest/fred", params)
    def oecd(self, **params: Any) -> Any:
        """OECD Indicators API"""
        return self._get("/macro/oecd", params)
    def search(self, **params: Any) -> Any:
        """Macro Data Search API"""
        return self._get("/macro/search", params)
    def worldbank_observations(self, seriesId: str, **params: Any) -> Any:
        """World Bank Observations API"""
        return self._get(f"/macro/worldbank/observations/{quote(str(seriesId))}", params)
    def worldbank_series(self, **params: Any) -> Any:
        """World Bank Series List API"""
        return self._get("/macro/worldbank/series", params)


class AsyncMacro(AsyncResource):
    async def bis_credit_gap(self, **params: Any) -> Any:
        """BIS Credit Gap API"""
        return await self._get("/macro/bis/credit-gap", params)
    async def bis_debt_securities(self, **params: Any) -> Any:
        """BIS Debt Securities API"""
        return await self._get("/macro/bis/debt-securities", params)
    async def bis_property_prices(self, **params: Any) -> Any:
        """BIS Property Prices API"""
        return await self._get("/macro/bis/property-prices", params)
    async def calendar(self, **params: Any) -> Any:
        """Macro Calendar API"""
        return await self._get("/macro/calendar", params)
    async def calendar_properties(self, **params: Any) -> Any:
        """Macro Calendar properties API"""
        return await self._get("/macro/calendar/properties", params)
    async def countries(self, **params: Any) -> Any:
        """Available Countries API"""
        return await self._get("/macro/countries", params)
    async def country(self, country: str, **params: Any) -> Any:
        """Country Indicators API"""
        return await self._get(f"/macro/country/{quote(str(country))}", params)
    async def country_risk(self, **params: Any) -> Any:
        """Country Risk API"""
        return await self._get("/macro/country-risk", params)
    async def credit_spreads(self, **params: Any) -> Any:
        """Credit Spreads API"""
        return await self._get("/macro/credit-spreads", params)
    async def ecb_observations(self, seriesKey: str, **params: Any) -> Any:
        """ECB Observations API"""
        return await self._get(f"/macro/ecb/observations/{quote(str(seriesKey))}", params)
    async def ecb_series(self, **params: Any) -> Any:
        """ECB Series List API"""
        return await self._get("/macro/ecb/series", params)
    async def eurostat_observations(self, seriesId: str, **params: Any) -> Any:
        """Eurostat Observations API"""
        return await self._get(f"/macro/eurostat/observations/{quote(str(seriesId))}", params)
    async def eurostat_series(self, **params: Any) -> Any:
        """Eurostat Series List API"""
        return await self._get("/macro/eurostat/series", params)
    async def fred_observations(self, seriesId: str, **params: Any) -> Any:
        """FRED Observations API"""
        return await self._get(f"/macro/fred/observations/{quote(str(seriesId))}", params)
    async def fred_series(self, **params: Any) -> Any:
        """FRED Series List API"""
        return await self._get("/macro/fred/series", params)
    async def imf_observations(self, seriesId: str, **params: Any) -> Any:
        """IMF Observations API"""
        return await self._get(f"/macro/imf/observations/{quote(str(seriesId))}", params)
    async def imf_series(self, **params: Any) -> Any:
        """IMF Series List API"""
        return await self._get("/macro/imf/series", params)
    async def indicator(self, country: str, slug: str, **params: Any) -> Any:
        """Indicator Profile API"""
        return await self._get(f"/macro/indicator/{quote(str(country))}/{quote(str(slug))}", params)
    async def latest_ecb(self, **params: Any) -> Any:
        """ECB Latest Values API"""
        return await self._get("/macro/latest/ecb", params)
    async def latest_fred(self, **params: Any) -> Any:
        """FRED Latest Values API"""
        return await self._get("/macro/latest/fred", params)
    async def oecd(self, **params: Any) -> Any:
        """OECD Indicators API"""
        return await self._get("/macro/oecd", params)
    async def search(self, **params: Any) -> Any:
        """Macro Data Search API"""
        return await self._get("/macro/search", params)
    async def worldbank_observations(self, seriesId: str, **params: Any) -> Any:
        """World Bank Observations API"""
        return await self._get(f"/macro/worldbank/observations/{quote(str(seriesId))}", params)
    async def worldbank_series(self, **params: Any) -> Any:
        """World Bank Series List API"""
        return await self._get("/macro/worldbank/series", params)
