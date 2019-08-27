FROM python:3.7-alpine as base

FROM base as builder

RUN mkdir /install
RUN apk update && apk add postgresql-libs gcc musl-dev
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY activity_analyser /app

# defined in docker-compose
ARG CONFIG

# get deploy configuration from host
COPY ${CONFIG}/activity_analyser/config.yaml /app/

WORKDIR /app

CMD ["python", "app"]
