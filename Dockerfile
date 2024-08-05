FROM python:3.8-slim

WORKDIR /api-flask

COPY controllers/ /api-flask/controllers/
COPY models/  /api-flask/models/
COPY services/  /api-flask/services/
COPY __init__.py app.py  /api-flask/

RUN apt-get update
RUN apt-get -y install gcc
RUN pip3 install --upgrade pip && pip install --no-cache-dir flask Flask-RESTful flasgger bert-extractive-summarizer

EXPOSE 3000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:3000", "-w", "4"]
