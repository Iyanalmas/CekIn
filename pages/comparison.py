"""Comparison page for all kernels."""

from __future__ import annotations

import csv

import streamlit as st

from config import EVALUATION_FILES, KERNEL_LABELS, KERNEL_ORDER


def _read_rows(path):
	if not path.exists():
		return []
	with path.open("r", encoding="utf-8-sig", newline="") as file_handle:
		return list(csv.DictReader(file_handle))


def show():
	st.title("Perbandingan Kernel")

	rows = []
	for kernel in KERNEL_ORDER:
		csv_rows = _read_rows(EVALUATION_FILES[kernel])
		if not csv_rows:
			continue
		first_row = csv_rows[0]
		rows.append(
			{
				"Kernel": KERNEL_LABELS[kernel],
				"Accuracy": first_row.get("accuracy", ""),
				"Precision": first_row.get("precision", ""),
				"Recall": first_row.get("recall", ""),
				"F1 Score": first_row.get("f1_score", ""),
			}
		)

	if rows:
		st.dataframe(rows, width="stretch")
	else:
		st.info("Semua file evaluasi masih kosong atau belum tersedia.")
