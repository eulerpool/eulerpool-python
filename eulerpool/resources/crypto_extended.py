from __future__ import annotations

from typing import Any
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class CryptoExtended(SyncResource):
    def top_coins(self) -> Any:
        return self._get("/crypto-extended/top-coins")

    def market_overview(self) -> Any:
        return self._get("/crypto-extended/market-overview")

    def analysis(self, symbol: str) -> Any:
        return self._get(f"/crypto-extended/analysis/{quote(symbol)}")

    def derivatives(self, symbol: str) -> Any:
        return self._get(f"/crypto-extended/derivatives/{quote(symbol)}")

    def onchain(self, symbol: str) -> Any:
        return self._get(f"/crypto-extended/onchain/{quote(symbol)}")

    def defi(self, symbol: str) -> Any:
        return self._get(f"/crypto-extended/defi/{quote(symbol)}")

    def defi_protocols(self) -> Any:
        return self._get("/crypto-extended/defi-protocols")

    def defi_yields(self) -> Any:
        return self._get("/crypto-extended/defi-yields")

    def dex_volumes(self) -> Any:
        return self._get("/crypto-extended/dex-volumes")

    def stablecoins(self) -> Any:
        return self._get("/crypto-extended/stablecoins")

    def fear_greed_history(self) -> Any:
        return self._get("/crypto-extended/fear-greed-history")

    def candles(self, symbol: str) -> Any:
        return self._get(f"/crypto-extended/candles/{quote(symbol)}")

    def chain_tvl(self) -> Any:
        return self._get("/crypto-extended/chain-tvl")

    def defi_fees(self) -> Any:
        return self._get("/crypto-extended/defi-fees")

    def stablecoin_supply(self) -> Any:
        return self._get("/crypto-extended/stablecoin-supply")

    def bridge_volumes(self) -> Any:
        return self._get("/crypto-extended/bridge-volumes")

    def funding_rates(self, symbol: str) -> Any:
        return self._get(f"/crypto-extended/funding-rates/{quote(symbol)}")

    def open_interest(self, symbol: str) -> Any:
        return self._get(f"/crypto-extended/open-interest/{quote(symbol)}")

    def intraday(self, symbol: str) -> Any:
        return self._get(f"/crypto-extended/intraday/{quote(symbol)}")

    def symbol_map(self) -> Any:
        return self._get("/crypto-extended/symbol-map")


class AsyncCryptoExtended(AsyncResource):
    async def top_coins(self) -> Any:
        return await self._get("/crypto-extended/top-coins")

    async def market_overview(self) -> Any:
        return await self._get("/crypto-extended/market-overview")

    async def analysis(self, symbol: str) -> Any:
        return await self._get(f"/crypto-extended/analysis/{quote(symbol)}")

    async def derivatives(self, symbol: str) -> Any:
        return await self._get(f"/crypto-extended/derivatives/{quote(symbol)}")

    async def onchain(self, symbol: str) -> Any:
        return await self._get(f"/crypto-extended/onchain/{quote(symbol)}")

    async def defi(self, symbol: str) -> Any:
        return await self._get(f"/crypto-extended/defi/{quote(symbol)}")

    async def defi_protocols(self) -> Any:
        return await self._get("/crypto-extended/defi-protocols")

    async def defi_yields(self) -> Any:
        return await self._get("/crypto-extended/defi-yields")

    async def dex_volumes(self) -> Any:
        return await self._get("/crypto-extended/dex-volumes")

    async def stablecoins(self) -> Any:
        return await self._get("/crypto-extended/stablecoins")

    async def fear_greed_history(self) -> Any:
        return await self._get("/crypto-extended/fear-greed-history")

    async def candles(self, symbol: str) -> Any:
        return await self._get(f"/crypto-extended/candles/{quote(symbol)}")

    async def chain_tvl(self) -> Any:
        return await self._get("/crypto-extended/chain-tvl")

    async def defi_fees(self) -> Any:
        return await self._get("/crypto-extended/defi-fees")

    async def stablecoin_supply(self) -> Any:
        return await self._get("/crypto-extended/stablecoin-supply")

    async def bridge_volumes(self) -> Any:
        return await self._get("/crypto-extended/bridge-volumes")

    async def funding_rates(self, symbol: str) -> Any:
        return await self._get(f"/crypto-extended/funding-rates/{quote(symbol)}")

    async def open_interest(self, symbol: str) -> Any:
        return await self._get(f"/crypto-extended/open-interest/{quote(symbol)}")

    async def intraday(self, symbol: str) -> Any:
        return await self._get(f"/crypto-extended/intraday/{quote(symbol)}")

    async def symbol_map(self) -> Any:
        return await self._get("/crypto-extended/symbol-map")
