#!/usr/bin/env python3

"""
File with a basic python coroutine
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for max_delay seconds and then return the delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
