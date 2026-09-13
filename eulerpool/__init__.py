"""Eulerpool Financial Data API SDK for Python."""

from __future__ import annotations

import os
from typing import Any, Optional

from ._client import AsyncHttpClient, HttpClient
from ._version import __version__
from .errors import (
    AuthenticationError,
    BadRequestError,
    EulerpoolError,
    NotFoundError,
    RateLimitError,
    ServerError,
)
from .resources.aaq import Aaq, AsyncAaq
from .resources.alternative import Alternative, AsyncAlternative
from .resources.analytics import Analytics, AsyncAnalytics
from .resources.backtest import Backtest, AsyncBacktest
from .resources.bonds import Bonds, AsyncBonds
from .resources.calendar import Calendar, AsyncCalendar
from .resources.certificates import Certificates, AsyncCertificates
from .resources.charting import Charting, AsyncCharting
from .resources.commodity import Commodity, AsyncCommodity
from .resources.crypto import Crypto, AsyncCrypto
from .resources.crypto_extended import CryptoExtended, AsyncCryptoExtended
from .resources.data import Data, AsyncData
from .resources.datasets import Datasets, AsyncDatasets
from .resources.deals import Deals, AsyncDeals
from .resources.derivatives import Derivatives, AsyncDerivatives
from .resources.dex import Dex, AsyncDex
from .resources.earning_calls import EarningCalls, AsyncEarningCalls
from .resources.ecb import Ecb, AsyncEcb
from .resources.economic_forecasts import EconomicForecasts, AsyncEconomicForecasts
from .resources.energy import Energy, AsyncEnergy
from .resources.equity import Equity, AsyncEquity
from .resources.equity_extended import EquityExtended, AsyncEquityExtended
from .resources.etf import Etf, AsyncEtf
from .resources.fair_value import FairValue, AsyncFairValue
from .resources.fixed_income import FixedIncome, AsyncFixedIncome
from .resources.forex import Forex, AsyncForex
from .resources.fundamentals import Fundamentals, AsyncFundamentals
from .resources.funds import Funds, AsyncFunds
from .resources.government import Government, AsyncGovernment
from .resources.ice_swap import IceSwap, AsyncIceSwap
from .resources.index import Index, AsyncIndex
from .resources.institutional import Institutional, AsyncInstitutional
from .resources.interest_rates import InterestRates, AsyncInterestRates
from .resources.macro import Macro, AsyncMacro
from .resources.market import Market, AsyncMarket
from .resources.mutual_fund import MutualFund, AsyncMutualFund
from .resources.news import News, AsyncNews
from .resources.nft import Nft, AsyncNft
from .resources.partner import Partner, AsyncPartner
from .resources.patents import Patents, AsyncPatents
from .resources.peer_comparison import PeerComparison, AsyncPeerComparison
from .resources.portfolio import Portfolio, AsyncPortfolio
from .resources.portfolio_risk import PortfolioRisk, AsyncPortfolioRisk
from .resources.private_markets import PrivateMarkets, AsyncPrivateMarkets
from .resources.research import Research, AsyncResearch
from .resources.risk_models import RiskModels, AsyncRiskModels
from .resources.screener import Screener, AsyncScreener
from .resources.sentiment import Sentiment, AsyncSentiment
from .resources.shipping import Shipping, AsyncShipping
from .resources.singapore import Singapore, AsyncSingapore
from .resources.transcripts import Transcripts, AsyncTranscripts
from .resources.trends import Trends, AsyncTrends
from .resources.vendor import Vendor, AsyncVendor
from .stream import AsyncStream, Stream

__all__ = [
    "Eulerpool",
    "AsyncEulerpool",
    "EulerpoolError",
    "AuthenticationError",
    "NotFoundError",
    "RateLimitError",
    "BadRequestError",
    "ServerError",
    "__version__",
]


def _require_key(api_key: Optional[str]) -> str:
    key = api_key or os.environ.get("EULERPOOL_API_KEY")
    if not key:
        raise AuthenticationError(
            "Pass an API key or set the EULERPOOL_API_KEY environment variable. "
            "Get a free key at https://eulerpool.com/developers/register"
        )
    return key


