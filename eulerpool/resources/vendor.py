from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Vendor(SyncResource):
    def catalog(self, **params: Any) -> Any:
        """Vendor Warehouse Catalog"""
        return self._get("/vendor/catalog", params)
    def get(self, vendor: str, dataset: str, key: Optional[str] = None, **params: Any) -> Any:
        """Vendor Keyed Snapshot"""
        if key is not None:
            return self._get(f"/vendor/{quote(str(vendor))}/{quote(str(dataset))}/{quote(str(key))}", params)
        return self._get(f"/vendor/{quote(str(vendor))}/{quote(str(dataset))}", params)


class AsyncVendor(AsyncResource):
    async def catalog(self, **params: Any) -> Any:
        """Vendor Warehouse Catalog"""
        return await self._get("/vendor/catalog", params)
    async def get(self, vendor: str, dataset: str, key: Optional[str] = None, **params: Any) -> Any:
        """Vendor Keyed Snapshot"""
        if key is not None:
            return await self._get(f"/vendor/{quote(str(vendor))}/{quote(str(dataset))}/{quote(str(key))}", params)
        return await self._get(f"/vendor/{quote(str(vendor))}/{quote(str(dataset))}", params)
