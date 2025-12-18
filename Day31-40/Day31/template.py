"""
=========================================
PYTHON FUNCTIONAL PROGRAMMING TEMPLATE
Covers:
- lambda functions
- map()
- filter()
- reduce()
- individual + combined usage
=========================================
"""

# -------------------------------
# 1️⃣ SAMPLE DATA
# -------------------------------
numbers = [1, 2, 3, 4, 5, 6]
names = ["Alice", "Bob", "Charlie", "David"]

# -------------------------------
# 2️⃣ LAMBDA FUNCTION
# -------------------------------
# Anonymous (one-line) function
# Syntax: lambda arguments: expression

square = lambda x: x * x
print("Lambda square:", square(5))  # Output: 25


# -------------------------------
# 3️⃣ MAP FUNCTION
# -------------------------------
# Applies a function to EACH element
# Syntax: map(function, iterable)
# Returns: map object (convert to list)

squared_numbers = map(lambda x: x * x, numbers)
print("Map (square):", list(squared_numbers))


# -------------------------------
# 4️⃣ FILTER FUNCTION
# -------------------------------
# Filters elements based on condition
# Syntax: filter(function, iterable)
# Function must return True/False

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Filter (even):", list(even_numbers))


# -------------------------------
# 5️⃣ REDUCE FUNCTION
# -------------------------------
# Reduces iterable to SINGLE value
# Must be imported from functools
# Syntax: reduce(function, iterable)

from functools import reduce

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Reduce (sum):", sum_of_numbers)


# -------------------------------
# 6️⃣ MAP + FILTER COMBINATION
# -------------------------------
# Square ONLY even numbers

even_squared = map(
    lambda x: x * x,
    filter(lambda x: x % 2 == 0, numbers)
)
print("Map + Filter:", list(even_squared))


# -------------------------------
# 7️⃣ MAP + FILTER + REDUCE
# -------------------------------
# Sum of squares of even numbers

result = reduce(
    lambda x, y: x + y,
    map(lambda x: x * x,
        filter(lambda x: x % 2 == 0, numbers))
)
print("Map + Filter + Reduce:", result)


# -------------------------------
# 8️⃣ MAP WITH STRINGS
# -------------------------------
# Convert names to uppercase

upper_names = map(lambda name: name.upper(), names)
print("Map (strings):", list(upper_names))


# -------------------------------
# 9️⃣ FILTER WITH STRINGS
# -------------------------------
# Names longer than 4 characters

long_names = filter(lambda name: len(name) > 4, names)
print("Filter (strings):", list(long_names))


# -------------------------------
# 🔟 KEY TAKEAWAYS (COMMENTS)
# -------------------------------
"""
✔ lambda → small anonymous function
✔ map    → transforms data
✔ filter → selects data
✔ reduce → combines data into one value
✔ map/filter return iterators → use list()
✔ reduce returns a single value
✔ Prefer list comprehension for readability in real projects
"""
