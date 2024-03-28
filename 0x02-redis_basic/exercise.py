#!/usr/bin/env python3
""" Module Documentation"""

import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count the number of calls"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ the wrapper function """
        key = method.__qualname__
        self._redis.incr(key)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


class Cache:
    """task 0 : Cache class"""

    def __init__(self):
        """
            store an instance of the Redis and
            flush the instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the input data in Redis using the random key
        and return the key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """ get data """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ get data """
        data = self._redis.get(key)

        return str(data)

    def get_int(self, key: str) -> int:
        """ get data """
        data = self._redis.get(key)

        return int(data)