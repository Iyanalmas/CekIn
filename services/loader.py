"""Cached artifact loading helpers."""

from __future__ import annotations

import pickle
from pathlib import Path

import streamlit as st

from config import MODELS, TFIDF_PATH


def _load_pickle(path: Path):
	if not path.exists():
		raise FileNotFoundError(f"File tidak ditemukan: {path}")
	with path.open("rb") as file_handle:
		return pickle.load(file_handle)


@st.cache_resource(show_spinner=False)
def load_tfidf_vectorizer():
	return _load_pickle(TFIDF_PATH)


@st.cache_resource(show_spinner=False)
def load_model(kernel: str):
	kernel_key = kernel.lower()
	if kernel_key not in MODELS:
		raise KeyError(f"Kernel tidak dikenal: {kernel}")
	return _load_pickle(MODELS[kernel_key])


@st.cache_resource(show_spinner=False)
def load_artifacts(kernel: str):
	return {
		"model": load_model(kernel),
		"tfidf": load_tfidf_vectorizer(),
	}
