# def greet(name="User"):
#     print("Hello", name)

# greet() # Default greeting
# greet("Aditya") # Personalized greeting

# def avergge(a=9, b=1):
#     print("The average is:", (a + b) / 2)

# avergge() # Default average
# avergge(5, 15) # Custom average
# avergge(20) # Custom average with one default value of b
# avergge(b=30) # Custom average with one default value of a

# def info(name, age):
#     print(name, age)

# info(age=21, name="Aditya")
# info("Aditya", 21)

# def greet(name):
#     print("Hello,", name)
# greet("Alice") # Correct usage with one argument
# greet() # Incorrect usage, will raise TypeError

#variable length arguments
# def average(*numbers):
#     if len(numbers) == 0:
#         print("No numbers provided.")
#         return
#     total = sum(numbers)
#     avg = total / len(numbers)
#     print("The average is:", avg)
# average(10, 20, 30) # Average of three numbers
# average(5, 15) # Average of two numbers
# average() # No numbers provided

# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
# show_info(name="Alice", age=25, city="New York")

# def average(a, b):
#     return (a + b) / 2

# result = average(10, 20)
# print(result)

def average(a, b):
    avg = (a + b) / 2
    print(avg)
average(10, 20)




