from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Fundamentals(SyncResource):
    def annual_report(self, identifier: str, **params: Any) -> Any:
        """Annual Report JSON (10-K)"""
        return self._get(f"/fundamentals/annual-report/{quote(str(identifier))}", params)
    def company(self, identifier: str, **params: Any) -> Any:
        """SEC Company Info"""
        return self._get(f"/fundamentals/company/{quote(str(identifier))}", params)
    def facts_search(self, **params: Any) -> Any:
        """XBRL Tag Search"""
        return self._get("/fundamentals/facts/search", params)
    def financials(self, identifier: str, **params: Any) -> Any:
        """XBRL Financial Facts"""
        return self._get(f"/fundamentals/financials/{quote(str(identifier))}", params)
    def financials_balance_sheet(self, identifier: str, **params: Any) -> Any:
        """Balance Sheet"""
        return self._get(f"/fundamentals/financials/{quote(str(identifier))}/balance-sheet", params)
    def financials_cash_flow(self, identifier: str, **params: Any) -> Any:
        """Cash Flow Statement"""
        return self._get(f"/fundamentals/financials/{quote(str(identifier))}/cash-flow", params)
    def financials_income_statement(self, identifier: str, **params: Any) -> Any:
        """Income Statement"""
        return self._get(f"/fundamentals/financials/{quote(str(identifier))}/income-statement", params)
    def financials_ratios(self, identifier: str, **params: Any) -> Any:
        """Financial Ratios"""
        return self._get(f"/fundamentals/financials/{quote(str(identifier))}/ratios", params)


class AsyncFundamentals(AsyncResource):
    async def annual_report(self, identifier: str, **params: Any) -> Any:
        """Annual Report JSON (10-K)"""
        return await self._get(f"/fundamentals/annual-report/{quote(str(identifier))}", params)
    async def company(self, identifier: str, **params: Any) -> Any:
        """SEC Company Info"""
        return await self._get(f"/fundamentals/company/{quote(str(identifier))}", params)
    async def facts_search(self, **params: Any) -> Any:
        """XBRL Tag Search"""
        return await self._get("/fundamentals/facts/search", params)
    async def financials(self, identifier: str, **params: Any) -> Any:
        """XBRL Financial Facts"""
        return await self._get(f"/fundamentals/financials/{quote(str(identifier))}", params)
    async def financials_balance_sheet(self, identifier: str, **params: Any) -> Any:
        """Balance Sheet"""
        return await self._get(f"/fundamentals/financials/{quote(str(identifier))}/balance-sheet", params)
    async def financials_cash_flow(self, identifier: str, **params: Any) -> Any:
        """Cash Flow Statement"""
        return await self._get(f"/fundamentals/financials/{quote(str(identifier))}/cash-flow", params)
    async def financials_income_statement(self, identifier: str, **params: Any) -> Any:
        """Income Statement"""
        return await self._get(f"/fundamentals/financials/{quote(str(identifier))}/income-statement", params)
    async def financials_ratios(self, identifier: str, **params: Any) -> Any:
        """Financial Ratios"""
        return await self._get(f"/fundamentals/financials/{quote(str(identifier))}/ratios", params)
