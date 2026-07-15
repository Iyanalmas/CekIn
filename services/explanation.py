"""Generate explanation for prediction results."""

from __future__ import annotations


def _confidence_sentence(confidence: float) -> str:
    """Menghasilkan kalimat berdasarkan tingkat confidence."""

    if confidence >= 90:
        return (
            "Model memiliki tingkat keyakinan yang sangat tinggi terhadap hasil klasifikasi ini."
        )

    elif confidence >= 75:
        return (
            "Model memiliki tingkat keyakinan yang tinggi terhadap hasil klasifikasi ini."
        )

    elif confidence >= 60:
        return (
            "Model memiliki tingkat keyakinan sedang sehingga hasil prediksi sebaiknya digunakan sebagai indikasi awal."
        )

    return (
        "Model memiliki tingkat keyakinan yang relatif rendah sehingga hasil klasifikasi perlu ditafsirkan dengan hati-hati."
    )


def generate_explanation(
    label: str,
    confidence: float,
    top_features: list[tuple[str, float]],
) -> str:
    """
    Membuat penjelasan hasil klasifikasi berdasarkan
    label, confidence, dan fitur TF-IDF yang paling berpengaruh.
    """

    keywords = [word for word, _ in top_features]

    kata1 = keywords[0] if len(keywords) > 0 else ""
    kata2 = keywords[1] if len(keywords) > 1 else ""
    kata3 = keywords[2] if len(keywords) > 2 else ""

    confidence_text = _confidence_sentence(confidence)

    if label.lower() == "valid":

        if confidence >= 90:
            explanation = (
                f'Berdasarkan hasil analisis, pola kosakata pada judul berita lebih menyerupai karakteristik berita valid yang dipelajari model. '
                f'Fitur "{kata1}", "{kata2}", dan "{kata3}" memberikan kontribusi terbesar terhadap keputusan tersebut.'
            )

        elif confidence >= 75:
            explanation = (
                f'Model menemukan bahwa kombinasi kata "{kata1}", "{kata2}", dan "{kata3}" '
                f'memiliki pola yang lebih dekat dengan data berita valid selama proses pelatihan sehingga judul diprediksi sebagai Valid.'
            )

        elif confidence >= 60:
            explanation = (
                f'Hasil klasifikasi menunjukkan bahwa representasi TF-IDF dari judul memiliki kemiripan dengan pola berita valid. '
                f'Kata "{kata1}" dan "{kata2}" menjadi fitur yang paling memengaruhi keputusan model.'
            )

        else:
            explanation = (
                f'Sistem memprediksi berita sebagai Valid karena pola kosakata hasil preprocessing '
                f'lebih banyak menyerupai pola berita valid pada data pelatihan. '
                f'Kata "{kata1}" dan "{kata2}" menjadi indikator yang paling berpengaruh.'
            )

    else:

        if confidence >= 90:
            explanation = (
                f'Berdasarkan hasil analisis, pola kosakata pada judul memiliki kemiripan dengan karakteristik berita hoaks pada data pelatihan. '
                f'Kata "{kata1}", "{kata2}", dan "{kata3}" merupakan fitur yang paling berkontribusi terhadap keputusan model.'
            )

        elif confidence >= 75:
            explanation = (
                f'Model menemukan bahwa kombinasi kata "{kata1}", "{kata2}", dan "{kata3}" '
                f'lebih sering muncul pada pola berita hoaks selama proses pelatihan sehingga judul diprediksi sebagai Hoaks.'
            )

        elif confidence >= 60:
            explanation = (
                f'Representasi TF-IDF dari judul menunjukkan kemiripan dengan pola berita hoaks yang telah dipelajari model. '
                f'Fitur "{kata1}" dan "{kata2}" menjadi faktor utama dalam proses klasifikasi.'
            )

        else:
            explanation = (
                f'Sistem memprediksi judul sebagai Hoaks karena pola kata hasil preprocessing '
                f'memiliki kemiripan yang lebih tinggi dengan data berita hoaks pada proses pelatihan. '
                f'Fitur utama yang memengaruhi keputusan adalah "{kata1}" dan "{kata2}".'
            )

    return f"{explanation} {confidence_text}"