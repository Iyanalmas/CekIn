"""Simple image rendering helpers for Streamlit."""

from __future__ import annotations

from pathlib import Path

import streamlit as st


def show_image(path: Path, caption: str | None = None, use_column_width: bool = True):
	if not path.exists():
		st.info(f"Gambar belum tersedia: {path.name}")
		return
	width = "stretch" if use_column_width else "content"
	st.image(str(path), caption=caption, width=width)
