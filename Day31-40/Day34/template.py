# Python Constructor Example Covering All Key Points

class Example:
    # Default constructor
    def __init__(self, x=None, y=None):
        if x is not None and y is not None:
            # Parameterized constructor behavior
            self.x = x
            self.y = y
            print(f"Parameterized constructor called: x={self.x}, y={self.y}")
        else:
            # Default constructor behavior
            self.x = 0
            self.y = 0
            print(f"Default constructor called: x={self.x}, y={self.y}")

    # Regular method for comparison
    def show(self):
        print(f"Values are x={self.x}, y={self.y}")

# Creating objects using different ways

# 1. Using default constructor
obj1 = Example()  # Default constructor is called
obj1.show()

# 2. Using parameterized constructor
obj2 = Example(10, 20)  # Parameterized constructor is called
obj2.show()

# 3. Using "simulated overloading" with default arguments
obj3 = Example(5)  # Only x provided, y defaults to None -> default values used
obj3.show()
