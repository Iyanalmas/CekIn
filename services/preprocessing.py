"""Text preprocessing pipeline."""

from __future__ import annotations

import re
from functools import lru_cache

try:
	from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
	from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
except ImportError:  # pragma: no cover - optional dependency fallback
	StemmerFactory = None
	StopWordRemoverFactory = None


URL_PATTERN = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
NON_ALPHA_PATTERN = re.compile(r"[^a-zA-Z\s]")
MULTISPACE_PATTERN = re.compile(r"\s+")


@lru_cache(maxsize=1)
def _get_stopwords():
	if StopWordRemoverFactory is None:
		return set()
	return set(StopWordRemoverFactory().get_stop_words())


@lru_cache(maxsize=1)
def _get_stemmer():
	if StemmerFactory is None:
		return None
	return StemmerFactory().create_stemmer()


def case_folding(text: str) -> str:
	return text.lower().strip()


def clean_text(text: str) -> str:
	text = URL_PATTERN.sub(" ", text)
	text = text.replace("\n", " ").replace("\r", " ")
	text = NON_ALPHA_PATTERN.sub(" ", text)
	return MULTISPACE_PATTERN.sub(" ", text).strip()


def tokenize(text: str) -> list[str]:
	return [token for token in text.split(" ") if token]


def remove_stopwords(tokens: list[str]) -> list[str]:
	stopwords = _get_stopwords()
	if not stopwords:
		return tokens
	return [token for token in tokens if token not in stopwords]


def stem_tokens(tokens: list[str]) -> list[str]:
	stemmer = _get_stemmer()
	if stemmer is None:
		return tokens
	return [stemmer.stem(token) for token in tokens]


def preprocess_text(text: str | None) -> str:
	if not text:
		return ""

	cleaned = clean_text(case_folding(text))
	tokens = tokenize(cleaned)
	tokens = remove_stopwords(tokens)
	tokens = stem_tokens(tokens)
	return " ".join(tokens).strip()
