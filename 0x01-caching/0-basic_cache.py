#!/usr/bin/env python3
"""
Basic dictionary
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic dictionary
    """

    def __init__(self):
        """Intialize the object"""
        super().__init__()

    def put(self, key, item):
        """Assign a key and value to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve a key and value to cache"""
        if key is not None:
            return self.cache_data.get(key)
