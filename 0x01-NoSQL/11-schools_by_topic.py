#!/usr/bin/env python3
""" Documentation """


def schools_by_topic(mongo_collection, topic):
    """ find function"""

    res = mongo_collection.find({"topics": topic})
    return res
