#!/usr/bin/env python3
"""MRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching"""

    AGE_BITS = []

    def put(self, key, item):
        """populates a caching dict"""
        if key is None or item is None:
            pass
        else:
            if self.cache_data.get(key):
                del self.cache_data[key]
                MRUCache.AGE_BITS.remove(key)
            self.cache_data[key] = item
            MRUCache.AGE_BITS.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard_key = MRUCache.AGE_BITS.pop(-2)
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """Retrieves a cached item"""
        if self.cache_data.get(key):
            MRUCache.AGE_BITS.remove(key)
            MRUCache.AGE_BITS.append(key)

        return self.cache_data.get(key)
