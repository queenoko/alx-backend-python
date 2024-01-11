#!/usr/bin/env python3
"""This Type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Accepts a mixed list of integers and floats and returns
    their sum as float"""
    y: float = 0.0
    for z in mxd_lst:
        y += z
    return y
