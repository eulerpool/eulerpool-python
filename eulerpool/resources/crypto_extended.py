from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class CryptoExtended(SyncResource):
    def analysis(self, symbol: str, **params: Any) -> Any:
        """Crypto Analysis Summary API"""
        return self._get(f"/crypto-extended/analysis/{quote(str(symbol))}", params)
    def asset_platforms(self, **params: Any) -> Any:
        """Asset Platforms (Blockchains) API"""
        return self._get("/crypto-extended/asset-platforms", params)
    def bridge_volumes(self, **params: Any) -> Any:
        """Bridge Volumes API"""
        return self._get("/crypto-extended/bridge-volumes", params)
    def btc_exchange_rates(self, **params: Any) -> Any:
        """BTC Exchange Rates API"""
        return self._get("/crypto-extended/btc-exchange-rates", params)
    def candles(self, symbol: str, **params: Any) -> Any:
        """Crypto OHLCV Candles API"""
        return self._get(f"/crypto-extended/candles/{quote(str(symbol))}", params)
    def categories(self, **params: Any) -> Any:
        """Crypto Categories API"""
        return self._get("/crypto-extended/categories", params)
    def chain_tvl(self, **params: Any) -> Any:
        """Chain TVL API"""
        return self._get("/crypto-extended/chain-tvl", params)
    def coin_tickers(self, coinId: str, **params: Any) -> Any:
        """Coin Tickers API"""
        return self._get(f"/crypto-extended/coin-tickers/{quote(str(coinId))}", params)
    def defi(self, symbol: str, **params: Any) -> Any:
        """DeFi Protocol Stats API"""
        return self._get(f"/crypto-extended/defi/{quote(str(symbol))}", params)
    def defi_fees(self, **params: Any) -> Any:
        """DeFi Fees & Revenue API"""
        return self._get("/crypto-extended/defi-fees", params)
    def defi_protocols(self, **params: Any) -> Any:
        """DeFi Protocols List API"""
        return self._get("/crypto-extended/defi-protocols", params)
    def defi_yields(self, **params: Any) -> Any:
        """DeFi Yields API"""
        return self._get("/crypto-extended/defi-yields", params)
    def derivatives(self, symbol: str, **params: Any) -> Any:
        """Crypto Derivatives API"""
        return self._get(f"/crypto-extended/derivatives/{quote(str(symbol))}", params)
    def derivatives_exchanges(self, **params: Any) -> Any:
        """Derivatives Exchanges API"""
        return self._get("/crypto-extended/derivatives-exchanges", params)
    def derivatives_tickers(self, **params: Any) -> Any:
        """Derivatives Tickers API"""
        return self._get("/crypto-extended/derivatives-tickers", params)
    def dex_volumes(self, **params: Any) -> Any:
        """DEX Volumes API"""
        return self._get("/crypto-extended/dex-volumes", params)
    def exchange_listings(self, symbol: str, **params: Any) -> Any:
        """Exchange Listings for a Coin"""
        return self._get(f"/crypto-extended/exchange-listings/{quote(str(symbol))}", params)
    def exchange_tickers(self, exchangeId: str, **params: Any) -> Any:
        """Exchange Trading Pairs"""
        return self._get(f"/crypto-extended/exchange-tickers/{quote(str(exchangeId))}", params)
    def exchange_volume(self, exchangeId: str, **params: Any) -> Any:
        """Exchange Volume History API"""
        return self._get(f"/crypto-extended/exchange-volume/{quote(str(exchangeId))}", params)
    def exchanges(self, **params: Any) -> Any:
        """Crypto Exchanges Directory"""
        return self._get("/crypto-extended/exchanges", params)
    def faq(self, symbol: str, **params: Any) -> Any:
        """Crypto FAQ Content"""
        return self._get(f"/crypto-extended/faq/{quote(str(symbol))}", params)
    def fear_greed_history(self, **params: Any) -> Any:
        """Crypto Fear & Greed History API"""
        return self._get("/crypto-extended/fear-greed-history", params)
    def funding_rates(self, symbol: str, **params: Any) -> Any:
        """Crypto Funding Rates API"""
        return self._get(f"/crypto-extended/funding-rates/{quote(str(symbol))}", params)
    def global_(self, **params: Any) -> Any:
        """Global Crypto Market Data API"""
        return self._get("/crypto-extended/global", params)
    def intraday(self, symbol: str, **params: Any) -> Any:
        """Crypto Intraday Quotes API"""
        return self._get(f"/crypto-extended/intraday/{quote(str(symbol))}", params)
    def liquidations(self, symbol: str, **params: Any) -> Any:
        """Crypto Liquidation Events"""
        return self._get(f"/crypto-extended/liquidations/{quote(str(symbol))}", params)
    def market_overview(self, **params: Any) -> Any:
        """Crypto Market Overview API"""
        return self._get("/crypto-extended/market-overview", params)
    def newly_listed(self, **params: Any) -> Any:
        """Newly Listed Cryptocurrencies API"""
        return self._get("/crypto-extended/newly-listed", params)
    def news_feed(self, **params: Any) -> Any:
        """Crypto News Feed"""
        return self._get("/crypto-extended/news-feed", params)
    def onchain(self, symbol: str, **params: Any) -> Any:
        """On-Chain Metrics API"""
        return self._get(f"/crypto-extended/onchain/{quote(str(symbol))}", params)
    def open_interest(self, symbol: str, **params: Any) -> Any:
        """Crypto Open Interest API"""
        return self._get(f"/crypto-extended/open-interest/{quote(str(symbol))}", params)
    def public_treasury(self, **params: Any) -> Any:
        """Public Treasury Holdings API"""
        return self._get("/crypto-extended/public-treasury", params)
    def stablecoin_supply(self, **params: Any) -> Any:
        """Stablecoin Supply History API"""
        return self._get("/crypto-extended/stablecoin-supply", params)
    def stablecoins(self, **params: Any) -> Any:
        """Stablecoin Market Caps API"""
        return self._get("/crypto-extended/stablecoins", params)
    def supply_breakdown(self, symbol: str, **params: Any) -> Any:
        """Crypto Supply Breakdown"""
        return self._get(f"/crypto-extended/supply-breakdown/{quote(str(symbol))}", params)
    def symbol_map(self, **params: Any) -> Any:
        """Binance Symbol Map API"""
        return self._get("/crypto-extended/symbol-map", params)
    def top_coins(self, **params: Any) -> Any:
        """Top Cryptocurrencies API"""
        return self._get("/crypto-extended/top-coins", params)
    def top_movers(self, **params: Any) -> Any:
        """Crypto Top Movers API"""
        return self._get("/crypto-extended/top-movers", params)
    def trending(self, **params: Any) -> Any:
        """Trending Cryptocurrencies API"""
        return self._get("/crypto-extended/trending", params)


