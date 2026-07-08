"""Main Streamlit router."""

from __future__ import annotations

import streamlit as st

from config import ASSETS_DIR
from pages.evaluation import show as show_evaluation
from pages.home import show as show_home


def _load_css() -> None:
    css_path = ASSETS_DIR / "style.css"

    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )


def main():
    st.set_page_config(
        page_title="CekIn",
        page_icon=str(ASSETS_DIR / "CekinLogo.png"),
        layout="wide",
    )

    _load_css()

    st.sidebar.title("CekIn")

    page = st.sidebar.radio(
        "Navigasi",
        [
            "Home",
            "Evaluation",
        ],
    )

    if page == "Home":
        show_home()

    elif page == "Evaluation":
        show_evaluation()


if __name__ == "__main__":
    main()