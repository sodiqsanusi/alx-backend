#!/usr/bin/env python3
"""
Build a caching system, use the MRU cache algorithm
"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    Using the MRU cache algorithm, build a caching system
    """
    def __init__(self):
        """
        Initialise the cache
        """
        super().__init__()
        self.cache_indexes = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache. uses the MRU caching algo
        """
        if key and item:
            if key in self.cache_data:
                self.cache_indexes.move_to_end(key)
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_removed = self.cache_indexes.popitem(last=True)[0]
                del self.cache_data[item_removed]
                print(f"DISCARD: {item_removed}")

            self.cache_data[key] = item
            self.cache_indexes[key] = item

    def get(self, key):
        """
        Get the value from the cache
        """
        if key in self.cache_data:
            self.cache_indexes.move_to_end(key)
            return self.cache_data[key]
        return None
