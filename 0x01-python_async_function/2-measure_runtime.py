#!/usr/bin/env python3

"""
This module contains code that measures the
run time of asynchronous coroutines
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure execution time of wait_n coroutine
    """

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    return elapsed_time / n
