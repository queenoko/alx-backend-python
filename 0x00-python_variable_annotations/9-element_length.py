#!/usr/bin/env python3
"""This is the Type-annotated function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """...Returns a list of tuples of sequence and int"""
    return [(z, len(z)) for z in lst]
