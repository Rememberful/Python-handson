"""
Concurrency Template in Python
- Multithreading
- Multiprocessing
- AsyncIO
"""

import time
import threading
import multiprocessing
import asyncio

# -------------------------------
# 1. TASK FUNCTION
# -------------------------------

def cpu_task(n):
    """Simulate a CPU-bound task"""
    print(f"[CPU Task] Start {n}")
    result = sum(i*i for i in range(10**6))
    print(f"[CPU Task] Done {n}")
    return result

def io_task(n):
    """Simulate an I/O-bound task"""
    print(f"[IO Task] Start {n}")
    time.sleep(2)
    print(f"[IO Task] Done {n}")

async def async_io_task(n):
    """Async version of I/O task"""
    print(f"[Async Task] Start {n}")
    await asyncio.sleep(2)
    print(f"[Async Task] Done {n}")


# -------------------------------
# 2. MULTITHREADING EXAMPLE
# -------------------------------

def run_multithreading():
    print("\n--- Multithreading Example ---")
    threads = []
    for i in range(3):
        t = threading.Thread(target=io_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# -------------------------------
# 3. MULTIPROCESSING EXAMPLE
# -------------------------------

def run_multiprocessing():
    print("\n--- Multiprocessing Example ---")
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=cpu_task, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


# -------------------------------
# 4. ASYNCIO EXAMPLE
# -------------------------------

async def run_asyncio():
    print("\n--- AsyncIO Example ---")
    tasks = [async_io_task(i) for i in range(3)]
    await asyncio.gather(*tasks)


# -------------------------------
# 5. MAIN ENTRY POINT
# -------------------------------

if __name__ == "__main__":
    start = time.time()

    # Run I/O-bound tasks using threads
    run_multithreading()

    # Run CPU-bound tasks using processes
    run_multiprocessing()

    # Run async tasks
    asyncio.run(run_asyncio())

    end = time.time()
    print(f"\nTotal elapsed time: {end - start:.2f} seconds")
