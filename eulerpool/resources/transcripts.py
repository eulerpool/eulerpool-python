from __future__ import annotations

from typing import Any, Optional
from urllib.parse import quote

from ._base import AsyncResource, SyncResource


class Transcripts(SyncResource):
    def calls(self, identifier: str, callId: Optional[str] = None, **params: Any) -> Any:
        """Full Transcript"""
        if callId is not None:
            return self._get(f"/transcripts/calls/{quote(str(identifier))}/{quote(str(callId))}", params)
        return self._get(f"/transcripts/calls/{quote(str(identifier))}", params)
    def calls_nlp(self, identifier: str, callId: str, **params: Any) -> Any:
        """Transcript NLP Analysis"""
        return self._get(f"/transcripts/calls/{quote(str(identifier))}/{quote(str(callId))}/nlp", params)
    def search(self, **params: Any) -> Any:
        """Search Transcripts"""
        return self._get("/transcripts/search", params)
    def sentiment_trend(self, identifier: str, **params: Any) -> Any:
        """Sentiment Trend"""
        return self._get(f"/transcripts/sentiment-trend/{quote(str(identifier))}", params)


class AsyncTranscripts(AsyncResource):
    async def calls(self, identifier: str, callId: Optional[str] = None, **params: Any) -> Any:
        """Full Transcript"""
        if callId is not None:
            return await self._get(f"/transcripts/calls/{quote(str(identifier))}/{quote(str(callId))}", params)
        return await self._get(f"/transcripts/calls/{quote(str(identifier))}", params)
    async def calls_nlp(self, identifier: str, callId: str, **params: Any) -> Any:
        """Transcript NLP Analysis"""
        return await self._get(f"/transcripts/calls/{quote(str(identifier))}/{quote(str(callId))}/nlp", params)
    async def search(self, **params: Any) -> Any:
        """Search Transcripts"""
        return await self._get("/transcripts/search", params)
    async def sentiment_trend(self, identifier: str, **params: Any) -> Any:
        """Sentiment Trend"""
        return await self._get(f"/transcripts/sentiment-trend/{quote(str(identifier))}", params)
