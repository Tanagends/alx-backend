#!/usr/bin/env python3
"""Defines a function index_range that takes two integer arguments
   page and page_size.

   The function should return a tuple of size two containing a start
   index and an end index corresponding to the range of indexes to
   return in a list for those particular pagination parameters.

   Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end index"""
    start_idx: int = (page - 1) * page_size
    end_idx: int = start_idx + page_size
    return start_idx, end_idx
