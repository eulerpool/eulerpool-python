from __future__ import annotations

from typing import Any, Union
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Calendar(SyncResource):
    def ipo(self) -> Any:
        return self._get("/calendar/ipo")

    def dividends(self, year: Union[int, str]) -> Any:
        return self._get(f"/calendar/dividends/{quote(str(year))}")

    def earnings(self, date: str) -> Any:
        return self._get(f"/calendar/earnings/{quote(date)}")

    def earnings_by_symbol(self, symbol: str) -> Any:
        return self._get(f"/calendar/earnings-by-symbol/{quote(symbol)}")

    def earnings_surprises(self, symbol: str) -> Any:
        return self._get(f"/calendar/earnings-surprises/{quote(symbol)}")


class AsyncCalendar(AsyncResource):
    async def ipo(self) -> Any:
        return await self._get("/calendar/ipo")

    async def dividends(self, year: Union[int, str]) -> Any:
        return await self._get(f"/calendar/dividends/{quote(str(year))}")

    async def earnings(self, date: str) -> Any:
        return await self._get(f"/calendar/earnings/{quote(date)}")

    async def earnings_by_symbol(self, symbol: str) -> Any:
        return await self._get(f"/calendar/earnings-by-symbol/{quote(symbol)}")

    async def earnings_surprises(self, symbol: str) -> Any:
        return await self._get(f"/calendar/earnings-surprises/{quote(symbol)}")
