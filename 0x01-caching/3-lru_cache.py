#!/usr/bin/env python3
"""
LRU caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching
    """

    def __init__(self):
        """Intialize the object"""
        self.lru = []
        super().__init__()

    def put(self, key, item):
        """Assign a key and value to cache"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.lru.remove(key)
                self.lru.append(key)
            else:
                if len(self.cache_data) < __class__.MAX_ITEMS:
                    self.cache_data[key] = item
                    self.lru.append(key)
                else:
                    print(f'DISCARD: {self.lru[0]}')
                    del self.cache_data[self.lru[0]]
                    self.cache_data[key] = item
                    self.lru.remove(self.lru[0])
                    self.lru.append(key)

    def get(self, key):
        """Retrieve a key and value to cache"""
        if key is not None:
            if key in self.cache_data.keys():
                self.lru.remove(key)
                self.lru.append(key)
            return self.cache_data.get(key)
