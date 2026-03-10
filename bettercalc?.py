def calc():
    try :
        x = int(input("Enter your 1st no. : "))
        y = int(input("Enter your 2nd no. : "))
        c = input("Enter the operator: ")

        if c == "+":
            print(x+y)
        elif c == "-":
            print(x-y)
        elif c == "*":
            print(x*y)
        elif c == "/":            
            print(x/y)
        else:
            print("Enter a valid charecter : ")
        
    except ValueError:
            print("Enter a valid number.")
    except ZeroDivisionError:
            print("Someone, among us, tried divind from 0. And it wasn't me.")

calc()