#!/usr/bin/env python3

"""
Run async coroutines in parallel and measure
runtime.
"""

import asyncio
import time

asyn_compr = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run coroutines in parallel and measure runtime"""

    start = time.time()
    await asyncio.gather(*[asyn_compr(), asyn_compr(),
                           asyn_compr(), asyn_compr()])
    stop = time.time()

    return stop - start
