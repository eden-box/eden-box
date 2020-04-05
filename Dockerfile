FROM python:3.7.7-slim as base

FROM base as builder

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

ENV APPUSERID=500

RUN useradd -ms /bin/bash app -u ${APPUSERID}
USER app
WORKDIR /home/app

COPY --chown=app:app requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/app/.local/bin:${PATH}"

COPY --chown=app:app ./activity_analyser ./activity_analyser

ENTRYPOINT ["python", "-m", "activity_analyser"]
