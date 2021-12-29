#https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV LISTEN_PORT 42069

COPY . /app

RUN apt update
RUN apt install -y libpq-dev build-essential
RUN pip3 install flask flask_marshmallow flask_sqlalchemy marshmallow-sqlalchemy psycopg2