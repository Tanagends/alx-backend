#!/usr/bin/env python3
"""LRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LIFO Caching"""

    AGE_BITS = []

    def put(self, key, item):
        """populates a caching dict"""
        if key is None or item is None:
            pass
        else:
            if self.cache_data.get(key):
                del self.cache_data[key]
                LRUCache.AGE_BITS.remove(key)
            self.cache_data[key] = item
            LRUCache.AGE_BITS.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard_key = LRUCache.AGE_BITS.pop(0)
                del self.cache_data[discard_key]
                print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """Retrieves a cached item"""
        if self.cache_data.get(key):
            LRUCache.AGE_BITS.remove(key)
            LRUCache.AGE_BITS.append(key)

        return self.cache_data.get(key)
