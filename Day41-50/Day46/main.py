# import time
# print(time.ctime())

# import time
# t = time.localtime()
# formatted = time.strftime("%d-%m-%Y %H:%M:%S", t)
# print(formatted)
import time
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print("Execution time:", end - start)




