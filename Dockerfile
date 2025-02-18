FROM python:3.10-slim

WORKDIR /api-flask

COPY trainer/  /api-flask/trainer/
COPY services/  /api-flask/services/
COPY controllers/ /api-flask/controllers/
COPY static/  /api-flask/static/
COPY templates/  /api-flask/templates/
COPY __init__.py app.py flask_blueprint.py /api-flask/

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc g++ python3-dev curl

# RUN apt-get -y install gcc
# RUN apt-get -y install g++
# RUN apt-get -y install python3-dev torch
RUN pip3 install --upgrade pip && pip install --no-cache-dir gunicorn flask Flask-RESTful flasgger bert-extractive-summarizer
RUN python -m spacy download fr_core_news_sm

EXPOSE 3000

CMD ["gunicorn", "app:create_app()", "-b", "0.0.0.0:3000", "-w", "2"]
