from pathlib import Path  # Ensure Path is imported

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Ensure this points to your static directory
]

LOGIN_URL = 'login'  # Use the URL pattern name defined in accounts/urls.py
LOGOUT_REDIRECT_URL = '/'  # Redirect to the home page after logout



