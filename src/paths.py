"""Shared paths for notebooks."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
TRANSACTIONS_CSV = DATA_DIR / "transactions_dataset.csv"
