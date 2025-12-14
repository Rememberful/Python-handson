# ---------- TAKING USER INPUT ----------

# input() always takes data as a STRING
name = input("Enter your name: ")
print("Hello,", name)

# ---------- TYPECASTING (CONVERTING DATA TYPES) ----------

# Taking number input (string → int)
age = int(input("Enter your age: "))
print("Your age is:", age)
print("Type of age:", type(age))

# Taking decimal number (string → float)
height = float(input("Enter your height in meters: "))
print("Your height is:", height)
print("Type of height:", type(height))

# ---------- STRING TYPECASTING ----------

# Converting numbers to string
age_str = str(age)
print("Age as string:", age_str)
print("Type of age_str:", type(age_str))

# ---------- USING TYPECASTING IN CALCULATIONS ----------

# Without typecasting (will cause error)
# result = age + "5"   ❌ Error

# With typecasting
result = age + int("5")
print("Age after 5 years:", result)

# ---------- BOOLEAN TYPECASTING ----------

# bool() conversion
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Hello"))  # True

# ---------- MULTIPLE INPUTS ----------

# Taking multiple values in one line
x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)

print("Sum:", x + y)

# ---------- SUMMARY ----------
# input() → always returns string
# int(), float(), str(), bool() → used for typecasting
