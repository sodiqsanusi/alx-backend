#!/usr/bin/env python3
"""
Build a caching system, use the FIFO cache algorithm
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    Using the FIFO cache algorithm, build a caching system
    """
    def __init__(self):
        """
        Initialise the cache
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        Adds an item to the cache. uses the FIFO caching algo
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_removed = self.key_indexes.pop(0)
                del self.cache_data[item_removed]
                print(f"DISCARD: {item_removed}")

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        Get the value from the cache
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
