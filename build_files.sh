#!/bin/bash
echo "=== Building TourCraze for Vercel ==="
python -m pip install -r requirements.txt
python tourCraze/manage.py collectstatic --noinput --clear
echo "=== Build Complete ==="
