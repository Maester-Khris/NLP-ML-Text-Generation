FROM python:3.8-slim

WORKDIR /api-flask

COPY controllers/ /api-flask/controllers/
COPY models/  /api-flask/models/
COPY services/  /api-flask/services/
COPY __init__.py app.py  /api-flask/

RUN apt-get update
RUN apt-get -y install gcc
RUN apt-get -y install g++
RUN apt-get -y install python3-dev
RUN pip3 install --upgrade pip && pip install --no-cache-dir gunicorn flask Flask-RESTful flasgger torchvision bert-extractive-summarizer
RUN python -m spacy download fr_core_news_sm

EXPOSE 3000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:3000", "-w", "4"]
