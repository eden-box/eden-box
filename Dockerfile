FROM python:3.7.7-slim as base

FROM base as builder

RUN mkdir /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --user -r /requirements.txt

COPY ./activity_analyser ./activity_analyser

CMD ["python", "-m", "activity_analyser"]
