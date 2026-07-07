"""Prediction helpers for news classification."""

from __future__ import annotations

import math

from config import DEFAULT_KERNEL, LABEL_MAP
from services.loader import load_artifacts
from services.preprocessing import preprocess_text


def _map_label(prediction):
	if isinstance(prediction, str):
		return LABEL_MAP.get(prediction.lower(), prediction.title())
	return LABEL_MAP.get(prediction, str(prediction))


def _confidence_from_model(model, features) -> float:
	if hasattr(model, "predict_proba"):
		probabilities = model.predict_proba(features)[0]
		return float(max(probabilities) * 100)

	if hasattr(model, "decision_function"):
		decision = model.decision_function(features)
		if hasattr(decision, "__iter__"):
			decision = decision[0]
		return float((1 / (1 + math.exp(-float(decision)))) * 100)

	return 0.0


def predict_news(text: str, kernel: str = DEFAULT_KERNEL) -> dict:
	artifacts = load_artifacts(kernel)
	model = artifacts["model"]
	tfidf = artifacts["tfidf"]

	processed_text = preprocess_text(text)
	features = tfidf.transform([processed_text])
	raw_prediction = model.predict(features)[0]
	label = _map_label(raw_prediction)
	confidence = _confidence_from_model(model, features)

	return {
		"label": label,
		"confidence": round(confidence, 2),
		"processed_text": processed_text,
		"kernel": kernel,
	}
