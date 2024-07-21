#!/usr/bin/env python3
"""
This file contains a function that calculates the pages sent through
pagination
"""
from typing import Tuple, List
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
