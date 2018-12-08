FROM python:3.6-alpine

RUN apk update && apk add bash build-base python3-dev libffi-dev gcc

WORKDIR /app

COPY ./ ./
RUN pip install pypiserver

RUN ["chmod", "+x", "./run.sh"]
ENTRYPOINT ["bash", "./run.sh"]

