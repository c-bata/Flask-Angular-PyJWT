import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# database
DEBUG = True
DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

# Generate a random secret key
SECRET_KEY = os.urandom(24)

CSRF_ENABLED = True
