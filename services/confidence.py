"""Confidence presentation helpers."""


def confidence_level(score: float) -> str:
	if score >= 90:
		return "high"
	if score >= 70:
		return "medium"
	return "low"


def confidence_color(score: float) -> str:
	level = confidence_level(score)
	if level == "high":
		return "#1f8f4c"
	if level == "medium":
		return "#c28b00"
	return "#c0392b"