class Eulerpool:
    """Synchronous client for the Eulerpool Financial Data API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        base_url: Optional[str] = None,
        use_auth_header: bool = False,
        max_retries: int = 2,
        timeout: float = 30.0,
    ) -> None:
        self._client = HttpClient(
            _require_key(api_key),
            base_url=base_url,
            use_auth_header=use_auth_header,
            max_retries=max_retries,
            timeout=timeout,
        )
        self.aaq = Aaq(self._client)
        self.alternative = Alternative(self._client)
        self.analytics = Analytics(self._client)
        self.backtest = Backtest(self._client)
        self.bonds = Bonds(self._client)
        self.calendar = Calendar(self._client)
        self.certificates = Certificates(self._client)
        self.charting = Charting(self._client)
        self.commodity = Commodity(self._client)
        self.crypto = Crypto(self._client)
        self.crypto_extended = CryptoExtended(self._client)
        self.data = Data(self._client)
        self.datasets = Datasets(self._client)
        self.deals = Deals(self._client)
        self.derivatives = Derivatives(self._client)
        self.dex = Dex(self._client)
        self.earning_calls = EarningCalls(self._client)
        self.ecb = Ecb(self._client)
        self.economic_forecasts = EconomicForecasts(self._client)
        self.energy = Energy(self._client)
        self.equity = Equity(self._client)
        self.equity_extended = EquityExtended(self._client)
        self.etf = Etf(self._client)
        self.fair_value = FairValue(self._client)
        self.fixed_income = FixedIncome(self._client)
        self.forex = Forex(self._client)
        self.fundamentals = Fundamentals(self._client)
        self.funds = Funds(self._client)
        self.government = Government(self._client)
        self.ice_swap = IceSwap(self._client)
        self.index = Index(self._client)
        self.institutional = Institutional(self._client)
        self.interest_rates = InterestRates(self._client)
        self.macro = Macro(self._client)
        self.market = Market(self._client)
        self.mutual_fund = MutualFund(self._client)
        self.news = News(self._client)
        self.nft = Nft(self._client)
        self.partner = Partner(self._client)
        self.patents = Patents(self._client)
        self.peer_comparison = PeerComparison(self._client)
        self.portfolio = Portfolio(self._client)
        self.portfolio_risk = PortfolioRisk(self._client)
        self.private_markets = PrivateMarkets(self._client)
        self.research = Research(self._client)
        self.risk_models = RiskModels(self._client)
        self.screener = Screener(self._client)
        self.sentiment = Sentiment(self._client)
        self.shipping = Shipping(self._client)
        self.singapore = Singapore(self._client)
        self.transcripts = Transcripts(self._client)
        self.trends = Trends(self._client)
        self.vendor = Vendor(self._client)
        self.aaqs = self.aaq
        self.stream = Stream(self._client)

    def get(self, path: str, **params: Any) -> Any:
        """Call any GET endpoint by path, e.g. client.get("/equity/profile/AAPL")."""
        if not path.startswith("/"):
            path = "/" + path
        return self._client.get(path, params or None)

    def post(self, path: str, body: Any = None, **params: Any) -> Any:
        if not path.startswith("/"):
            path = "/" + path
        return self._client.post(path, body, params or None)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "Eulerpool":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


class AsyncEulerpool:
    """Async client for the Eulerpool Financial Data API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        base_url: Optional[str] = None,
        use_auth_header: bool = False,
        max_retries: int = 2,
        timeout: float = 30.0,
    ) -> None:
        self._client = AsyncHttpClient(
            _require_key(api_key),
            base_url=base_url,
            use_auth_header=use_auth_header,
            max_retries=max_retries,
            timeout=timeout,
        )
        self.aaq = AsyncAaq(self._client)
        self.alternative = AsyncAlternative(self._client)
        self.analytics = AsyncAnalytics(self._client)
        self.backtest = AsyncBacktest(self._client)
        self.bonds = AsyncBonds(self._client)
        self.calendar = AsyncCalendar(self._client)
        self.certificates = AsyncCertificates(self._client)
        self.charting = AsyncCharting(self._client)
        self.commodity = AsyncCommodity(self._client)
        self.crypto = AsyncCrypto(self._client)
        self.crypto_extended = AsyncCryptoExtended(self._client)
        self.data = AsyncData(self._client)
        self.datasets = AsyncDatasets(self._client)
        self.deals = AsyncDeals(self._client)
        self.derivatives = AsyncDerivatives(self._client)
        self.dex = AsyncDex(self._client)
        self.earning_calls = AsyncEarningCalls(self._client)
        self.ecb = AsyncEcb(self._client)
        self.economic_forecasts = AsyncEconomicForecasts(self._client)
        self.energy = AsyncEnergy(self._client)
        self.equity = AsyncEquity(self._client)
        self.equity_extended = AsyncEquityExtended(self._client)
        self.etf = AsyncEtf(self._client)
        self.fair_value = AsyncFairValue(self._client)
        self.fixed_income = AsyncFixedIncome(self._client)
        self.forex = AsyncForex(self._client)
        self.fundamentals = AsyncFundamentals(self._client)
        self.funds = AsyncFunds(self._client)
        self.government = AsyncGovernment(self._client)
        self.ice_swap = AsyncIceSwap(self._client)
        self.index = AsyncIndex(self._client)
        self.institutional = AsyncInstitutional(self._client)
        self.interest_rates = AsyncInterestRates(self._client)
        self.macro = AsyncMacro(self._client)
        self.market = AsyncMarket(self._client)
        self.mutual_fund = AsyncMutualFund(self._client)
        self.news = AsyncNews(self._client)
        self.nft = AsyncNft(self._client)
        self.partner = AsyncPartner(self._client)
        self.patents = AsyncPatents(self._client)
        self.peer_comparison = AsyncPeerComparison(self._client)
        self.portfolio = AsyncPortfolio(self._client)
        self.portfolio_risk = AsyncPortfolioRisk(self._client)
        self.private_markets = AsyncPrivateMarkets(self._client)
        self.research = AsyncResearch(self._client)
        self.risk_models = AsyncRiskModels(self._client)
        self.screener = AsyncScreener(self._client)
        self.sentiment = AsyncSentiment(self._client)
        self.shipping = AsyncShipping(self._client)
        self.singapore = AsyncSingapore(self._client)
        self.transcripts = AsyncTranscripts(self._client)
        self.trends = AsyncTrends(self._client)
        self.vendor = AsyncVendor(self._client)
        self.aaqs = self.aaq
        self.stream = AsyncStream(self._client)

    async def get(self, path: str, **params: Any) -> Any:
        if not path.startswith("/"):
            path = "/" + path
        return await self._client.get(path, params or None)

    async def post(self, path: str, body: Any = None, **params: Any) -> Any:
        if not path.startswith("/"):
            path = "/" + path
        return await self._client.post(path, body, params or None)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AsyncEulerpool":
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.close()
