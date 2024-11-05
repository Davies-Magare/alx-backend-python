#!/usr/bin/env python3

"""
A coroutine that yields a random
number between 0 and 10
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> typing.Generator[float, None, None]:
    """Generate a random number between 0 to 10"""

    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
