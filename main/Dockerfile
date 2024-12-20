FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /main

COPY requirements.txt .
RUN pip install  -r requirements.txt


COPY . .

USER root
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

RUN apt-get update && apt-get clean

CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8080"]
