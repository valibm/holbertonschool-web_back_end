#!/usr/bin/env python3
"""
Multiple coroutines at the same time with async
"""
import asyncio
from typing import List
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async routine that takes in 2 int arguments.
    """
    l = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(l)]
    return finish
