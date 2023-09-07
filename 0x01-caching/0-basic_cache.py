#!/usr/bin/python3
"""Basic dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        """add data to dict"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        return

    def get(self, key):
        """Gets value"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
