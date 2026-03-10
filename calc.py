def a(x,y):
    return x+y
def s(x,y):
    return x-y
def m(x,y):
    return x*y
def d(x,y):
    return x/y

x = int(input("Enter Your 1st Digit :"))
y = int(input("Enter Your 2nd Digit :"))
c = input("Enter your Operetor: ")

try:
    if   c == "+":
        print(a(x,y))
    elif c == "-":
        print(s(x,y))
    elif c == "*":
        print(m(x,y))
    elif c == "/":
        print(d(x,y))
    else :
        print("Eneter a valid operator [=,-,*,/]")
except:
    if c == "//" or c == "**" or c == "%" :
        print("The operators : [// , % , **] are not yet included.")