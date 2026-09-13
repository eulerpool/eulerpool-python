from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class EquityExtended(SyncResource):
    def aaqs(self, identifier: str, **params: Any) -> Any:
        """AAQS (Quality Score) API"""
        return self._get(f"/equity-extended/aaqs/{quote(str(identifier))}", params)
    def aggregate_signals(self, identifier: str, **params: Any) -> Any:
        """Aggregate Technical Signals API"""
        return self._get(f"/equity-extended/aggregate-signals/{quote(str(identifier))}", params)
    def basic_financials(self, identifier: str, **params: Any) -> Any:
        """Basic Financials (Key Ratios) API"""
        return self._get(f"/equity-extended/basic-financials/{quote(str(identifier))}", params)
    def corporate_events(self, ticker: str, **params: Any) -> Any:
        """Corporate Events (8-K) API"""
        return self._get(f"/equity-extended/corporate-events/{quote(str(ticker))}", params)
    def earnings_calendar(self, identifier: str, **params: Any) -> Any:
        """Earnings Calendar API"""
        return self._get(f"/equity-extended/earnings-calendar/{quote(str(identifier))}", params)
    def ebitda_estimates(self, identifier: str, **params: Any) -> Any:
        """EBITDA Estimates API"""
        return self._get(f"/equity-extended/ebitda-estimates/{quote(str(identifier))}", params)
    def financials_reported(self, identifier: str, **params: Any) -> Any:
        """As-Reported Financials API"""
        return self._get(f"/equity-extended/financials-reported/{quote(str(identifier))}", params)
    def index_history(self, symbol: str, **params: Any) -> Any:
        """Index Historical Constituents API"""
        return self._get(f"/equity-extended/index-history/{quote(str(symbol))}", params)
    def isin_changes(self, **params: Any) -> Any:
        """ISIN Change History API"""
        return self._get("/equity-extended/isin-changes", params)
    def market_news(self, **params: Any) -> Any:
        """Market News API"""
        return self._get("/equity-extended/market-news", params)
    def options_chain(self, identifier: str, **params: Any) -> Any:
        """Options Chain API"""
        return self._get(f"/equity-extended/options-chain/{quote(str(identifier))}", params)
    def peers(self, identifier: str, **params: Any) -> Any:
        """Company Peers API"""
        return self._get(f"/equity-extended/peers/{quote(str(identifier))}", params)
    def price_target_history(self, identifier: str, **params: Any) -> Any:
        """Price Target History API"""
        return self._get(f"/equity-extended/price-target-history/{quote(str(identifier))}", params)
    def sec_company(self, ticker: str, **params: Any) -> Any:
        """SEC Company Info API"""
        return self._get(f"/equity-extended/sec-company/{quote(str(ticker))}", params)
    def sec_filings(self, identifier: str, **params: Any) -> Any:
        """SEC Filings API"""
        return self._get(f"/equity-extended/sec-filings/{quote(str(identifier))}", params)
    def short_interest(self, identifier: str, **params: Any) -> Any:
        """Short Interest API"""
        return self._get(f"/equity-extended/short-interest/{quote(str(identifier))}", params)
    def short_volume(self, identifier: str, **params: Any) -> Any:
        """Short Volume API"""
        return self._get(f"/equity-extended/short-volume/{quote(str(identifier))}", params)
    def supply_chain(self, ticker: str, **params: Any) -> Any:
        """Supply Chain Relationships API"""
        return self._get(f"/equity-extended/supply-chain/{quote(str(ticker))}", params)
    def symbol_changes(self, **params: Any) -> Any:
        """Symbol Change History API"""
        return self._get("/equity-extended/symbol-changes", params)
    def tech_indicators(self, identifier: str, **params: Any) -> Any:
        """Technical Indicators Time Series API"""
        return self._get(f"/equity-extended/tech-indicators/{quote(str(identifier))}", params)
    def technical_signals(self, identifier: str, **params: Any) -> Any:
        """Technical Signals API"""
        return self._get(f"/equity-extended/technical-signals/{quote(str(identifier))}", params)
    def xbrl_fact(self, ticker: str, tag: str, **params: Any) -> Any:
        """XBRL Fact Time Series API"""
        return self._get(f"/equity-extended/xbrl/fact/{quote(str(ticker))}/{quote(str(tag))}", params)
    def xbrl_facts(self, ticker: str, **params: Any) -> Any:
        """SEC XBRL Facts API"""
        return self._get(f"/equity-extended/xbrl/facts/{quote(str(ticker))}", params)


