from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class PeerComparison(SyncResource):
    def compare(self, body: Any = None, **params: Any) -> Any:
        """Compare Companies"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/peer-comparison/compare", body, params)
    def financial_benchmarking(self, identifier: str, **params: Any) -> Any:
        """Financial Benchmarking"""
        return self._get(f"/peer-comparison/financial-benchmarking/{quote(str(identifier))}", params)
    def metrics(self, **params: Any) -> Any:
        """Available Metrics"""
        return self._get("/peer-comparison/metrics", params)
    def peers(self, identifier: str, **params: Any) -> Any:
        """Auto-Detect Peers"""
        return self._get(f"/peer-comparison/peers/{quote(str(identifier))}", params)
    def relative_valuation(self, identifier: str, **params: Any) -> Any:
        """Relative Valuation"""
        return self._get(f"/peer-comparison/relative-valuation/{quote(str(identifier))}", params)
    def scatter(self, **params: Any) -> Any:
        """Scatter Plot Data"""
        return self._get("/peer-comparison/scatter", params)


class AsyncPeerComparison(AsyncResource):
    async def compare(self, body: Any = None, **params: Any) -> Any:
        """Compare Companies"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/peer-comparison/compare", body, params)
    async def financial_benchmarking(self, identifier: str, **params: Any) -> Any:
        """Financial Benchmarking"""
        return await self._get(f"/peer-comparison/financial-benchmarking/{quote(str(identifier))}", params)
    async def metrics(self, **params: Any) -> Any:
        """Available Metrics"""
        return await self._get("/peer-comparison/metrics", params)
    async def peers(self, identifier: str, **params: Any) -> Any:
        """Auto-Detect Peers"""
        return await self._get(f"/peer-comparison/peers/{quote(str(identifier))}", params)
    async def relative_valuation(self, identifier: str, **params: Any) -> Any:
        """Relative Valuation"""
        return await self._get(f"/peer-comparison/relative-valuation/{quote(str(identifier))}", params)
    async def scatter(self, **params: Any) -> Any:
        """Scatter Plot Data"""
        return await self._get("/peer-comparison/scatter", params)
