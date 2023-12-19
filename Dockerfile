FROM python:3.11.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update && \
    pip install --upgrade pip  && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
