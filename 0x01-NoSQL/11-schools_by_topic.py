#!/usr/bin/env python3
""" Documentation """


def update_topics(mongo_collection, name, topics):
    """ Update function"""

    res = mongo_collection.find({"topics": topic})
    return res
