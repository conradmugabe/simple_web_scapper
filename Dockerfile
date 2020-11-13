FROM python:3.7.7 AS builder
WORKDIR /app

# RUN apk add --no-cache libxml2-dev libxslt-dev gcc

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
# Sets utf-8 encoding for Python et al
ENV LANG=C.UTF-8
# Turns off writing .pyc files; superfluous on an ephemeral container.
ENV PYTHONDONTWRITEBYTECODE=1
# Seems to speed things up
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.7.7 AS app
# RUN apk add --no-cache libxml2-dev libxslt-dev gcc

# Extra python env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
# copy in Python environment
COPY --from=builder /opt/venv /opt/venv

COPY . .

# ENTRYPOINT ["exec", "gunicorn", "--bind", ":$PORT", "--workers", "1", "--threads", "8", "--timeout", "0", "template_gateway:app"]
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 template_gateway:app

FROM app AS tester
RUN pip install pytest
RUN pytest