FROM python:3.7.7-slim as base

FROM base as builder

RUN mkdir /install
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY ./activity_analyser ./activity_analyser

CMD ["python", "-m", "activity_analyser"]
