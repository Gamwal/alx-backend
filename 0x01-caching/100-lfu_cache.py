#!/usr/bin/env python3
"""
LFU caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    lfu caching
    """

    def __init__(self):
        """Intialize the object"""
        self.lfu = {}
        super().__init__()

    def put(self, key, item):
        """Assign a key and value to cache"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.lfu[key] += 1
            else:
                if len(self.cache_data) < __class__.MAX_ITEMS:
                    self.cache_data[key] = item
                    self.lfu[key] = 1
                else:
                    drop = min(self.lfu, key=self.lfu.get)
                    print(f'DISCARD: {drop}')
                    del self.cache_data[drop]
                    self.cache_data[key] = item
                    del self.lfu[drop]
                    self.lfu[key] = 1

    def get(self, key):
        """Retrieve a key and value to cache"""
        if key is not None:
            if key in self.cache_data.keys():
                self.lfu[key] += 1
            return self.cache_data.get(key)
