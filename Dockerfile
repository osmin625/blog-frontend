FROM klakegg/hugo:latest as builder

WORKDIR /site
COPY . .
RUN hugo
