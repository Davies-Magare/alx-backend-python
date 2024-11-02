#!/usr/bin/env python3

"""
This module demonstrates how to create
an asynchronous task using asyncio library
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a coroutine Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
