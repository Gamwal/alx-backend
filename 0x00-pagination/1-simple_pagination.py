#!/usr/bin/env python3
"""
Simple helper function
"""

import csv
import math
from typing import List


def index_range(page=None, page_size=None):
    """
    Simple helper function for pagination

    Args:
        page (int): page number (1-indexed)
        page_size(int): page size

    Returns:
        (start_index, end_index) (tuple): Range of indexes to return in a list
                                          for those particular pagination
                                          parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


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
        """
        class function to get pages
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        page_indices = index_range(page=page, page_size=page_size)
        try:
            return self.dataset()[page_indices[0]:page_indices[1]]
        except IndexError:
            return []
