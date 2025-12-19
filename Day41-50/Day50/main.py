# # import asyncio
# # async def say_hello():
# #     print("Hello")
# #     await asyncio.sleep(1)
# #     print("World")
# # asyncio.run(say_hello())

# # import time
# # def task(n):
# #     time.sleep(2)
# #     print(f"Task {n} done")
# # task(1)
# # task(2)

# # import asyncio
# # async def task(n):
# #     await asyncio.sleep(2)
# #     print(f"Task {n} done")
# # async def main():
# #     await asyncio.gather(
# #         task(1),
# #         task(2)
# #     )
# # asyncio.run(main())

# import asyncio
# # async def fetch_data(n):
# #     print(f"Fetching {n}")
# #     await asyncio.sleep(2)
# #     return f"Result {n}"
# # async def main():
# #     results = await asyncio.gather(
# #         fetch_data(1),
# #         fetch_data(2),
# #         fetch_data(3)
# #     )
# #     print(results)
# # asyncio.run(main())



# import threading
# import time
# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#         time.sleep(1)
# # Create thread
# t = threading.Thread(target=print_numbers)
# # Start thread
# t.start()
# # Wait for thread to finish
# t.join()
# print("Thread finished")

# import threading
# import time
# def task(n):
#     print(f"Task {n} starting")
#     time.sleep(2)
#     print(f"Task {n} finished")
# threads = []
# for i in range(3):
#     t = threading.Thread(target=task, args=(i,))
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()

# import multiprocessing
# def worker(name):
#     print(f"Worker {name} is running")
# if __name__ == "__main__":
#     p = multiprocessing.Process(target=worker, args=("Alice",))
#     p.start()  # start the process
#     p.join()   # wait for it to finish


# import multiprocessing
# import time
# def task(n):
#     print(f"Task {n} started")
#     time.sleep(2)
#     print(f"Task {n} finished")
# if __name__ == "__main__":
#     processes = []
#     for i in range(3):
#         p = multiprocessing.Process(target=task, args=(i,))
#         processes.append(p)
#         p.start()
#     for p in processes:
#         p.join()

# import multiprocessing
# def worker(q):
#     q.put("Hello from worker")
# if __name__ == "__main__":
#     q = multiprocessing.Queue()
#     p = multiprocessing.Process(target=worker, args=(q,))
#     p.start()
#     print(q.get())  # receive data from worker
#     p.join()

from multiprocessing import Process, Manager
def worker(d):
    d["name"] = "Alice"
if __name__ == "__main__":
    with Manager() as manager:
        shared_dict = manager.dict()
        p = Process(target=worker, args=(shared_dict,))
        p.start()
        p.join()
        print(shared_dict)  # {'name': 'Alice'}





