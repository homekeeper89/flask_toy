FROM python:3.7.2-stretch

ARG runfile

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

ENV FLASK_APP=$runfile
# CMD flask run --host=0.0.0.0
CMD ["uwsgi", "app.ini"]
