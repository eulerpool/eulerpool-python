from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Backtest(SyncResource):
    def optimize(self, body: Any = None, **params: Any) -> Any:
        """Optimize Strategy"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/backtest/optimize", body, params)
    def run(self, body: Any = None, **params: Any) -> Any:
        """Run Backtest"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/backtest/run", body, params)
    def templates(self, **params: Any) -> Any:
        """Strategy Templates"""
        return self._get("/backtest/templates", params)
    def walk_forward(self, body: Any = None, **params: Any) -> Any:
        """Walk-Forward Analysis"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return self._post("/backtest/walk-forward", body, params)


class AsyncBacktest(AsyncResource):
    async def optimize(self, body: Any = None, **params: Any) -> Any:
        """Optimize Strategy"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/backtest/optimize", body, params)
    async def run(self, body: Any = None, **params: Any) -> Any:
        """Run Backtest"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/backtest/run", body, params)
    async def templates(self, **params: Any) -> Any:
        """Strategy Templates"""
        return await self._get("/backtest/templates", params)
    async def walk_forward(self, body: Any = None, **params: Any) -> Any:
        """Walk-Forward Analysis"""
        if body is None and params:
            body, params = params, None
        elif isinstance(body, dict) and params:
            body = {**body, **params}
            params = None
        return await self._post("/backtest/walk-forward", body, params)
