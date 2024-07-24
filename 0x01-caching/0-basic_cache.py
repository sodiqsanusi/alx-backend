#!/usr/bin/env python3
"""
Work on creating a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    This builds on the baseCaching class to build a caching system
    """
    def put(self, key, item):
        """
        Adds a given key-value pair to the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the data from cache
        """
        return self.cache_data.get(key, None)
