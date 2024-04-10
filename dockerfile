FROM python:3.11.7-slim

ARG BUILD_DEPS="curl"
RUN apt-get update && apt-get install -y $BUILD_DEPS
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.2.0 POETRY_HOME=/root/poetry python3 -
ENV PATH="${PATH}:/root/poetry/bin"

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.7.0 POETRY_HOME=/root/poetry python3 -
ENV PATH="${PATH}:/root/poetry/bin"

COPY pyproject.toml /DRF_shedule_4_coach/
WORKDIR /DRF_shedule_4_coach
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY core schedule_api manage.py README.md ./

