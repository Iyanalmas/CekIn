"""Home page for news prediction."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from config import DEFAULT_KERNEL, OUTPUT_DIR
from services.confidence import confidence_color, confidence_level
from services.predictor import predict_news
from utils.formatter import format_label, format_percentage
from utils.helper import append_csv_row, current_timestamp, normalize_text


LOG_PATH = OUTPUT_DIR / "prediction_log.csv"


def _log_prediction(text: str, result: dict) -> None:
    append_csv_row(
        LOG_PATH,
        {
            "timestamp": current_timestamp(),
            "input_text": text,
            "kernel": result["kernel"],
            "label": result["label"],
            "confidence": f"{result['confidence']:.2f}",
        },
        ["timestamp", "input_text", "kernel", "label", "confidence"],
    )


def _feature_dataframe(top_features):
    if not top_features:
        return pd.DataFrame(columns=["Fitur", "Bobot TF-IDF"])

    return pd.DataFrame(
        [
            {
                "Fitur": word,
                "Bobot TF-IDF": round(score, 3),
            }
            for word, score in top_features
        ]
    )


def show():
    st.title("Prediksi Hoaks Berita")

    if "selected_kernel" not in st.session_state:
        st.session_state.selected_kernel = "polynomial"

    col_input, col_action = st.columns([4, 1])

    with col_input:
        text = st.text_area(
            "Judul berita",
            placeholder="Ada Berita apa hari ini ...",
            label_visibility="collapsed",
            height=68,
        )

    with col_action:
        submitted = st.button(
            "Prediksi",
            type="primary",
            use_container_width=True,
        )

    kernel = st.session_state.selected_kernel

    if submitted:
        cleaned_text = normalize_text(text)

        if not cleaned_text:
            st.warning("Masukkan judul berita terlebih dahulu.")
            return

        result = predict_news(
            cleaned_text,
            kernel=kernel or DEFAULT_KERNEL,
        )

        _log_prediction(cleaned_text, result)

        color = confidence_color(result["confidence"])
        level = confidence_level(result["confidence"])

        # ==========================
        # Hasil Prediksi
        # ==========================

        st.markdown(
            "<hr class='result-divider'>",
            unsafe_allow_html=True,
        )

        box_label, box_value, box_confidence = st.columns(3)

        with box_label:
            st.markdown(
                "<div class='result-box result-box-label'>Hasil Prediksi</div>",
                unsafe_allow_html=True,
            )

        with box_value:
            st.markdown(
                f"<div class='result-box result-box-value'>{format_label(result['label'])}</div>",
                unsafe_allow_html=True,
            )

        with box_confidence:
            st.markdown(
                f"<div class='result-box result-box-confidence' style='border-color:{color};'>"
                f"Confidence: {format_percentage(result['confidence'])} ({level})"
                f"</div>",
                unsafe_allow_html=True,
            )

        # ==========================
        # Hasil Preprocessing
        # ==========================

        if result["processed_text"]:
            st.markdown("### 📄 Hasil Preprocessing")

            st.markdown(
                f"<div class='result-box result-box-processed'>{result['processed_text']}</div>",
                unsafe_allow_html=True,
            )

        # ==========================
        # Fitur TF-IDF
        # ==========================

        st.markdown("### 📌 Fitur yang Paling Berpengaruh")

        st.caption(
            "Semakin besar bobot TF-IDF, semakin besar kontribusi fitur terhadap keputusan model."
        )

        st.dataframe(
            _feature_dataframe(result["top_features"]),
            hide_index=True,
            use_container_width=True,
        )

        # ==========================
        # Alasan Prediksi
        # ==========================

        st.markdown("### 💡 Alasan Prediksi")

        st.info(result["explanation"])