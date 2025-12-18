import functools

def decorator(func):
    @functools.wraps(func)   # preserves function name, docstring, etc.
    def wrapper(*args, **kwargs):  # accepts any arguments
        print("Before function call")

        result = func(*args, **kwargs)  # call original function

        print("After function call")
        return result  # return the original function's result

    return wrapper


@decorator
def example_function(name, age):
    """This is an example function."""
    print(f"Name: {name}, Age: {age}")
    return "Function completed"


# Function call
output = example_function("Alice", 25)

print("Returned value:", output)
print("Function name:", example_function.__name__)
print("Docstring:", example_function.__doc__)
