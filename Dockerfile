FROM python:3.11.4-slim-bullseye

WORKDIR /app

COPY requirements.txt setup.py config.ini ./
COPY tsrtna ./tsrtna

RUN python setup.py install
RUN twstock -U

CMD ["tsrtna"]