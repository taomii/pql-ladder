FROM python:3.8-slim-buster

WORKDIR /poller

COPY . /poller/

RUN apt update
RUN apt install -y libpq-dev build-essential
RUN pip3 install -r requirements.txt

ENV PYTHONPATH /poller

CMD [ "python3", "main.py"]