class AsyncEquityExtended(AsyncResource):
    async def aaqs(self, identifier: str, **params: Any) -> Any:
        """AAQS (Quality Score) API"""
        return await self._get(f"/equity-extended/aaqs/{quote(str(identifier))}", params)
    async def aggregate_signals(self, identifier: str, **params: Any) -> Any:
        """Aggregate Technical Signals API"""
        return await self._get(f"/equity-extended/aggregate-signals/{quote(str(identifier))}", params)
    async def basic_financials(self, identifier: str, **params: Any) -> Any:
        """Basic Financials (Key Ratios) API"""
        return await self._get(f"/equity-extended/basic-financials/{quote(str(identifier))}", params)
    async def corporate_events(self, ticker: str, **params: Any) -> Any:
        """Corporate Events (8-K) API"""
        return await self._get(f"/equity-extended/corporate-events/{quote(str(ticker))}", params)
    async def earnings_calendar(self, identifier: str, **params: Any) -> Any:
        """Earnings Calendar API"""
        return await self._get(f"/equity-extended/earnings-calendar/{quote(str(identifier))}", params)
    async def ebitda_estimates(self, identifier: str, **params: Any) -> Any:
        """EBITDA Estimates API"""
        return await self._get(f"/equity-extended/ebitda-estimates/{quote(str(identifier))}", params)
    async def financials_reported(self, identifier: str, **params: Any) -> Any:
        """As-Reported Financials API"""
        return await self._get(f"/equity-extended/financials-reported/{quote(str(identifier))}", params)
    async def index_history(self, symbol: str, **params: Any) -> Any:
        """Index Historical Constituents API"""
        return await self._get(f"/equity-extended/index-history/{quote(str(symbol))}", params)
    async def isin_changes(self, **params: Any) -> Any:
        """ISIN Change History API"""
        return await self._get("/equity-extended/isin-changes", params)
    async def market_news(self, **params: Any) -> Any:
        """Market News API"""
        return await self._get("/equity-extended/market-news", params)
    async def options_chain(self, identifier: str, **params: Any) -> Any:
        """Options Chain API"""
        return await self._get(f"/equity-extended/options-chain/{quote(str(identifier))}", params)
    async def peers(self, identifier: str, **params: Any) -> Any:
        """Company Peers API"""
        return await self._get(f"/equity-extended/peers/{quote(str(identifier))}", params)
    async def price_target_history(self, identifier: str, **params: Any) -> Any:
        """Price Target History API"""
        return await self._get(f"/equity-extended/price-target-history/{quote(str(identifier))}", params)
    async def sec_company(self, ticker: str, **params: Any) -> Any:
        """SEC Company Info API"""
        return await self._get(f"/equity-extended/sec-company/{quote(str(ticker))}", params)
    async def sec_filings(self, identifier: str, **params: Any) -> Any:
        """SEC Filings API"""
        return await self._get(f"/equity-extended/sec-filings/{quote(str(identifier))}", params)
    async def short_interest(self, identifier: str, **params: Any) -> Any:
        """Short Interest API"""
        return await self._get(f"/equity-extended/short-interest/{quote(str(identifier))}", params)
    async def short_volume(self, identifier: str, **params: Any) -> Any:
        """Short Volume API"""
        return await self._get(f"/equity-extended/short-volume/{quote(str(identifier))}", params)
    async def supply_chain(self, ticker: str, **params: Any) -> Any:
        """Supply Chain Relationships API"""
        return await self._get(f"/equity-extended/supply-chain/{quote(str(ticker))}", params)
    async def symbol_changes(self, **params: Any) -> Any:
        """Symbol Change History API"""
        return await self._get("/equity-extended/symbol-changes", params)
    async def tech_indicators(self, identifier: str, **params: Any) -> Any:
        """Technical Indicators Time Series API"""
        return await self._get(f"/equity-extended/tech-indicators/{quote(str(identifier))}", params)
    async def technical_signals(self, identifier: str, **params: Any) -> Any:
        """Technical Signals API"""
        return await self._get(f"/equity-extended/technical-signals/{quote(str(identifier))}", params)
    async def xbrl_fact(self, ticker: str, tag: str, **params: Any) -> Any:
        """XBRL Fact Time Series API"""
        return await self._get(f"/equity-extended/xbrl/fact/{quote(str(ticker))}/{quote(str(tag))}", params)
    async def xbrl_facts(self, ticker: str, **params: Any) -> Any:
        """SEC XBRL Facts API"""
        return await self._get(f"/equity-extended/xbrl/facts/{quote(str(ticker))}", params)
