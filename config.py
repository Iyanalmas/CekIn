"""Global application configuration."""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "output"


MODELS = {
	"linear": MODELS_DIR / "model_linear.pkl",
	"rbf": MODELS_DIR / "model_rbf.pkl",
	"polynomial": MODELS_DIR / "model_polynomial.pkl",
	"sigmoid": MODELS_DIR / "model_sigmoid.pkl",
}

TFIDF_PATH = MODELS_DIR / "tfidf.pkl"

EVALUATION_FILES = {
	"linear": DATA_DIR / "hasil_evaluasi_linear.csv",
	"rbf": DATA_DIR / "hasil_evaluasi_rbf.csv",
	"polynomial": DATA_DIR / "hasil_evaluasi_polynomial.csv",
	"sigmoid": DATA_DIR / "hasil_evaluasi_sigmoid.csv",
}

KERNEL_ORDER = ["linear", "rbf", "polynomial", "sigmoid"]

KERNEL_LABELS = {
	"linear": "Linear",
	"rbf": "RBF",
	"polynomial": "Polynomial",
	"sigmoid": "Sigmoid",
}

LABEL_MAP = {
	0: "Valid",
	1: "Hoaks",
	"valid": "Valid",
	"hoaks": "Hoaks",
	"hoax": "Hoaks",
}

DEFAULT_KERNEL = "polynomial"
