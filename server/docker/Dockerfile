FROM python:3.7.0-alpine3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt
RUN poetry shell
RUN poetry install & poetry update

COPY . .

ENV FLASK_APP=main.py

CMD flask run --host=0.0.0.0