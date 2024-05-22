#!/usr/bin/env python3
"""Basic Dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Dictionary"""

    def put(self, key, item):
        """populates a caching dict"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves a cached item"""
        return self.cache_data.get(key)
