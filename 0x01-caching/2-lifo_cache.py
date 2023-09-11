#!/usr/bin/python3
"""LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache inherit from BaseCaching"""
    def __init__(self):
        """Initiation"""
        super().__init__()

    def put(self, key: str, item: str) -> None:
        """Updates Dic on base class"""
        if key is None or item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last = list(self.cache_data.keys())[-1]
            del self.cache_data[last]
            print(f"Discard: {last}")
        self.cache_data[key] = item

    def get(self, key):
        """Get value using key"""
        if key is None or self.cache_data[key] is None:
            return None
        return self.cache_data[key]
