FROM node:10.14.1-alpine

WORKDIR /app

RUN apk update && apk add yarn python3
RUN alias python=python3

COPY package.json .
COPY package-lock.json .
COPY yarn.lock .

RUN npm install

COPY . .

ENTRYPOINT npm run dev
