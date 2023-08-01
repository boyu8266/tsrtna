FROM python:3.11.4-slim-bullseye

WORKDIR /app

COPY requirements.txt setup.py ./
COPY tsrtna ./tsrtna

RUN python setup.py install

CMD ["tsrtna"]