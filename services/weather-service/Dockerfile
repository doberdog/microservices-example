FROM python:3.6-alpine

RUN apk update && apk add bash build-base python3-dev libffi-dev postgresql-libs postgresql-dev gcc musl-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

RUN ["chmod", "+x", "./run.sh"]
ENTRYPOINT ./run.sh

