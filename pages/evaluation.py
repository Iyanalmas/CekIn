"""Evaluation page for a single kernel."""

from __future__ import annotations

import csv

import streamlit as st

from config import EVALUATION_FILES, KERNEL_LABELS


def _read_single_row_csv(path):
	if not path.exists():
		return []
	with path.open("r", encoding="utf-8-sig", newline="") as file_handle:
		return list(csv.DictReader(file_handle))


def show():
	st.title("Evaluasi Per Kernel")
	kernel = st.selectbox("Pilih kernel", list(KERNEL_LABELS.keys()), format_func=lambda key: KERNEL_LABELS[key])

	rows = _read_single_row_csv(EVALUATION_FILES[kernel])
	if rows:
		st.dataframe(rows, width="stretch")
	else:
		st.info("Data evaluasi belum tersedia.")

	st.caption("Confusion matrix ditampilkan jika file gambar tersedia di folder assets atau output.")
