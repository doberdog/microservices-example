FROM node:10.14.1-alpine

WORKDIR /app

RUN apk update && apk add yarn python3
RUN alias python=python3

COPY package.json .
COPY yarn.lock .

RUN yarn install

COPY . .

EXPOSE 3000
ENTRYPOINT yarn start
