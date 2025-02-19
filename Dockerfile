FROM python:3.10-slim

WORKDIR /api-flask

COPY trainer/  /api-flask/trainer/
COPY services/  /api-flask/services/
COPY controllers/ /api-flask/controllers/
COPY static/  /api-flask/static/
COPY templates/  /api-flask/templates/
COPY __init__.py app.py flask_blueprint.py /api-flask/

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc g++ python3-dev cron curl

# RUN apt-get -y install gcc
# RUN apt-get -y install g++
# RUN apt-get -y install python3-dev torch
RUN pip3 install --upgrade pip && pip install --no-cache-dir gunicorn flask Flask-RESTful flasgger spacy joblib
#bert-extractive-summarizer
RUN python -m spacy download fr_core_news_sm



# Create a script to ping the URL
RUN echo '#!/bin/sh\nif curl -s http://google.com > /dev/null; then\n    echo "Ping successful at $(date)"\nfi' > /usr/local/bin/ping-url.sh && \
    chmod +x /usr/local/bin/ping-url.sh

# Add cron job
RUN echo "*/2 * * * * /usr/local/bin/ping-url.sh" >> /etc/crontab


EXPOSE 10000

# Copy the start script and make it executable
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# Use exec form for CMD
CMD ["/usr/local/bin/start.sh"]

#CMD ["gunicorn", "app:create_app()", "-b", "0.0.0.0:10000", "-w", "2"]
#CMD cron && gunicorn app:create_app() -b 0.0.0.0:10000 -w 2

