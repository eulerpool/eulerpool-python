from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Equity(SyncResource):
    def profile(self, isin: str) -> Any:
        return self._get(f"/equity/profile/{quote(isin)}")

    def quotes(self, identifier: str) -> Any:
        return self._get(f"/equity/quotes/{quote(identifier)}")

    def balance_sheet(self, isin: str) -> Any:
        return self._get(f"/equity/balancesheet/{quote(isin)}")

    def income_statement(self, isin: str) -> Any:
        return self._get(f"/equity/incomestatement/{quote(isin)}")

    def cash_flow_statement(self, isin: str) -> Any:
        return self._get(f"/equity/cashflowstatement/{quote(isin)}")

    def ownership(self, isin: str) -> Any:
        return self._get(f"/equity/ownership/{quote(isin)}")

    def executives(self, isin: str) -> Any:
        return self._get(f"/equity/executives/{quote(isin)}")

    def peers(self, isin: str) -> Any:
        return self._get(f"/equity/peers/{quote(isin)}")

    def supply_chain(self, isin: str) -> Any:
        return self._get(f"/equity/supply-chain/{quote(isin)}")

    def segments(self, isin: str) -> Any:
        return self._get(f"/equity/segments/{quote(isin)}")

    def estimates(self, isin: str) -> Any:
        return self._get(f"/equity/estimates/{quote(isin)}")

    def splits(self, isin: str) -> Any:
        return self._get(f"/equity/splits/{quote(isin)}")

    def dividends(self, isin: str) -> Any:
        return self._get(f"/equity/dividends/{quote(isin)}")

    def dividends_by_fy(self, isin: str) -> Any:
        return self._get(f"/equity/dividends-by-fy/{quote(isin)}")

    def insider_trades(self, isin: str) -> Any:
        return self._get(f"/equity/insider-trades/{quote(isin)}")

    def esg_rating(self, isin: str) -> Any:
        return self._get(f"/equity/esg-rating/{quote(isin)}")

    def short_volume(self, isin: str) -> Any:
        return self._get(f"/equity/short-volume/{quote(isin)}")

    def short_interest_positions(self, isin: str) -> Any:
        return self._get(f"/equity/short-interest-positions/{quote(isin)}")

    def regions(self, isin: str) -> Any:
        return self._get(f"/equity/regions/{quote(isin)}")

    def country_insider_trades(self, country: str) -> Any:
        return self._get(f"/equity/country-insider-trades/{quote(country)}")

    def swot(self, isin: str) -> Any:
        return self._get(f"/equity/swot/{quote(isin)}")

    def discover(self) -> Any:
        return self._get("/equity/discover")

    def metrics(self, isin: str) -> Any:
        return self._get(f"/equity/metrics/{quote(isin)}")

    def upgrades(self, isin: str) -> Any:
        return self._get(f"/equity/upgrades/{quote(isin)}")

    def overview(self, isin: str) -> Any:
        return self._get(f"/equity/overview/{quote(isin)}")

    def income_statement_quarterly(self, isin: str) -> Any:
        return self._get(f"/equity/income-statement-quarterly/{quote(isin)}")

    def cash_flow_statement_quarterly(self, isin: str) -> Any:
        return self._get(f"/equity/cashflow-statement-quarterly/{quote(isin)}")

    def fundamentals_quarterly(self, isin: str) -> Any:
        return self._get(f"/equity/fundamentals-quarterly/{quote(isin)}")

    def aaqs(self, isin: str) -> Any:
        return self._get(f"/equity/aaqs/{quote(isin)}")

    def shares_outstanding(self, isin: str) -> Any:
        return self._get(f"/equity/shares-outstanding/{quote(isin)}")

    def market_cap(self, isin: str) -> Any:
        return self._get(f"/equity/market-cap/{quote(isin)}")

    def candles(self, isin: str) -> Any:
        return self._get(f"/equity/candles/{quote(isin)}")

    def insider_trades_derivatives(self, isin: str) -> Any:
        return self._get(f"/equity/insider-trades-derivatives/{quote(isin)}")

    def insider_trades_eu(self, isin: str) -> Any:
        return self._get(f"/equity/insider-trades-eu/{quote(isin)}")

    def valuation_history(self, isin: str) -> Any:
        return self._get(f"/equity/valuation-history/{quote(isin)}")

    def returns(self, isin: str) -> Any:
        return self._get(f"/equity/returns/{quote(isin)}")

    def growth(self, isin: str) -> Any:
        return self._get(f"/equity/growth/{quote(isin)}")

    def margins(self, isin: str) -> Any:
        return self._get(f"/equity/margins/{quote(isin)}")

    def dividend_quality(self, isin: str) -> Any:
        return self._get(f"/equity/dividend-quality/{quote(isin)}")

    def kpi(self, isin: str) -> Any:
        return self._get(f"/equity/kpi/{quote(isin)}")

    def coverage(self, isin: str) -> Any:
        return self._get(f"/equity/coverage/{quote(isin)}")

    def list(self) -> Any:
        return self._get("/equity/list")

    def search(self) -> Any:
        return self._get("/equity/search")


