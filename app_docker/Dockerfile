FROM python:3.8-slim

ARG runfile

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

ENTRYPOINT ["sh", "./app_docker/docker-entrypoint.sh"]

ENV FLASK_APP=$runfile
CMD flask run --host=0.0.0.0
