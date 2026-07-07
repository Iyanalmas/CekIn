"""Formatting helpers for UI output."""


def format_label(label: str) -> str:
	normalized = label.strip().lower()
	if normalized == "valid":
		return "Valid"
	if normalized == "hoaks":
		return "Hoaks"
	return label.title()


def format_percentage(value: float) -> str:
	return f"{value:.2f}%"


def format_metric(value) -> str:
	if isinstance(value, float):
		return f"{value:.4f}".rstrip("0").rstrip(".")
	return str(value)
