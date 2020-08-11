FROM python:3.8-buster

RUN mkdir /app

COPY app /app/app
COPY dev_server.py /app/
COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt
CMD python dev_server.py