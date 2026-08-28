import os
import sys
import shutil
from pathlib import Path

# Ensure the Django project directory is on Python's module search path
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = BASE_DIR / "tourCraze"
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourCraze.settings')

# Detect serverless execution (Vercel, AWS Lambda, or read-only filesystem)
IS_SERVERLESS = bool(
    os.environ.get('VERCEL')
    or os.environ.get('VERCEL_ENV')
    or os.environ.get('AWS_LAMBDA_FUNCTION_NAME')
    or not os.access(str(PROJECT_DIR), os.W_OK)
)

if IS_SERVERLESS:
    src_db = PROJECT_DIR / "db.sqlite3"
    tmp_db = Path("/tmp/db.sqlite3")
    try:
        # Copy the pre-seeded SQLite database to the writable /tmp directory
        if src_db.exists() and (not tmp_db.exists() or tmp_db.stat().st_size == 0):
            shutil.copyfile(str(src_db), str(tmp_db))
    except Exception as e:
        print("Vercel DB copy note:", e)

import django
django.setup()

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

# Auto-migrate any unapplied migrations
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print("Vercel migration note:", e)

# Vercel serverless function entrypoint
app = get_wsgi_application()
