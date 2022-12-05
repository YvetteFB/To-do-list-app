FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

