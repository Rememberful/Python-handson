# =====================================================
# ACCESS MODIFIERS IN PYTHON — COMPLETE TEMPLATE
# =====================================================

class Parent:
    def __init__(self):
        # -------------------------------
        # PUBLIC ATTRIBUTE
        # Accessible from anywhere
        # -------------------------------
        self.public_var = "I am public"

        # -------------------------------
        # PROTECTED ATTRIBUTE (Convention)
        # Single underscore (_)
        # Accessible inside class and subclasses
        # Not enforced by Python
        # -------------------------------
        self._protected_var = "I am protected"

        # -------------------------------
        # PRIVATE ATTRIBUTE (Name Mangling)
        # Double underscore (__)
        # Accessible ONLY inside this class
        # -------------------------------
        self.__private_var = "I am private"

    # --------------------------------
    # PUBLIC METHOD
    # --------------------------------
    def public_method(self):
        print("Public method")
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)

    # --------------------------------
    # PROTECTED METHOD
    # --------------------------------
    def _protected_method(self):
        print("Protected method")

    # --------------------------------
    # PRIVATE METHOD
    # --------------------------------
    def __private_method(self):
        print("Private method")

    # --------------------------------
    # PUBLIC METHOD accessing PRIVATE method
    # (Best practice)
    # --------------------------------
    def access_private_method(self):
        self.__private_method()


# =====================================================
# CHILD CLASS (INHERITANCE)
# =====================================================

class Child(Parent):
    def __init__(self):
        super().__init__()

    def access_members(self):
        print("\n--- Inside Child Class ---")

        # Public member → Accessible
        print(self.public_var)

        # Protected member → Accessible (intended)
        print(self._protected_var)

        # Private member → NOT directly accessible
        # print(self.__private_var)  # ❌ ERROR

        # Name mangling workaround (NOT recommended)
        print(self._Parent__private_var)


# =====================================================
# OUTSIDE THE CLASS
# =====================================================

obj = Parent()

print("\n--- Outside Class ---")

# Public → Accessible
print(obj.public_var)

# Protected → Accessible but discouraged
print(obj._protected_var)

# Private → NOT accessible
# print(obj.__private_var)  # ❌ ERROR

# Name mangling access (discouraged)
print(obj._Parent__private_var)

# Methods
obj.public_method()           # Allowed
obj._protected_method()       # Allowed (discouraged)
# obj.__private_method()      # ❌ ERROR
obj.access_private_method()   # Allowed


# =====================================================
# IMPORTANT NOTES
# =====================================================

"""
1. Python does NOT enforce access control.
2. Public members have no underscore.
3. Protected members use single underscore (_).
4. Private members use double underscore (__).
5. Private members use name mangling: _ClassName__member
6. Protected members are inherited normally.
7. Private members are NOT directly inherited.
8. Use getters/setters (@property) for controlled access.
9. These are conventions — Python trusts the developer.
"""
