# Iterable examples
items = ["apple", "banana", "cherry"]

print("Basic enumerate (default start=0):")
for index, item in enumerate(items):
    print(index, item)

print("\nEnumerate with custom start index:")
for index, item in enumerate(items, start=1):
    print(index, item)

print("\nEnumerate with string:")
word = "Python"
for index, char in enumerate(word):
    print(index, char)

print("\nEnumerate converted to list:")
enum_list = list(enumerate(items))
print(enum_list)

print("\nEnumerate tuple unpacking:")
for pair in enumerate(items):
    print(pair)  # (index, value)
