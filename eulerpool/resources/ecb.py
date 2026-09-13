from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Ecb(SyncResource):
    def exchange_rates(self, currency: Optional[str] = None, **params: Any) -> Any:
        """ECB exchange rate history"""
        if currency is not None:
            return self._get(f"/ecb/exchange-rates/{quote(str(currency))}", params)
        return self._get("/ecb/exchange-rates", params)
    def key_rates(self, **params: Any) -> Any:
        """ECB key interest rates"""
        return self._get("/ecb/key-rates", params)
    def yield_curves(self, **params: Any) -> Any:
        """ECB euro area yield curves"""
        return self._get("/ecb/yield-curves", params)


class AsyncEcb(AsyncResource):
    async def exchange_rates(self, currency: Optional[str] = None, **params: Any) -> Any:
        """ECB exchange rate history"""
        if currency is not None:
            return await self._get(f"/ecb/exchange-rates/{quote(str(currency))}", params)
        return await self._get("/ecb/exchange-rates", params)
    async def key_rates(self, **params: Any) -> Any:
        """ECB key interest rates"""
        return await self._get("/ecb/key-rates", params)
    async def yield_curves(self, **params: Any) -> Any:
        """ECB euro area yield curves"""
        return await self._get("/ecb/yield-curves", params)
