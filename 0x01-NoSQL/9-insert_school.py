#!/usr/bin/env python3
"""
A function that inserts a new document in a collection
based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    add a new document to an existing collection
    and returns the new id
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
