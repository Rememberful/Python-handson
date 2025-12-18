# x = 4
# def greet():
#     x= 5
#     print(x)
# greet()

x = 10
def change():
    global x
    x = 20
    print(x)
    x = 30
    print(x)
change()
