#!/usr/bin/env python3
"""FIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching"""

    def put(self, key, item):
        """populates a caching dict"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = next(iter(self.cache_data))
            del self.cache_data[discard_key]
            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """Retrieves a cached item"""
        return self.cache_data.get(key)
