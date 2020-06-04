FROM python:3.7.0-alpine3.8

WORKDIR /app

RUN apk add --update --no-cache --virtual build-deps gcc python3-dev musl-dev libc-dev linux-headers libxslt-dev libxml2-dev
RUN apk add libffi-dev openssl-dev

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . .

ENV FLASK_APP=main.py

CMD flask run --host=0.0.0.0