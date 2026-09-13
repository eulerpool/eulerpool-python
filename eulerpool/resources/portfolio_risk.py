from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class PortfolioRisk(SyncResource):
    def attribution(self, portfolioId: str, **params: Any) -> Any:
        """Brinson Attribution"""
        return self._get(f"/portfolio-risk/attribution/{quote(str(portfolioId))}", params)
    def correlation(self, portfolioId: str, **params: Any) -> Any:
        """Correlation Matrix"""
        return self._get(f"/portfolio-risk/correlation/{quote(str(portfolioId))}", params)
    def risk_metrics(self, portfolioId: str, **params: Any) -> Any:
        """Risk Metrics"""
        return self._get(f"/portfolio-risk/risk-metrics/{quote(str(portfolioId))}", params)
    def stress_test(self, portfolioId: str, body: Any = None, **params: Any) -> Any:
        """Stress Test"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post(f"/portfolio-risk/stress-test/{quote(str(portfolioId))}", body, params)
    def tracking(self, portfolioId: str, **params: Any) -> Any:
        """Tracking Error"""
        return self._get(f"/portfolio-risk/tracking/{quote(str(portfolioId))}", params)
    def var(self, portfolioId: str, **params: Any) -> Any:
        """Value at Risk"""
        return self._get(f"/portfolio-risk/var/{quote(str(portfolioId))}", params)


class AsyncPortfolioRisk(AsyncResource):
    async def attribution(self, portfolioId: str, **params: Any) -> Any:
        """Brinson Attribution"""
        return await self._get(f"/portfolio-risk/attribution/{quote(str(portfolioId))}", params)
    async def correlation(self, portfolioId: str, **params: Any) -> Any:
        """Correlation Matrix"""
        return await self._get(f"/portfolio-risk/correlation/{quote(str(portfolioId))}", params)
    async def risk_metrics(self, portfolioId: str, **params: Any) -> Any:
        """Risk Metrics"""
        return await self._get(f"/portfolio-risk/risk-metrics/{quote(str(portfolioId))}", params)
    async def stress_test(self, portfolioId: str, body: Any = None, **params: Any) -> Any:
        """Stress Test"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post(f"/portfolio-risk/stress-test/{quote(str(portfolioId))}", body, params)
    async def tracking(self, portfolioId: str, **params: Any) -> Any:
        """Tracking Error"""
        return await self._get(f"/portfolio-risk/tracking/{quote(str(portfolioId))}", params)
    async def var(self, portfolioId: str, **params: Any) -> Any:
        """Value at Risk"""
        return await self._get(f"/portfolio-risk/var/{quote(str(portfolioId))}", params)
