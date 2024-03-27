#!/usr/bin/env python3
""" Module Documentation"""

import redis
from  uuid import uuid4
from typing import Union


class Cache:
    """task 0 : Cache class"""

    def __init__(self):
        """
            store an instance of the Redis and
            flush the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the input data in Redis using the random key
        and return the key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
