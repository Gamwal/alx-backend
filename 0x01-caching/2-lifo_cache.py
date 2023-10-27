#!/usr/bin/env python3
"""
LIFO caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO caching
    """

    def __init__(self):
        """Intialize the object"""
        self.last_item_key = None
        super().__init__()

    def put(self, key, item):
        """Assign a key and value to cache"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.last_item_key = key
            else:
                if len(self.cache_data) < __class__.MAX_ITEMS:
                    self.cache_data[key] = item
                else:
                    if self.last_item_key is None or\
                      self.last_item_key not in self.cache_data.keys():
                        self.last_item_key = list(self.cache_data.keys())[-1]
                    print(f'DISCARD: {self.last_item_key}')
                    del self.cache_data[self.last_item_key]
                    self.cache_data[key] = item

    def get(self, key):
        """Retrieve a key and value to cache"""
        if key is not None:
            return self.cache_data.get(key)
