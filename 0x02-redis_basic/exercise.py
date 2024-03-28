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


def call_history(method: Callable) -> Callable:
    """ Count the number of calls"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ the wrapper function """
        inputs = "{}:inputs".format(method.__qualname__)
        outputs = "{}:outputs".format(method.__qualname__)
        result = method(self, *args, **kwargs)
        self._redis.rpush(inputs, str(args))
        self._redis.rpush(outputs, str(result))
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

    @call_history
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


def replay(method: Callable) -> None:
    """Documentation"""
    c = redis.Redis()
    inputs = c.lrange("Cache.store:inputs", 0, -1)
    outputs = c.lrange("Cache.store:outputs", 0, -1)

    print('{} was called {} times'.format(method.__qualname__,
          c.get('Cache.store').decode("utf-8")))

    for inp, out in zip(inputs, outputs):
        print(
            "{}(*{}) -> {}".format(inp.decode("utf-8"),
                                   out.decode("utf-8"))
        )
