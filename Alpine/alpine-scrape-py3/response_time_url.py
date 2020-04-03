#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for test alpine-scrape docker.

This module be writen for test docker, it also can be used for testing URL response time.
The key function: get_response_time_by_url

  Typical usage example:

  get_response_time_by_url('http://shiok.tech')
  $ python response_time_url.py "http://shiok.tech"
"""
import os
import logging
import requests
from logging.handlers import TimedRotatingFileHandler

LOG_PATH = '/scripts'
url = 'http://shiok.tech/'


def get_response_time_by_url(address):
    """Access the URL, return response time.

    Args:
        address: The URL will be accessed.

    Returns:
        status, value
        if status == 0, value = string of response time
        if status == -1. value = error describer
    """
    try:
        r = requests.get(address, timeout=6)
        r.raise_for_status()
        resp_time = str(round(r.elapsed.total_seconds(), 2))
        return 0, resp_time
    except requests.exceptions.HTTPError as err01:
        return -1, "HTTP error: " + str(err01)
    except requests.exceptions.ConnectionError as err02:
        return -1, "Error connecting: " + str(err02)
    except requests.exceptions.Timeout as err03:
        return -1, "Timeout error:" + str(err03)
    except requests.exceptions.RequestException as err04:
        return -1, "Error: " + str(err04)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        url = sys.argv[1]
    logger = logging.getLogger("Response time log")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')

    # writing to file
    handler = TimedRotatingFileHandler(os.path.join(LOG_PATH, 'response-time.log'), when='midnight', backupCount=30)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # writing to stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    ret_code, ret_str = get_response_time_by_url(url)
    if ret_code == 0:
        logger.info(ret_str)
    else:
        logger.error(ret_str)
