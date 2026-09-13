from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Energy(SyncResource):
    def coal_quarterly(self, **params: Any) -> Any:
        """Coal Quarterly"""
        return self._get("/energy/coal/quarterly", params)
    def electricity_monthly(self, **params: Any) -> Any:
        """Electricity Monthly"""
        return self._get("/energy/electricity/monthly", params)
    def energy_latest(self, **params: Any) -> Any:
        """Latest Energy Data"""
        return self._get("/energy/energy/latest", params)
    def jodi(self, **params: Any) -> Any:
        """JODI Oil & Gas Flows"""
        return self._get("/energy/jodi", params)
    def natural_gas_weekly(self, **params: Any) -> Any:
        """Natural Gas Weekly"""
        return self._get("/energy/natural-gas/weekly", params)
    def petroleum_weekly(self, **params: Any) -> Any:
        """Petroleum Weekly"""
        return self._get("/energy/petroleum/weekly", params)
    def pipelines(self, id: Optional[str] = None, **params: Any) -> Any:
        """Pipeline Details"""
        if id is not None:
            return self._get(f"/energy/pipelines/{quote(str(id))}", params)
        return self._get("/energy/pipelines/", params)
    def pipelines_flows(self, id: str, **params: Any) -> Any:
        """Pipeline Flows"""
        return self._get(f"/energy/pipelines/{quote(str(id))}/flows", params)
    def pipelines_flows_latest(self, **params: Any) -> Any:
        """Latest Pipeline Flows"""
        return self._get("/energy/pipelines/flows/latest", params)
    def storage_facilities(self, **params: Any) -> Any:
        """Storage Facilities"""
        return self._get("/energy/storage/facilities", params)
    def storage_facilities_levels(self, id: str, **params: Any) -> Any:
        """Facility Storage Levels"""
        return self._get(f"/energy/storage/facilities/{quote(str(id))}/levels", params)
    def storage_latest(self, **params: Any) -> Any:
        """Latest Storage Levels"""
        return self._get("/energy/storage/latest", params)
    def storage_summary(self, **params: Any) -> Any:
        """Storage Summary"""
        return self._get("/energy/storage/summary", params)


class AsyncEnergy(AsyncResource):
    async def coal_quarterly(self, **params: Any) -> Any:
        """Coal Quarterly"""
        return await self._get("/energy/coal/quarterly", params)
    async def electricity_monthly(self, **params: Any) -> Any:
        """Electricity Monthly"""
        return await self._get("/energy/electricity/monthly", params)
    async def energy_latest(self, **params: Any) -> Any:
        """Latest Energy Data"""
        return await self._get("/energy/energy/latest", params)
    async def jodi(self, **params: Any) -> Any:
        """JODI Oil & Gas Flows"""
        return await self._get("/energy/jodi", params)
    async def natural_gas_weekly(self, **params: Any) -> Any:
        """Natural Gas Weekly"""
        return await self._get("/energy/natural-gas/weekly", params)
    async def petroleum_weekly(self, **params: Any) -> Any:
        """Petroleum Weekly"""
        return await self._get("/energy/petroleum/weekly", params)
    async def pipelines(self, id: Optional[str] = None, **params: Any) -> Any:
        """Pipeline Details"""
        if id is not None:
            return await self._get(f"/energy/pipelines/{quote(str(id))}", params)
        return await self._get("/energy/pipelines/", params)
    async def pipelines_flows(self, id: str, **params: Any) -> Any:
        """Pipeline Flows"""
        return await self._get(f"/energy/pipelines/{quote(str(id))}/flows", params)
    async def pipelines_flows_latest(self, **params: Any) -> Any:
        """Latest Pipeline Flows"""
        return await self._get("/energy/pipelines/flows/latest", params)
    async def storage_facilities(self, **params: Any) -> Any:
        """Storage Facilities"""
        return await self._get("/energy/storage/facilities", params)
    async def storage_facilities_levels(self, id: str, **params: Any) -> Any:
        """Facility Storage Levels"""
        return await self._get(f"/energy/storage/facilities/{quote(str(id))}/levels", params)
    async def storage_latest(self, **params: Any) -> Any:
        """Latest Storage Levels"""
        return await self._get("/energy/storage/latest", params)
    async def storage_summary(self, **params: Any) -> Any:
        """Storage Summary"""
        return await self._get("/energy/storage/summary", params)
