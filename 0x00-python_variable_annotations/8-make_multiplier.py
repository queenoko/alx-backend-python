#!/usr/bin/env python3
"""This is the Type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """...Returns a function that multiplies the float"""
    return lambda x: x * multiplier
