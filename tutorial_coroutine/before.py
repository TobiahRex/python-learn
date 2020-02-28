"""
https://realpython.com/lessons/what-are-python-coroutines/

Coroutine is like a generator
- Start/stop/return values.
Coroutine is different from a generator
- generators produce values
- coroutines consume values

async tasks, require an EventLoop to consume the coroutine's that
are generated. 
"""
from random import randint
import time
import asyncio
import timeit

async def get_random_nums():
    await asyncio.sleep(3)
    rand_num = randint(0, 10)
    print(f'num: {rand_num}')

async def main():
    async_tasks = [
        get_random_nums(),
        get_random_nums(),
        get_random_nums(),
    ];
    (data, pending) = await asyncio.wait(async_tasks)
    
    for task in data:
        print(f'task {task}')


if __name__ == '__main__':
    asyncio.run(main())
