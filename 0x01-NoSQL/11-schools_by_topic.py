#!/usr/bin/env python3
""" Documentation """


def schools_by_topic(mongo_collection, topics):
    """ find function"""

    res = mongo_collection.find({"topics": topic})
    return res
