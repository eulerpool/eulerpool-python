from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Equity(SyncResource):
    def aaqs(self, identifier: str, **params: Any) -> Any:
        """AAQS Quality Score API"""
        return self._get(f"/equity/aaqs/{quote(str(identifier))}", params)
    def analyst_grades(self, identifier: str, **params: Any) -> Any:
        """Analyst Grades API"""
        return self._get(f"/equity/analyst-grades/{quote(str(identifier))}", params)
    def balance_sheet(self, identifier: str, **params: Any) -> Any:
        """Balance Sheet API"""
        return self._get(f"/equity/balancesheet/{quote(str(identifier))}", params)
    balancesheet = balance_sheet
    def beneficial_ownership(self, identifier: str, **params: Any) -> Any:
        """Beneficial Ownership API"""
        return self._get(f"/equity/beneficial-ownership/{quote(str(identifier))}", params)
    def candles(self, identifier: str, **params: Any) -> Any:
        """Stock OHLCV Candles API"""
        return self._get(f"/equity/candles/{quote(str(identifier))}", params)
    def cash_flow_statement(self, identifier: str, **params: Any) -> Any:
        """Cash Flow Statement API"""
        return self._get(f"/equity/cashflowstatement/{quote(str(identifier))}", params)
    cashflowstatement = cash_flow_statement
    def cashflow_statement_quarterly(self, identifier: str, **params: Any) -> Any:
        """Quarterly Cash Flow Statement API"""
        return self._get(f"/equity/cashflow-statement-quarterly/{quote(str(identifier))}", params)
    def country_insider_trades(self, country: str, **params: Any) -> Any:
        """Country Insider Trades API"""
        return self._get(f"/equity/country-insider-trades/{quote(str(country))}", params)
    def coverage(self, identifier: str, **params: Any) -> Any:
        """Data Coverage API"""
        return self._get(f"/equity/coverage/{quote(str(identifier))}", params)
    def discover(self, **params: Any) -> Any:
        """Discover Stocks API"""
        return self._get("/equity/discover", params)
    def dividend_quality(self, identifier: str, **params: Any) -> Any:
        """Dividend Quality API"""
        return self._get(f"/equity/dividend-quality/{quote(str(identifier))}", params)
    def dividend_safety(self, ticker: str, **params: Any) -> Any:
        """Dividend Safety Score API"""
        return self._get(f"/equity/dividend-safety/{quote(str(ticker))}", params)
    def dividends(self, identifier: str, **params: Any) -> Any:
        """Dividends API"""
        return self._get(f"/equity/dividends/{quote(str(identifier))}", params)
    def dividends_by_fy(self, identifier: str, **params: Any) -> Any:
        """Dividends by Fiscal Year API"""
        return self._get(f"/equity/dividends-by-fy/{quote(str(identifier))}", params)
    def employees(self, identifier: str, **params: Any) -> Any:
        """Employee Count History API"""
        return self._get(f"/equity/employees/{quote(str(identifier))}", params)
    def esg_rating(self, identifier: str, **params: Any) -> Any:
        """ESG Rating API"""
        return self._get(f"/equity/esg-rating/{quote(str(identifier))}", params)
    def estimates(self, identifier: str, **params: Any) -> Any:
        """Analyst Estimates API"""
        return self._get(f"/equity/estimates/{quote(str(identifier))}", params)
    def etf_exposure(self, identifier: str, **params: Any) -> Any:
        """ETF Exposure"""
        return self._get(f"/equity/etf-exposure/{quote(str(identifier))}", params)
    def executives(self, identifier: str, **params: Any) -> Any:
        """Company Executives API"""
        return self._get(f"/equity/executives/{quote(str(identifier))}", params)
    def forecast(self, identifier: str, **params: Any) -> Any:
        """Analyst Forecast Detail"""
        return self._get(f"/equity/forecast/{quote(str(identifier))}", params)
    def fundamentals_quarterly(self, identifier: str, **params: Any) -> Any:
        """Quarterly Fundamentals API"""
        return self._get(f"/equity/fundamentals-quarterly/{quote(str(identifier))}", params)
    def grade_news(self, **params: Any) -> Any:
        """Analyst Grade News (Market-Wide)"""
        return self._get("/equity/grade-news", params)
    def growth(self, identifier: str, **params: Any) -> Any:
        """Growth Metrics API"""
        return self._get(f"/equity/growth/{quote(str(identifier))}", params)
    def income_statement(self, identifier: str, **params: Any) -> Any:
        """Income Statement API"""
        return self._get(f"/equity/incomestatement/{quote(str(identifier))}", params)
    incomestatement = income_statement
    def income_statement_quarterly(self, identifier: str, **params: Any) -> Any:
        """Quarterly Income Statement API"""
        return self._get(f"/equity/income-statement-quarterly/{quote(str(identifier))}", params)
    def insider_trades(self, identifier: str, **params: Any) -> Any:
        """Insider Trades API"""
        return self._get(f"/equity/insider-trades/{quote(str(identifier))}", params)
    def insider_trades_derivatives(self, identifier: str, **params: Any) -> Any:
        """SEC Derivative Insider Trades API"""
        return self._get(f"/equity/insider-trades-derivatives/{quote(str(identifier))}", params)
    def insider_trades_eu(self, identifier: str, **params: Any) -> Any:
        """EU Insider Trades API"""
        return self._get(f"/equity/insider-trades-eu/{quote(str(identifier))}", params)
    def key_figures(self, identifier: str, **params: Any) -> Any:
        """Company Key Figures"""
        return self._get(f"/equity/key-figures/{quote(str(identifier))}", params)
    def kpi(self, identifier: str, **params: Any) -> Any:
        """KPI Bundle API"""
        return self._get(f"/equity/kpi/{quote(str(identifier))}", params)
    def list(self, **params: Any) -> Any:
        """List All Stocks API"""
        return self._get("/equity/list", params)
    def margins(self, identifier: str, **params: Any) -> Any:
        """Margin Data API"""
        return self._get(f"/equity/margins/{quote(str(identifier))}", params)
    def market_cap(self, identifier: str, **params: Any) -> Any:
        """Historical Market Cap API"""
        return self._get(f"/equity/market-cap/{quote(str(identifier))}", params)
    def market_cap_history(self, identifier: str, **params: Any) -> Any:
        """Market Cap History (Vendor)"""
        return self._get(f"/equity/market-cap-history/{quote(str(identifier))}", params)
    def market_multiples(self, type: str, **params: Any) -> Any:
        """Market-Wide Valuation Multiples"""
        return self._get(f"/equity/market-multiples/{quote(str(type))}", params)
    def metrics(self, identifier: str, **params: Any) -> Any:
        """Financial Metrics & Ratios API"""
        return self._get(f"/equity/metrics/{quote(str(identifier))}", params)
    def overview(self, identifier: str, **params: Any) -> Any:
        """Company Overview API"""
        return self._get(f"/equity/overview/{quote(str(identifier))}", params)
    def ownership(self, identifier: str, **params: Any) -> Any:
        """Stock Ownership API"""
        return self._get(f"/equity/ownership/{quote(str(identifier))}", params)
    def peers(self, identifier: str, **params: Any) -> Any:
        """Company Peers API"""
        return self._get(f"/equity/peers/{quote(str(identifier))}", params)
    def pit_estimates(self, ticker: str, **params: Any) -> Any:
        """Point-in-Time Estimates API"""
        return self._get(f"/equity/pit/estimates/{quote(str(ticker))}", params)
    def pit_profile(self, identifier: str, **params: Any) -> Any:
        """Point-in-Time Profile API"""
        return self._get(f"/equity/pit/profile/{quote(str(identifier))}", params)
    def price_change(self, identifier: str, **params: Any) -> Any:
        """Price Change Summary"""
        return self._get(f"/equity/price-change/{quote(str(identifier))}", params)
    def price_target(self, identifier: str, **params: Any) -> Any:
        """Current Analyst Price Target Consensus"""
        return self._get(f"/equity/price-target/{quote(str(identifier))}", params)
    def price_target_consensus(self, identifier: str, **params: Any) -> Any:
        """Price Target Consensus API"""
        return self._get(f"/equity/price-target-consensus/{quote(str(identifier))}", params)
    def price_target_news(self, identifier: str, **params: Any) -> Any:
        """Price Target News"""
        return self._get(f"/equity/price-target-news/{quote(str(identifier))}", params)
    def price_target_news_latest(self, **params: Any) -> Any:
        """Price Target News (Market-Wide)"""
        return self._get("/equity/price-target-news-latest", params)
    def profile(self, identifier: str, **params: Any) -> Any:
        """Profile API"""
        return self._get(f"/equity/profile/{quote(str(identifier))}", params)
    def quality_scores(self, ticker: str, **params: Any) -> Any:
        """Quality Scores API"""
        return self._get(f"/equity/quality-scores/{quote(str(ticker))}", params)
    def quotes(self, identifier: str, **params: Any) -> Any:
        """Quote API"""
        return self._get(f"/equity/quotes/{quote(str(identifier))}", params)
    def regions(self, identifier: str, **params: Any) -> Any:
        """Revenue by Region API"""
        return self._get(f"/equity/regions/{quote(str(identifier))}", params)
    def relative_move(self, identifier: str, **params: Any) -> Any:
        """Relative Price Move"""
        return self._get(f"/equity/relative-move/{quote(str(identifier))}", params)
    def returns(self, identifier: str, **params: Any) -> Any:
        """Stock Returns API"""
        return self._get(f"/equity/returns/{quote(str(identifier))}", params)
    def search(self, **params: Any) -> Any:
        """Stock Search API"""
        return self._get("/equity/search", params)
    def sec_form4(self, identifier: str, **params: Any) -> Any:
        """SEC Form 4 Insider Trades API"""
        return self._get(f"/equity/sec-form4/{quote(str(identifier))}", params)
    def sec_ftd(self, ticker: str, **params: Any) -> Any:
        """SEC Fail-to-Deliver API"""
        return self._get(f"/equity/sec-ftd/{quote(str(ticker))}", params)
    def segments(self, identifier: str, **params: Any) -> Any:
        """Business Segments API"""
        return self._get(f"/equity/segments/{quote(str(identifier))}", params)
    def segments_history(self, identifier: str, **params: Any) -> Any:
        """Revenue Segments History API"""
        return self._get(f"/equity/segments-history/{quote(str(identifier))}", params)
    def shares_float(self, identifier: str, **params: Any) -> Any:
        """Shares Float API"""
        return self._get(f"/equity/shares-float/{quote(str(identifier))}", params)
    def shares_outstanding(self, identifier: str, **params: Any) -> Any:
        """Historical Shares Outstanding API"""
        return self._get(f"/equity/shares-outstanding/{quote(str(identifier))}", params)
    def short_interest_positions(self, identifier: str, **params: Any) -> Any:
        """Short Interest Positions API"""
        return self._get(f"/equity/short-interest-positions/{quote(str(identifier))}", params)
    def short_volume(self, identifier: str, **params: Any) -> Any:
        """Short Volume API"""
        return self._get(f"/equity/short-volume/{quote(str(identifier))}", params)
    def splits(self, identifier: str, **params: Any) -> Any:
        """Stock Splits API"""
        return self._get(f"/equity/splits/{quote(str(identifier))}", params)
    def supply_chain(self, identifier: str, **params: Any) -> Any:
        """Supply Chain API"""
        return self._get(f"/equity/supply-chain/{quote(str(identifier))}", params)
    def swot(self, identifier: str, **params: Any) -> Any:
        """SWOT Analysis API"""
        return self._get(f"/equity/swot/{quote(str(identifier))}", params)
    def upgrades(self, identifier: str, **params: Any) -> Any:
        """Analyst Upgrade/Downgrade History API"""
        return self._get(f"/equity/upgrades/{quote(str(identifier))}", params)
    def valuation_history(self, identifier: str, **params: Any) -> Any:
        """Valuation History API"""
        return self._get(f"/equity/valuation-history/{quote(str(identifier))}", params)
    def vendor_ratings(self, identifier: str, **params: Any) -> Any:
        """Vendor Analyst Ratings"""
        return self._get(f"/equity/vendor-ratings/{quote(str(identifier))}", params)


