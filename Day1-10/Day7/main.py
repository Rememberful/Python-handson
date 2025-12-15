# x = int(input("Enter a number: "))
# match x:
#     case 0:
#         print("Zero")
#     case 1:
#         print("One")


day = "Y"

match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("End of week")
    case _:
        print("Normal day")
