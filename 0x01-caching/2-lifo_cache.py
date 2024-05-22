#!/usr/bin/env python3
"""LIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching"""

    def put(self, key, item):
        """populates a caching dict"""
        if key is None or item is None:
            pass
        else:
            if self.cache_data.get(key):
                del self.cache_data[key]
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard_key = list(self.cache_data.keys())[-2]
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """Retrieves a cached item"""
        return self.cache_data.get(key)