class AsyncEquity(AsyncResource):
    async def aaqs(self, identifier: str, **params: Any) -> Any:
        """AAQS Quality Score API"""
        return await self._get(f"/equity/aaqs/{quote(str(identifier))}", params)
    async def analyst_grades(self, identifier: str, **params: Any) -> Any:
        """Analyst Grades API"""
        return await self._get(f"/equity/analyst-grades/{quote(str(identifier))}", params)
    async def balance_sheet(self, identifier: str, **params: Any) -> Any:
        """Balance Sheet API"""
        return await self._get(f"/equity/balancesheet/{quote(str(identifier))}", params)
    balancesheet = balance_sheet
    async def beneficial_ownership(self, identifier: str, **params: Any) -> Any:
        """Beneficial Ownership API"""
        return await self._get(f"/equity/beneficial-ownership/{quote(str(identifier))}", params)
    async def candles(self, identifier: str, **params: Any) -> Any:
        """Stock OHLCV Candles API"""
        return await self._get(f"/equity/candles/{quote(str(identifier))}", params)
    async def cash_flow_statement(self, identifier: str, **params: Any) -> Any:
        """Cash Flow Statement API"""
        return await self._get(f"/equity/cashflowstatement/{quote(str(identifier))}", params)
    cashflowstatement = cash_flow_statement
    async def cashflow_statement_quarterly(self, identifier: str, **params: Any) -> Any:
        """Quarterly Cash Flow Statement API"""
        return await self._get(f"/equity/cashflow-statement-quarterly/{quote(str(identifier))}", params)
    async def country_insider_trades(self, country: str, **params: Any) -> Any:
        """Country Insider Trades API"""
        return await self._get(f"/equity/country-insider-trades/{quote(str(country))}", params)
    async def coverage(self, identifier: str, **params: Any) -> Any:
        """Data Coverage API"""
        return await self._get(f"/equity/coverage/{quote(str(identifier))}", params)
    async def discover(self, **params: Any) -> Any:
        """Discover Stocks API"""
        return await self._get("/equity/discover", params)
    async def dividend_quality(self, identifier: str, **params: Any) -> Any:
        """Dividend Quality API"""
        return await self._get(f"/equity/dividend-quality/{quote(str(identifier))}", params)
    async def dividend_safety(self, ticker: str, **params: Any) -> Any:
        """Dividend Safety Score API"""
        return await self._get(f"/equity/dividend-safety/{quote(str(ticker))}", params)
    async def dividends(self, identifier: str, **params: Any) -> Any:
        """Dividends API"""
        return await self._get(f"/equity/dividends/{quote(str(identifier))}", params)
    async def dividends_by_fy(self, identifier: str, **params: Any) -> Any:
        """Dividends by Fiscal Year API"""
        return await self._get(f"/equity/dividends-by-fy/{quote(str(identifier))}", params)
    async def employees(self, identifier: str, **params: Any) -> Any:
        """Employee Count History API"""
        return await self._get(f"/equity/employees/{quote(str(identifier))}", params)
    async def esg_rating(self, identifier: str, **params: Any) -> Any:
        """ESG Rating API"""
        return await self._get(f"/equity/esg-rating/{quote(str(identifier))}", params)
    async def estimates(self, identifier: str, **params: Any) -> Any:
        """Analyst Estimates API"""
        return await self._get(f"/equity/estimates/{quote(str(identifier))}", params)
    async def etf_exposure(self, identifier: str, **params: Any) -> Any:
        """ETF Exposure"""
        return await self._get(f"/equity/etf-exposure/{quote(str(identifier))}", params)
    async def executives(self, identifier: str, **params: Any) -> Any:
        """Company Executives API"""
        return await self._get(f"/equity/executives/{quote(str(identifier))}", params)
    async def forecast(self, identifier: str, **params: Any) -> Any:
        """Analyst Forecast Detail"""
        return await self._get(f"/equity/forecast/{quote(str(identifier))}", params)
    async def fundamentals_quarterly(self, identifier: str, **params: Any) -> Any:
        """Quarterly Fundamentals API"""
        return await self._get(f"/equity/fundamentals-quarterly/{quote(str(identifier))}", params)
    async def grade_news(self, **params: Any) -> Any:
        """Analyst Grade News (Market-Wide)"""
        return await self._get("/equity/grade-news", params)
    async def growth(self, identifier: str, **params: Any) -> Any:
        """Growth Metrics API"""
        return await self._get(f"/equity/growth/{quote(str(identifier))}", params)
    async def income_statement(self, identifier: str, **params: Any) -> Any:
        """Income Statement API"""
        return await self._get(f"/equity/incomestatement/{quote(str(identifier))}", params)
    incomestatement = income_statement
    async def income_statement_quarterly(self, identifier: str, **params: Any) -> Any:
        """Quarterly Income Statement API"""
        return await self._get(f"/equity/income-statement-quarterly/{quote(str(identifier))}", params)
    async def insider_trades(self, identifier: str, **params: Any) -> Any:
        """Insider Trades API"""
        return await self._get(f"/equity/insider-trades/{quote(str(identifier))}", params)
    async def insider_trades_derivatives(self, identifier: str, **params: Any) -> Any:
        """SEC Derivative Insider Trades API"""
        return await self._get(f"/equity/insider-trades-derivatives/{quote(str(identifier))}", params)
    async def insider_trades_eu(self, identifier: str, **params: Any) -> Any:
        """EU Insider Trades API"""
        return await self._get(f"/equity/insider-trades-eu/{quote(str(identifier))}", params)
    async def key_figures(self, identifier: str, **params: Any) -> Any:
        """Company Key Figures"""
        return await self._get(f"/equity/key-figures/{quote(str(identifier))}", params)
    async def kpi(self, identifier: str, **params: Any) -> Any:
        """KPI Bundle API"""
        return await self._get(f"/equity/kpi/{quote(str(identifier))}", params)
    async def list(self, **params: Any) -> Any:
        """List All Stocks API"""
        return await self._get("/equity/list", params)
    async def margins(self, identifier: str, **params: Any) -> Any:
        """Margin Data API"""
        return await self._get(f"/equity/margins/{quote(str(identifier))}", params)
    async def market_cap(self, identifier: str, **params: Any) -> Any:
        """Historical Market Cap API"""
        return await self._get(f"/equity/market-cap/{quote(str(identifier))}", params)
    async def market_cap_history(self, identifier: str, **params: Any) -> Any:
        """Market Cap History (Vendor)"""
        return await self._get(f"/equity/market-cap-history/{quote(str(identifier))}", params)
    async def market_multiples(self, type: str, **params: Any) -> Any:
        """Market-Wide Valuation Multiples"""
        return await self._get(f"/equity/market-multiples/{quote(str(type))}", params)
    async def metrics(self, identifier: str, **params: Any) -> Any:
        """Financial Metrics & Ratios API"""
        return await self._get(f"/equity/metrics/{quote(str(identifier))}", params)
    async def overview(self, identifier: str, **params: Any) -> Any:
        """Company Overview API"""
        return await self._get(f"/equity/overview/{quote(str(identifier))}", params)
    async def ownership(self, identifier: str, **params: Any) -> Any:
        """Stock Ownership API"""
        return await self._get(f"/equity/ownership/{quote(str(identifier))}", params)
    async def peers(self, identifier: str, **params: Any) -> Any:
        """Company Peers API"""
        return await self._get(f"/equity/peers/{quote(str(identifier))}", params)
    async def pit_estimates(self, ticker: str, **params: Any) -> Any:
        """Point-in-Time Estimates API"""
        return await self._get(f"/equity/pit/estimates/{quote(str(ticker))}", params)
    async def pit_profile(self, identifier: str, **params: Any) -> Any:
        """Point-in-Time Profile API"""
        return await self._get(f"/equity/pit/profile/{quote(str(identifier))}", params)
    async def price_change(self, identifier: str, **params: Any) -> Any:
        """Price Change Summary"""
        return await self._get(f"/equity/price-change/{quote(str(identifier))}", params)
    async def price_target(self, identifier: str, **params: Any) -> Any:
        """Current Analyst Price Target Consensus"""
        return await self._get(f"/equity/price-target/{quote(str(identifier))}", params)
    async def price_target_consensus(self, identifier: str, **params: Any) -> Any:
        """Price Target Consensus API"""
        return await self._get(f"/equity/price-target-consensus/{quote(str(identifier))}", params)
    async def price_target_news(self, identifier: str, **params: Any) -> Any:
        """Price Target News"""
        return await self._get(f"/equity/price-target-news/{quote(str(identifier))}", params)
    async def price_target_news_latest(self, **params: Any) -> Any:
        """Price Target News (Market-Wide)"""
        return await self._get("/equity/price-target-news-latest", params)
    async def profile(self, identifier: str, **params: Any) -> Any:
        """Profile API"""
        return await self._get(f"/equity/profile/{quote(str(identifier))}", params)
    async def quality_scores(self, ticker: str, **params: Any) -> Any:
        """Quality Scores API"""
        return await self._get(f"/equity/quality-scores/{quote(str(ticker))}", params)
    async def quotes(self, identifier: str, **params: Any) -> Any:
        """Quote API"""
        return await self._get(f"/equity/quotes/{quote(str(identifier))}", params)
    async def regions(self, identifier: str, **params: Any) -> Any:
        """Revenue by Region API"""
        return await self._get(f"/equity/regions/{quote(str(identifier))}", params)
    async def relative_move(self, identifier: str, **params: Any) -> Any:
        """Relative Price Move"""
        return await self._get(f"/equity/relative-move/{quote(str(identifier))}", params)
    async def returns(self, identifier: str, **params: Any) -> Any:
        """Stock Returns API"""
        return await self._get(f"/equity/returns/{quote(str(identifier))}", params)
    async def search(self, **params: Any) -> Any:
        """Stock Search API"""
        return await self._get("/equity/search", params)
    async def sec_form4(self, identifier: str, **params: Any) -> Any:
        """SEC Form 4 Insider Trades API"""
        return await self._get(f"/equity/sec-form4/{quote(str(identifier))}", params)
    async def sec_ftd(self, ticker: str, **params: Any) -> Any:
        """SEC Fail-to-Deliver API"""
        return await self._get(f"/equity/sec-ftd/{quote(str(ticker))}", params)
    async def segments(self, identifier: str, **params: Any) -> Any:
        """Business Segments API"""
        return await self._get(f"/equity/segments/{quote(str(identifier))}", params)
    async def segments_history(self, identifier: str, **params: Any) -> Any:
        """Revenue Segments History API"""
        return await self._get(f"/equity/segments-history/{quote(str(identifier))}", params)
    async def shares_float(self, identifier: str, **params: Any) -> Any:
        """Shares Float API"""
        return await self._get(f"/equity/shares-float/{quote(str(identifier))}", params)
    async def shares_outstanding(self, identifier: str, **params: Any) -> Any:
        """Historical Shares Outstanding API"""
        return await self._get(f"/equity/shares-outstanding/{quote(str(identifier))}", params)
    async def short_interest_positions(self, identifier: str, **params: Any) -> Any:
        """Short Interest Positions API"""
        return await self._get(f"/equity/short-interest-positions/{quote(str(identifier))}", params)
    async def short_volume(self, identifier: str, **params: Any) -> Any:
        """Short Volume API"""
        return await self._get(f"/equity/short-volume/{quote(str(identifier))}", params)
    async def splits(self, identifier: str, **params: Any) -> Any:
        """Stock Splits API"""
        return await self._get(f"/equity/splits/{quote(str(identifier))}", params)
    async def supply_chain(self, identifier: str, **params: Any) -> Any:
        """Supply Chain API"""
        return await self._get(f"/equity/supply-chain/{quote(str(identifier))}", params)
    async def swot(self, identifier: str, **params: Any) -> Any:
        """SWOT Analysis API"""
        return await self._get(f"/equity/swot/{quote(str(identifier))}", params)
    async def upgrades(self, identifier: str, **params: Any) -> Any:
        """Analyst Upgrade/Downgrade History API"""
        return await self._get(f"/equity/upgrades/{quote(str(identifier))}", params)
    async def valuation_history(self, identifier: str, **params: Any) -> Any:
        """Valuation History API"""
        return await self._get(f"/equity/valuation-history/{quote(str(identifier))}", params)
    async def vendor_ratings(self, identifier: str, **params: Any) -> Any:
        """Vendor Analyst Ratings"""
        return await self._get(f"/equity/vendor-ratings/{quote(str(identifier))}", params)
