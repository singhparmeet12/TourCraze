import os
import sys
from pathlib import Path

# Ensure the Django project directory is on Python's module search path
PROJECT_DIR = Path(__file__).resolve().parent.parent / "tourCraze"
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourCraze.settings')

import django
django.setup()

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

# In serverless environments, initialize the database tables in /tmp if not present
if os.environ.get('VERCEL'):
    try:
        db_file = '/tmp/db.sqlite3'
        if not os.path.exists(db_file):
            call_command('migrate', interactive=False)
    except Exception as e:
        print("Vercel DB initialization note:", e)

# Vercel serverless function entrypoint
app = get_wsgi_application()
