#!/usr/bin/env python3
"""
a function that returns the list of school having
a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    this function finds schools by topic
    Args:
        mongo_collection: pymongo collection object
        topic(str)
    Returns: list of schools having the specified topic
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
