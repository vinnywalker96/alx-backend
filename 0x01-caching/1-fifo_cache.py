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
        if key is not None or item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            data = next(iter(self.cache_data))
            remove = self.cache_data.pop(data)
            print(f"DISCARD {data}")

    def get(self, key):
        """get data by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
