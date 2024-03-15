import multiprocessing
import random
import time

arr = [random.randint(1, 100) for _ in range(1000000)]

def calculate_sum(start, end, results):
    total = sum(arr[start:end])
    results.value += total

start_time = time.time()

processes = []
chunk_size = len(arr) // 10
results = multiprocessing.Value('i', 0)

for i in range(10):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < 9 else len(arr)
    process = multiprocessing.Process(target=calculate_sum, args=(start, end, results))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

total_sum = results.value

end_time = time.time()

print("Сумма элементов массива:", total_sum)
print("Время выполнения (многопроцессорность):", end_time - start_time, "секунд")
