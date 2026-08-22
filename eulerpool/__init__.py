"""Eulerpool Financial Data API SDK for Python."""

from __future__ import annotations

from typing import Optional

from ._client import AsyncHttpClient, HttpClient
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
from .resources.bonds import AsyncBonds, Bonds
from .resources.calendar import AsyncCalendar, Calendar
from .resources.certificates import AsyncCertificates, Certificates
from .resources.commodity import AsyncCommodity, Commodity
from .resources.crypto import AsyncCrypto, Crypto
from .resources.crypto_extended import AsyncCryptoExtended, CryptoExtended
from .resources.earning_calls import AsyncEarningCalls, EarningCalls
from .resources.equity import AsyncEquity, Equity
from .resources.equity_extended import AsyncEquityExtended, EquityExtended
from .resources.etf import AsyncEtf, Etf
from .resources.fair_value import AsyncFairValue, FairValue
from .resources.forex import AsyncForex, Forex
from .resources.ice_swap import AsyncIceSwap, IceSwap
from .resources.index import AsyncIndex, Index
from .resources.institutional import AsyncInstitutional, Institutional
from .resources.macro import AsyncMacro, Macro
from .resources.market import AsyncMarket, Market
from .resources.mutual_fund import AsyncMutualFund, MutualFund
from .resources.news import AsyncNews, News
from .resources.research import AsyncResearch, Research
from .resources.screener import AsyncScreener, Screener
from .resources.sentiment import AsyncSentiment, Sentiment
from .resources.trends import AsyncTrends, Trends

__all__ = [
    "Eulerpool",
    "AsyncEulerpool",
    "EulerpoolError",
    "AuthenticationError",
    "NotFoundError",
    "RateLimitError",
    "BadRequestError",
    "ServerError",
]


class Eulerpool:
    """Synchronous client for the Eulerpool Financial Data API."""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        use_auth_header: bool = False,
        max_retries: int = 2,
        timeout: float = 30.0,
    ) -> None:
        self._client = HttpClient(
            api_key,
            base_url=base_url,
            use_auth_header=use_auth_header,
            max_retries=max_retries,
            timeout=timeout,
        )
        self.equity = Equity(self._client)
        self.equity_extended = EquityExtended(self._client)
        self.etf = Etf(self._client)
        self.macro = Macro(self._client)
        self.forex = Forex(self._client)
        self.bonds = Bonds(self._client)
        self.crypto = Crypto(self._client)
        self.crypto_extended = CryptoExtended(self._client)
        self.market = Market(self._client)
        self.alternative = Alternative(self._client)
        self.sentiment = Sentiment(self._client)
        self.research = Research(self._client)
        self.calendar = Calendar(self._client)
        self.screener = Screener(self._client)
        self.mutual_fund = MutualFund(self._client)
        self.commodity = Commodity(self._client)
        self.institutional = Institutional(self._client)
        self.certificates = Certificates(self._client)
        self.earning_calls = EarningCalls(self._client)
        self.index = Index(self._client)
        self.news = News(self._client)
        self.trends = Trends(self._client)
        self.ice_swap = IceSwap(self._client)
        self.fair_value = FairValue(self._client)
        self.aaq = Aaq(self._client)

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
        api_key: str,
        *,
        base_url: Optional[str] = None,
        use_auth_header: bool = False,
        max_retries: int = 2,
        timeout: float = 30.0,
    ) -> None:
        self._client = AsyncHttpClient(
            api_key,
            base_url=base_url,
            use_auth_header=use_auth_header,
            max_retries=max_retries,
            timeout=timeout,
        )
        self.equity = AsyncEquity(self._client)
        self.equity_extended = AsyncEquityExtended(self._client)
        self.etf = AsyncEtf(self._client)
        self.macro = AsyncMacro(self._client)
        self.forex = AsyncForex(self._client)
        self.bonds = AsyncBonds(self._client)
        self.crypto = AsyncCrypto(self._client)
        self.crypto_extended = AsyncCryptoExtended(self._client)
        self.market = AsyncMarket(self._client)
        self.alternative = AsyncAlternative(self._client)
        self.sentiment = AsyncSentiment(self._client)
        self.research = AsyncResearch(self._client)
        self.calendar = AsyncCalendar(self._client)
        self.screener = AsyncScreener(self._client)
        self.mutual_fund = AsyncMutualFund(self._client)
        self.commodity = AsyncCommodity(self._client)
        self.institutional = AsyncInstitutional(self._client)
        self.certificates = AsyncCertificates(self._client)
        self.earning_calls = AsyncEarningCalls(self._client)
        self.index = AsyncIndex(self._client)
        self.news = AsyncNews(self._client)
        self.trends = AsyncTrends(self._client)
        self.ice_swap = AsyncIceSwap(self._client)
        self.fair_value = AsyncFairValue(self._client)
        self.aaq = AsyncAaq(self._client)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AsyncEulerpool":
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.close()
