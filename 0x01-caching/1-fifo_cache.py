#!/usr/bin/python3
"""FIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits BaseCaching
    """
    def __init__(self):
        """Initializing """
        super().__init__()

    def put(self, key, item):
        """Add item to basecache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first = next(iter(self.cache_data))
            del self.cache_data[first]
            print(f"DISCARD: {first}")
        self.cache_data[key] = item

    def get(self, key):
        """Gets value"""
        if key is None or self.cache_data[key] is None:
            return None
        return self.cache_data[key]