class AsyncEquity(AsyncResource):
    async def profile(self, isin: str) -> Any:
        return await self._get(f"/equity/profile/{quote(isin)}")

    async def quotes(self, identifier: str) -> Any:
        return await self._get(f"/equity/quotes/{quote(identifier)}")

    async def balance_sheet(self, isin: str) -> Any:
        return await self._get(f"/equity/balancesheet/{quote(isin)}")

    async def income_statement(self, isin: str) -> Any:
        return await self._get(f"/equity/incomestatement/{quote(isin)}")

    async def cash_flow_statement(self, isin: str) -> Any:
        return await self._get(f"/equity/cashflowstatement/{quote(isin)}")

    async def ownership(self, isin: str) -> Any:
        return await self._get(f"/equity/ownership/{quote(isin)}")

    async def executives(self, isin: str) -> Any:
        return await self._get(f"/equity/executives/{quote(isin)}")

    async def peers(self, isin: str) -> Any:
        return await self._get(f"/equity/peers/{quote(isin)}")

    async def supply_chain(self, isin: str) -> Any:
        return await self._get(f"/equity/supply-chain/{quote(isin)}")

    async def segments(self, isin: str) -> Any:
        return await self._get(f"/equity/segments/{quote(isin)}")

    async def estimates(self, isin: str) -> Any:
        return await self._get(f"/equity/estimates/{quote(isin)}")

    async def splits(self, isin: str) -> Any:
        return await self._get(f"/equity/splits/{quote(isin)}")

    async def dividends(self, isin: str) -> Any:
        return await self._get(f"/equity/dividends/{quote(isin)}")

    async def dividends_by_fy(self, isin: str) -> Any:
        return await self._get(f"/equity/dividends-by-fy/{quote(isin)}")

    async def insider_trades(self, isin: str) -> Any:
        return await self._get(f"/equity/insider-trades/{quote(isin)}")

    async def esg_rating(self, isin: str) -> Any:
        return await self._get(f"/equity/esg-rating/{quote(isin)}")

    async def short_volume(self, isin: str) -> Any:
        return await self._get(f"/equity/short-volume/{quote(isin)}")

    async def short_interest_positions(self, isin: str) -> Any:
        return await self._get(f"/equity/short-interest-positions/{quote(isin)}")

    async def regions(self, isin: str) -> Any:
        return await self._get(f"/equity/regions/{quote(isin)}")

    async def country_insider_trades(self, country: str) -> Any:
        return await self._get(f"/equity/country-insider-trades/{quote(country)}")

    async def swot(self, isin: str) -> Any:
        return await self._get(f"/equity/swot/{quote(isin)}")

    async def discover(self) -> Any:
        return await self._get("/equity/discover")

    async def metrics(self, isin: str) -> Any:
        return await self._get(f"/equity/metrics/{quote(isin)}")

    async def upgrades(self, isin: str) -> Any:
        return await self._get(f"/equity/upgrades/{quote(isin)}")

    async def overview(self, isin: str) -> Any:
        return await self._get(f"/equity/overview/{quote(isin)}")

    async def income_statement_quarterly(self, isin: str) -> Any:
        return await self._get(f"/equity/income-statement-quarterly/{quote(isin)}")

    async def cash_flow_statement_quarterly(self, isin: str) -> Any:
        return await self._get(f"/equity/cashflow-statement-quarterly/{quote(isin)}")

    async def fundamentals_quarterly(self, isin: str) -> Any:
        return await self._get(f"/equity/fundamentals-quarterly/{quote(isin)}")

    async def aaqs(self, isin: str) -> Any:
        return await self._get(f"/equity/aaqs/{quote(isin)}")

    async def shares_outstanding(self, isin: str) -> Any:
        return await self._get(f"/equity/shares-outstanding/{quote(isin)}")

    async def market_cap(self, isin: str) -> Any:
        return await self._get(f"/equity/market-cap/{quote(isin)}")

    async def candles(self, isin: str) -> Any:
        return await self._get(f"/equity/candles/{quote(isin)}")

    async def insider_trades_derivatives(self, isin: str) -> Any:
        return await self._get(f"/equity/insider-trades-derivatives/{quote(isin)}")

    async def insider_trades_eu(self, isin: str) -> Any:
        return await self._get(f"/equity/insider-trades-eu/{quote(isin)}")

    async def valuation_history(self, isin: str) -> Any:
        return await self._get(f"/equity/valuation-history/{quote(isin)}")

    async def returns(self, isin: str) -> Any:
        return await self._get(f"/equity/returns/{quote(isin)}")

    async def growth(self, isin: str) -> Any:
        return await self._get(f"/equity/growth/{quote(isin)}")

    async def margins(self, isin: str) -> Any:
        return await self._get(f"/equity/margins/{quote(isin)}")

    async def dividend_quality(self, isin: str) -> Any:
        return await self._get(f"/equity/dividend-quality/{quote(isin)}")

    async def kpi(self, isin: str) -> Any:
        return await self._get(f"/equity/kpi/{quote(isin)}")

    async def coverage(self, isin: str) -> Any:
        return await self._get(f"/equity/coverage/{quote(isin)}")

    async def list(self) -> Any:
        return await self._get("/equity/list")

    async def search(self) -> Any:
        return await self._get("/equity/search")
