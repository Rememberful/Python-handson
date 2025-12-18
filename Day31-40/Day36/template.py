# ================================
# GETTERS & SETTERS — COMPLETE TEMPLATE
# ================================

class Person:
    def __init__(self, name, age):
        self.name = name          # Public attribute (can be accessed directly)
        self._country = "India"   # Protected attribute (by convention)
        self.__age = age          # Private attribute (name mangling)

    # --------------------------------
    # 1. GETTER using @property
    # --------------------------------
    # Allows reading a private attribute
    # Accessed like a normal variable
    @property
    def age(self):
        return self.__age

    # --------------------------------
    # 2. SETTER using @property_name.setter
    # --------------------------------
    # Allows controlled modification of a private attribute
    @age.setter
    def age(self, value):
        # Validation logic
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value

    # --------------------------------
    # 3. READ-ONLY PROPERTY (no setter)
    # --------------------------------
    # Can be read but NOT modified
    @property
    def country(self):
        return self._country

    # --------------------------------
    # 4. DELETER (optional but important)
    # --------------------------------
    # Controls what happens when an attribute is deleted
    @age.deleter
    def age(self):
        print("Deleting age...")
        del self.__age


# ================================
# USAGE
# ================================

p = Person("Alice", 25)

# Getter usage (looks like attribute access)
print(p.age)            # 25

# Setter usage (looks like assignment)
p.age = 30
print(p.age)            # 30

# Validation in setter
# p.age = -5            # Raises ValueError

# Read-only property
print(p.country)        # India
# p.country = "USA"     # ❌ AttributeError (no setter)

# Deleter
del p.age               # Calls deleter method
# print(p.age)          # ❌ AttributeError (age deleted)


# ================================
# IMPORTANT NOTES
# ================================

# 1. @property makes methods behave like attributes
# 2. Private attributes use double underscore (__age)
# 3. Validation logic belongs in setters
# 4. Read-only properties have only a getter
# 5. Deleters control attribute deletion
# 6. This approach is called "Pythonic Encapsulation"
