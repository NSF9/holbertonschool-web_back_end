#!/usr/bin/env python3
import asyncio
import random

"""async / await"""

async def wait_random(max_delay: int = 5) -> float:
    """Wait for a random amount of time between 1 and max_delay seconds."""
    wait_time = random.uniform(1, max_delay)
    print(f"Waiting for {wait_time:.2f} seconds...")
    await asyncio.sleep(wait_time)
    print("Done waiting!")