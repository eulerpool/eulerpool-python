from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Portfolio(SyncResource):
    def delete_portfolios(self, id: str, **params: Any) -> Any:
        """Delete portfolio"""
        return self._delete(f"/portfolio/portfolios/{quote(str(id))}", params)
    def portfolios(self, **params: Any) -> Any:
        """List portfolios"""
        return self._get("/portfolio/portfolios", params)
    def portfolios_alerts(self, id: str, **params: Any) -> Any:
        """Portfolio alerts"""
        return self._get(f"/portfolio/portfolios/{quote(str(id))}/alerts", params)
    def portfolios_alerts_id(self, id: str, body: Any = None, **params: Any) -> Any:
        """Create alert"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post(f"/portfolio/portfolios/{quote(str(id))}/alerts", body, params)
    def portfolios_alt(self, body: Any = None, **params: Any) -> Any:
        """Create portfolio"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/portfolio/portfolios", body, params)
    def portfolios_analytics(self, id: str, **params: Any) -> Any:
        """Portfolio analytics"""
        return self._get(f"/portfolio/portfolios/{quote(str(id))}/analytics", params)
    def portfolios_positions(self, id: str, **params: Any) -> Any:
        """Portfolio positions"""
        return self._get(f"/portfolio/portfolios/{quote(str(id))}/positions", params)
    def portfolios_transactions(self, id: str, body: Any = None, **params: Any) -> Any:
        """Add transaction"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post(f"/portfolio/portfolios/{quote(str(id))}/transactions", body, params)
    def portfolios_valuations(self, id: str, **params: Any) -> Any:
        """Portfolio daily valuations"""
        return self._get(f"/portfolio/portfolios/{quote(str(id))}/valuations", params)


class AsyncPortfolio(AsyncResource):
    async def delete_portfolios(self, id: str, **params: Any) -> Any:
        """Delete portfolio"""
        return await self._delete(f"/portfolio/portfolios/{quote(str(id))}", params)
    async def portfolios(self, **params: Any) -> Any:
        """List portfolios"""
        return await self._get("/portfolio/portfolios", params)
    async def portfolios_alerts(self, id: str, **params: Any) -> Any:
        """Portfolio alerts"""
        return await self._get(f"/portfolio/portfolios/{quote(str(id))}/alerts", params)
    async def portfolios_alerts_id(self, id: str, body: Any = None, **params: Any) -> Any:
        """Create alert"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post(f"/portfolio/portfolios/{quote(str(id))}/alerts", body, params)
    async def portfolios_alt(self, body: Any = None, **params: Any) -> Any:
        """Create portfolio"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/portfolio/portfolios", body, params)
    async def portfolios_analytics(self, id: str, **params: Any) -> Any:
        """Portfolio analytics"""
        return await self._get(f"/portfolio/portfolios/{quote(str(id))}/analytics", params)
    async def portfolios_positions(self, id: str, **params: Any) -> Any:
        """Portfolio positions"""
        return await self._get(f"/portfolio/portfolios/{quote(str(id))}/positions", params)
    async def portfolios_transactions(self, id: str, body: Any = None, **params: Any) -> Any:
        """Add transaction"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post(f"/portfolio/portfolios/{quote(str(id))}/transactions", body, params)
    async def portfolios_valuations(self, id: str, **params: Any) -> Any:
        """Portfolio daily valuations"""
        return await self._get(f"/portfolio/portfolios/{quote(str(id))}/valuations", params)
