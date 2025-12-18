# def decorator(func):
#     def wrapper():
#         print("Before calling the function")
#         func()  # Call the original function
#         print("After calling the function")
#     return wrapper
# def say_hello():
#     print("Hello!")
# # Decorating manually
# decorated_function = decorator(say_hello)
# decorated_function()

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
