#!/usr/bin/env python3
"""Module that defines an async comprehension coroutine.

This module imports async_generator and defines a coroutine
that collects 10 random numbers using an asynchronous
comprehension.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of 10 random floats from async_generator.

    Uses an asynchronous comprehension to iterate over
    async_generator and collect the yielded values.
    """
    return [number async for number in async_generator()]
