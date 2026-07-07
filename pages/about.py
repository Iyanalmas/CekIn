"""Static about page."""

import streamlit as st


def show():
	st.title("Tentang Sistem")
	st.markdown(
		"""
		Aplikasi ini digunakan untuk klasifikasi berita menggunakan SVM dengan beberapa kernel.

		Alur umumnya:
		1. Teks berita dimasukkan oleh pengguna.
		2. Teks diproses melalui preprocessing yang sama seperti saat training.
		3. TF-IDF mengubah teks menjadi fitur numerik.
		4. Model SVM menghasilkan label prediksi dan confidence score.
		"""
	)
