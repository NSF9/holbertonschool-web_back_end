#!/usr/bin/env python3
import asyncio
import random

"""async / await"""

async def wait_random(max_delay: int = 5) -> float:
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay