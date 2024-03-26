#!/usr/bin/env python3
""" Documentation """


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""

    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
