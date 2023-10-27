#!/usr/bin/env python3
"""
MRU caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRU caching
    """

    def __init__(self):
        """Intialize the object"""
        self.mru = []
        super().__init__()

    def put(self, key, item):
        """Assign a key and value to cache"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.mru.remove(key)
                self.mru.append(key)
            else:
                if len(self.cache_data) < __class__.MAX_ITEMS:
                    self.cache_data[key] = item
                    self.mru.append(key)
                else:
                    print(f'DISCARD: {self.mru[-1]}')
                    del self.cache_data[self.mru[-1]]
                    self.cache_data[key] = item
                    self.mru.remove(self.mru[-1])
                    self.mru.append(key)

    def get(self, key):
        """Retrieve a key and value to cache"""
        if key is not None:
            if key in self.cache_data.keys():
                self.mru.remove(key)
                self.mru.append(key)
            return self.cache_data.get(key)
