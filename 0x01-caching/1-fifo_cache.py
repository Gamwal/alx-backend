#!/usr/bin/env python3
"""
FIFO caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching
    """

    def __init__(self):
        """Intialize the object"""
        super().__init__()

    def put(self, key, item):
        """Assign a key and value to cache"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            else:
                if len(self.cache_data) < __class__.MAX_ITEMS:
                    self.cache_data[key] = item
                else:
                    first_item_key = list(self.cache_data.keys())[0]
                    print(f'DISCARD: {first_item_key}')
                    del self.cache_data[first_item_key]
                    self.cache_data[key] = item

    def get(self, key):
        """Retrieve a key and value to cache"""
        if key is not None:
            return self.cache_data.get(key)
