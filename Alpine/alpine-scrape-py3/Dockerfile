# vim:set ft=dockerfile:
# This is a docker include web scrap library for py3

ARG ALPINE_PY3_VERSION=latest
FROM alpine-py3:${ALPINE_PY3_VERSION}

LABEL maintainer="August Tu"

RUN echo "**** install Python Packages ****" && \
    pip install -U \
       requests && \
    echo "**** clean up ****" && \
    rm -rf \
       /var/cache/apk/* \
       /root/.cache \
       /tmp/*
