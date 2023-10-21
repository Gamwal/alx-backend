#!/usr/bin/env python3
"""
Simple helper function
"""


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
