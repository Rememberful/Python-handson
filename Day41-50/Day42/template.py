"""
MAGIC / DUNDER METHODS IN PYTHON
===============================

This single file demonstrates:
- Object creation
- String representation
- Operator overloading
- Comparison operators
- Container behavior
- Attribute handling
- Callable objects
- Context manager
"""

# --------------------------------------------------
# MAIN CLASS USING MAGIC METHODS
# --------------------------------------------------

class Book:
    # 1. Object creation
    def __new__(cls, *args, **kwargs):
        print("__new__ called (object created)")
        return super().__new__(cls)

    def __init__(self, title, pages):
        print("__init__ called (object initialized)")
        self.title = title
        self.pages = pages

    # 2. String representation
    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    # 3. Operator overloading
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

    # 4. Comparison operators
    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    # 5. Container behavior
    def __len__(self):
        return self.pages

    def __getitem__(self, index):
        return self.title[index]

    # 6. Attribute handling
    def __getattr__(self, name):
        return f"Attribute '{name}' not found"

    def __setattr__(self, name, value):
        print(f"Setting attribute {name} = {value}")
        super().__setattr__(name, value)

    # 7. Callable object
    def __call__(self):
        return f"Reading '{self.title}'"

    # 8. Context manager
    def __enter__(self):
        print("Opening book")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing book")
        return False


# --------------------------------------------------
# USING THE MAGIC METHODS
# --------------------------------------------------

print("\n--- Object Creation ---")
b1 = Book("Python Basics", 300)
b2 = Book("Advanced Python", 450)

print("\n--- String Representation ---")
print(b1)            # __str__
print(repr(b1))      # __repr__

print("\n--- Operator Overloading ---")
print("Total pages:", b1 + b2)

print("\n--- Comparison ---")
print("Same pages?", b1 == b2)
print("b1 < b2?", b1 < b2)

print("\n--- Container Behavior ---")
print("Length of book:", len(b1))
print("First letter of title:", b1[0])

print("\n--- Attribute Handling ---")
print(b1.author)     # __getattr__

print("\n--- Callable Object ---")
print(b1())          # __call__

print("\n--- Context Manager ---")
with b1 as book:
    print(book)

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
"""
KEY POINTS:
----------
✔ Magic methods start & end with __
✔ Automatically called by Python
✔ Enable operator overloading
✔ Customize object behavior
✔ Make classes powerful & pythonic
"""
