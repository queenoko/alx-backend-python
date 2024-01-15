#!/usr/bin/env python3
"""This will execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This will spawns wait_random n times with the specified max_delay
    and returns the list of all the delays (float values)."""
    later = [wait_random(max_delay) for _ in range(n)]
    later = asyncio.as_completed(later)
    delays = [await future for future in later]
    return delays
