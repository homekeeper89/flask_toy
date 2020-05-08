FROM python:3.7.4-alpine
MAINTAINER matthew "matthew@cupist.com"

RUN apk add --update --no-cache --virtual build-deps gcc python3-dev musl-dev libc-dev linux-headers libxslt-dev libxml2-dev
RUN apk add libffi-dev openssl-dev libpq postgresql-dev

RUN pip install --upgrade pip setuptools
RUN pip install poetry

COPY poetry.lock pyproject.toml /
RUN poetry install
RUN poetry shell

COPY . /
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["main.py"]

# $ docker build -t flask-application:latest .
# $ docker run -d -p 5000:5000 flask-application