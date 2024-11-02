#!/usr/bin/env python3

"""
This module demonstrates how to run multiple
coroutines at the same time with async
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def qsrt(arr):
    """Sort the list with qsort"""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return qsrt(left) + [pivot] + qsrt(right)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run multiple coroutines."""

    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    results = await asyncio.gather(*tasks)
    return qsrt(results)
