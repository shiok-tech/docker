# vim:set ft=dockerfile:
# This is a base docker for add timezone support to alpine
# Don't use it directly
ARG ALPINE_VERSION=latest
ARG TIMEZONE="Asia/Singapore"
FROM alpine:${ALPINE_VERSION}

LABEL maintainer="August Tu" 

RUN apk update \
        && apk upgrade \
        && apk add --no-cache tzdata \
        && cp /usr/share/zoneinfo/Asia/Singapore /etc/localtime \
        && echo ${TIMEZONE} > /etc/timezone \
        && apk del tzdata \
        && rm -rf \
              /var/cache/apk/* \
              /root/.cache \
              /tmp/*