class AsyncCryptoExtended(AsyncResource):
    async def analysis(self, symbol: str, **params: Any) -> Any:
        """Crypto Analysis Summary API"""
        return await self._get(f"/crypto-extended/analysis/{quote(str(symbol))}", params)
    async def asset_platforms(self, **params: Any) -> Any:
        """Asset Platforms (Blockchains) API"""
        return await self._get("/crypto-extended/asset-platforms", params)
    async def bridge_volumes(self, **params: Any) -> Any:
        """Bridge Volumes API"""
        return await self._get("/crypto-extended/bridge-volumes", params)
    async def btc_exchange_rates(self, **params: Any) -> Any:
        """BTC Exchange Rates API"""
        return await self._get("/crypto-extended/btc-exchange-rates", params)
    async def candles(self, symbol: str, **params: Any) -> Any:
        """Crypto OHLCV Candles API"""
        return await self._get(f"/crypto-extended/candles/{quote(str(symbol))}", params)
    async def categories(self, **params: Any) -> Any:
        """Crypto Categories API"""
        return await self._get("/crypto-extended/categories", params)
    async def chain_tvl(self, **params: Any) -> Any:
        """Chain TVL API"""
        return await self._get("/crypto-extended/chain-tvl", params)
    async def coin_tickers(self, coinId: str, **params: Any) -> Any:
        """Coin Tickers API"""
        return await self._get(f"/crypto-extended/coin-tickers/{quote(str(coinId))}", params)
    async def defi(self, symbol: str, **params: Any) -> Any:
        """DeFi Protocol Stats API"""
        return await self._get(f"/crypto-extended/defi/{quote(str(symbol))}", params)
    async def defi_fees(self, **params: Any) -> Any:
        """DeFi Fees & Revenue API"""
        return await self._get("/crypto-extended/defi-fees", params)
    async def defi_protocols(self, **params: Any) -> Any:
        """DeFi Protocols List API"""
        return await self._get("/crypto-extended/defi-protocols", params)
    async def defi_yields(self, **params: Any) -> Any:
        """DeFi Yields API"""
        return await self._get("/crypto-extended/defi-yields", params)
    async def derivatives(self, symbol: str, **params: Any) -> Any:
        """Crypto Derivatives API"""
        return await self._get(f"/crypto-extended/derivatives/{quote(str(symbol))}", params)
    async def derivatives_exchanges(self, **params: Any) -> Any:
        """Derivatives Exchanges API"""
        return await self._get("/crypto-extended/derivatives-exchanges", params)
    async def derivatives_tickers(self, **params: Any) -> Any:
        """Derivatives Tickers API"""
        return await self._get("/crypto-extended/derivatives-tickers", params)
    async def dex_volumes(self, **params: Any) -> Any:
        """DEX Volumes API"""
        return await self._get("/crypto-extended/dex-volumes", params)
    async def exchange_listings(self, symbol: str, **params: Any) -> Any:
        """Exchange Listings for a Coin"""
        return await self._get(f"/crypto-extended/exchange-listings/{quote(str(symbol))}", params)
    async def exchange_tickers(self, exchangeId: str, **params: Any) -> Any:
        """Exchange Trading Pairs"""
        return await self._get(f"/crypto-extended/exchange-tickers/{quote(str(exchangeId))}", params)
    async def exchange_volume(self, exchangeId: str, **params: Any) -> Any:
        """Exchange Volume History API"""
        return await self._get(f"/crypto-extended/exchange-volume/{quote(str(exchangeId))}", params)
    async def exchanges(self, **params: Any) -> Any:
        """Crypto Exchanges Directory"""
        return await self._get("/crypto-extended/exchanges", params)
    async def faq(self, symbol: str, **params: Any) -> Any:
        """Crypto FAQ Content"""
        return await self._get(f"/crypto-extended/faq/{quote(str(symbol))}", params)
    async def fear_greed_history(self, **params: Any) -> Any:
        """Crypto Fear & Greed History API"""
        return await self._get("/crypto-extended/fear-greed-history", params)
    async def funding_rates(self, symbol: str, **params: Any) -> Any:
        """Crypto Funding Rates API"""
        return await self._get(f"/crypto-extended/funding-rates/{quote(str(symbol))}", params)
    async def global_(self, **params: Any) -> Any:
        """Global Crypto Market Data API"""
        return await self._get("/crypto-extended/global", params)
    async def intraday(self, symbol: str, **params: Any) -> Any:
        """Crypto Intraday Quotes API"""
        return await self._get(f"/crypto-extended/intraday/{quote(str(symbol))}", params)
    async def liquidations(self, symbol: str, **params: Any) -> Any:
        """Crypto Liquidation Events"""
        return await self._get(f"/crypto-extended/liquidations/{quote(str(symbol))}", params)
    async def market_overview(self, **params: Any) -> Any:
        """Crypto Market Overview API"""
        return await self._get("/crypto-extended/market-overview", params)
    async def newly_listed(self, **params: Any) -> Any:
        """Newly Listed Cryptocurrencies API"""
        return await self._get("/crypto-extended/newly-listed", params)
    async def news_feed(self, **params: Any) -> Any:
        """Crypto News Feed"""
        return await self._get("/crypto-extended/news-feed", params)
    async def onchain(self, symbol: str, **params: Any) -> Any:
        """On-Chain Metrics API"""
        return await self._get(f"/crypto-extended/onchain/{quote(str(symbol))}", params)
    async def open_interest(self, symbol: str, **params: Any) -> Any:
        """Crypto Open Interest API"""
        return await self._get(f"/crypto-extended/open-interest/{quote(str(symbol))}", params)
    async def public_treasury(self, **params: Any) -> Any:
        """Public Treasury Holdings API"""
        return await self._get("/crypto-extended/public-treasury", params)
    async def stablecoin_supply(self, **params: Any) -> Any:
        """Stablecoin Supply History API"""
        return await self._get("/crypto-extended/stablecoin-supply", params)
    async def stablecoins(self, **params: Any) -> Any:
        """Stablecoin Market Caps API"""
        return await self._get("/crypto-extended/stablecoins", params)
    async def supply_breakdown(self, symbol: str, **params: Any) -> Any:
        """Crypto Supply Breakdown"""
        return await self._get(f"/crypto-extended/supply-breakdown/{quote(str(symbol))}", params)
    async def symbol_map(self, **params: Any) -> Any:
        """Binance Symbol Map API"""
        return await self._get("/crypto-extended/symbol-map", params)
    async def top_coins(self, **params: Any) -> Any:
        """Top Cryptocurrencies API"""
        return await self._get("/crypto-extended/top-coins", params)
    async def top_movers(self, **params: Any) -> Any:
        """Crypto Top Movers API"""
        return await self._get("/crypto-extended/top-movers", params)
    async def trending(self, **params: Any) -> Any:
        """Trending Cryptocurrencies API"""
        return await self._get("/crypto-extended/trending", params)
