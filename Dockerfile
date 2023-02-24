FROM python:3.10

ENV PYTHONBUFFERRED 1

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

