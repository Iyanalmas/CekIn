"""General helper functions."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path


def normalize_text(text: str) -> str:
	return " ".join(text.split()).strip()


def read_csv_rows(path: Path) -> list[dict[str, str]]:
	if not path.exists():
		return []

	with path.open("r", encoding="utf-8-sig", newline="") as file_handle:
		return list(csv.DictReader(file_handle))


def append_csv_row(path: Path, row: dict[str, str], fieldnames: list[str]) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	file_exists = path.exists() and path.stat().st_size > 0

	with path.open("a", encoding="utf-8", newline="") as file_handle:
		writer = csv.DictWriter(file_handle, fieldnames=fieldnames)
		if not file_exists:
			writer.writeheader()
		writer.writerow(row)


def current_timestamp() -> str:
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
