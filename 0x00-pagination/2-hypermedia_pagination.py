#!/usr/bin/env python3
"""Simple Pagination"""
import csv
import math
from typing import List

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
        """Retrieve the required page rows"""
        assert(isinstance(page, int))
        assert(page > 0)
        assert(isinstance(page_size, int))
        assert(page_size > 0)
        start, end = index_range(page, page_size)
        data = (self.dataset()[start:end] if len(self.dataset()[start:])
                >= page_size else self.dataset()[start:])
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a dictionary of hypermedia metadata"""
        data = self.get_page(page, page_size)
        total = len(self.dataset()) / page_size
        if total - int(total) > 0.0001:
            total = int(total) + 1
        else:
            total = int(total)
        meta_data = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": (page + 1 if len(self.get_page(page + 1, page_size))
                          > 0 else None),
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total
        }
        return meta_data
