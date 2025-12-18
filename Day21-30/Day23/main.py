# try:
#     x = 10 / 0
# except:
#     print("An error occurred")

# a = input("Enter the number:")
# try: 
#     print(f"Multiplication table of {int(a)} is: ")
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Sorry some error occured.")

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# try:
#     a = int(input("Enter a number: "))
#     b = 10 / a
# except ValueError:
#     print("Please enter a valid integer")
# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("This will always execute")

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Error occurred")
# finally:
#     print("This will still execute")

# try:
#     file = open("data.txt", "r")
#     print(file.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     file.close()




