#!/usr/bin/env python3

"""
Collect 10 numbers using async
comprehension
"""

from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async
    comprehensing
    """

    result = []
    async for i in async_generator():
        result.append(i)
    return result
