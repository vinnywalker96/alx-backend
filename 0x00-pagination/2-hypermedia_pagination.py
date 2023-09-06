#!/usr/bin/env python3
"""Simple Pagination"""
import csv
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return Page range"""
        assert (
            isinstance(page, int) and page > 0
        ), "Page must be a positive integer"
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index is not None and end_index is not None:
            return data[start_index:end_index]

        return []


    def get_hyper(self, page: int, page_size: int) -> Dict:
        """Return page data
        
        Args:
            page: int 
            page_size: int
        """
        data = self.get_page(page, page_size)
        total_items = len(data)
        total_pages = total_items // page_size
        if total_items % page_size != 0:
            total_pages += 1
        page_data = {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': None,
                'prev_page': None,
                'total_pages': total_pages
        }
        return page_data
