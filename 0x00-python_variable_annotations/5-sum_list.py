#!/usr/bin/env python3
"""This Type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and returns their sum as float"""
    y: float = 0.0
    for z in input_list:
        y += z
    return y
