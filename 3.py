import asyncio
import random
import time

arr = [random.randint(1, 100) for _ in range(1000000)]

async def calculate_sum(start, end):
    total = sum(arr[start:end])
    return total

async def main():
    start_time = time.time()
    tasks = []
    chunk_size = len(arr) // 10

    for i in range(10):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < 9 else len(arr)
        task = asyncio.create_task(calculate_sum(start, end))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    total_sum = sum(results)

    end_time = time.time()

    print("Сумма элементов массива:", total_sum)
    print("Время выполнения (асинхронность):", end_time - start_time, "секунд")

asyncio.run(main())
