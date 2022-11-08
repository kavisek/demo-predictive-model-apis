FROM python:3.9-alpine

COPY . /app

WORKDIR /app

RUN apk update
RUN apk add bash
RUN apk add --update build-base linux-headers python3-dev py-psutil && rm -rf /var/cache/apk/*
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash"]