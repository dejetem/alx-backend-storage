#!/usr/bin/env python3
"""
a function that changes all topics of a school document
based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name(str)
        topics(str)
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
