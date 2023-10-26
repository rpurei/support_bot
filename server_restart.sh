#!/bin/bash
kill -9 $(ps aux | grep -v "uvicorn main:app" | grep uvicorn | awk '{print $2}')
export TRANSFORMERS_CACHE=/var/www/chatbot/api/cache
cd /var/www/chatbot/api
source /var/www/chatbot/api/venv/bin/activate
pip install -r requirements.txt
/var/www/chatbot/api/venv/bin/uvicorn main:app --host 127.0.0.1 --port 3000 --ssl-keyfile /etc/ssl/zdmail.key  --ssl-certfile /etc/ssl/zdmail.crt >> /var/www/chatbot/api/logs/api.log
