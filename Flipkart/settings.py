from pathlib import Path  # Ensure Path is imported

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Ensure this points to your static directory
]


