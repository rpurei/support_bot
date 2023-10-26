#!/bin/bash
export TRANSFORMERS_CACHE=/var/www/chatbot/api/cache
cd /var/www/chatbot/api
source /var/www/chatbot/api/venv/bin/activate
pip install -r requirements.txt
/var/www/chatbot/api/venv/bin/uvicorn main:app --host 0.0.0.0 --port 3000
