FROM python:3.8-slim-buster

WORKDIR /api

COPY . /api/

RUN apt update
RUN apt install -y libpq-dev build-essential
RUN pip3 install flask flask_marshmallow flask_sqlalchemy marshmallow-sqlalchemy psycopg2

ENV PYTHONPATH /api

CMD [ "python3", "api.py"]