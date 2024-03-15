import threading
import random
import time

arr = [random.randint(1, 100) for _ in range(1000000)]

def calculate_sum(start, end, results):
    total = sum(arr[start:end])
    results.append(total)

start_time = time.time()

threads = []
chunk_size = len(arr) // 10
results = []

for i in range(10):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < 9 else len(arr)
    thread = threading.Thread(target=calculate_sum, args=(start, end, results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

total_sum = sum(results)

end_time = time.time()

print("Сумма элементов массива:", total_sum)
print("Время выполнения (многопоточность):", end_time - start_time, "секунд")
