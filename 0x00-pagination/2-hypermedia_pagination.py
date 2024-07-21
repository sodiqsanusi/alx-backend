#!/usr/bin/env python3
"""
This file contains a function that calculates the pages sent through
pagination
"""
from typing import Tuple, List, Dict, Any
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Gets the start and end indexes for pagination
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        To make sure all methods have documentations
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Don't know how this is supposed to work yet, will check for more info
        """
        assert type(page_size) == int
        assert type(page) == int
        assert page > 0
        assert page_size > 0
        file_length = len(self.dataset())
        start_index, end_index = index_range(page, page_size)
        end_index = min(file_length, end_index)
        if start_index >= file_length:
            return []
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get values about next and previous pages and return it as a dictionary
        """
        data = self.get_page(page, page_size)
        r_page_size = len(data)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
                "page_size": r_page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
        }
