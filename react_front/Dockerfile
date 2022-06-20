FROM node:13.12.0-alpine as build

WORKDIR /react_front
COPY ./package.json ./
COPY ./package-lock.json ./
RUN npm ci --silent
COPY ./ ./
RUN npm run build

