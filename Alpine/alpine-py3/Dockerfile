# vim:set ft=dockerfile:
# This is a base docker for add pure python 3 support
# Don't use it directly

# If want to specify version, please uncommit PYTHON3_VERSION
# See: https://pkgs.alpinelinux.org/packages

ARG ALPINE_TIMEZONE_VERSION=latest
#ARG PYTHON3_VERSION=3.8.2-r0
FROM alpine-timezone:${ALPINE_TIMEZONE_VERSION}

LABEL maintainer="August Tu"

# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

RUN echo "**** install Python 3 ****" && \
    apk update && \
    apk upgrade && \
    apk add --no-cache python3 && \
#    apk add --no-cache python3=${PYTHON3_VERSION} && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    echo "**** clean up ****" && \
    rm -rf \
       /var/cache/apk/* \
       /root/.cache \
       /tmp/*
