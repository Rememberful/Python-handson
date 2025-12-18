# age = -5
# if age < 0:
#     raise ValueError("Age cannot be negative")

# age = -10
# if age < 0:
#     raise InvalidAgeError("Invalid age provided")


class InvalidAgeError(Exception):
    pass
try:
    age = -10
    if age < 0:
        raise InvalidAgeError("Invalid age provided")
except InvalidAgeError as e:
    print("Custom Error:", e)


