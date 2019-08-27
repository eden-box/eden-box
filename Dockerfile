FROM python:3.7-slim-buster as base

FROM base as builder

RUN mkdir /install
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    musl-dev \
    postgresql-dev

WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY activity_analyser /app

# defined in docker-compose
ARG CONFIG

# get deploy configuration from host
COPY ${CONFIG}/activity_analyser/config.yaml /app/config.yaml

CMD ["python -m", "app"]
