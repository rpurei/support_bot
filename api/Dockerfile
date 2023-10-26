FROM python:3.9
WORKDIR /var/www/chatbot/api
COPY . .
ENV TRANSFORMERS_CACHE=/var/www/chatbot/api/cache
RUN rm /bin/sh && ln -s /bin/bash /bin/sh # && python -m venv venv && source /var/www/chatbot/api/venv/bin/activate
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
EXPOSE 3000
