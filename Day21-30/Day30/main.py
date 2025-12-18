# 
# file = open("sample.txt", "r")
# content = file.read(10)   # Reads first 10 characters
# print(content)
# file.close()

# file = open("sample.txt", "r")
# line1 = file.readline()
# line2 = file.readline()
# print(line1)
# print(line2)
# file.close()

# file = open("sample.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()

# with open("sample.txt", "r") as file:
#     print(file.tell())


with open("sample.txt", "r") as file:
    file.seek(0)   # Move to start
    print(file.read())


