# 

# import sys
# print(sys.argv)

# import sys
# if len(sys.argv) < 2:
#     print("Usage: python hello.py <name>")
#     sys.exit(1)
# name = sys.argv[1]
# print(f"Hello, {name}!")

import argparse
parser = argparse.ArgumentParser(description="Simple greeting utility")
parser.add_argument("name", help="Name of the person to greet")
args = parser.parse_args()
print(f"Hello, {args.name}!")


