def choice():
    operators = ['+','-','*','/']
    for i in operators:
        print(i)
    choose = input("\n Eneter the operator from the list above : ")

    if choose in operators:
        return choose
    else :
        print("Put on your Glasses, Buddy.")    

def calc():
    try :
        x = int(input("Enter your 1st no. : "))
        y = int(input("Enter your 2nd no. : "))
        
        decision = choice()

        if decision == "+":
            print(x+y)
        elif decision == "-":
            print(x-y)
        elif decision == "*":
            print(x*y)
        elif decision == "/":            
            print(x/y)
        else:
            print("Enter a valid charecter : ")
        
    except ValueError:
            print("Enter a valid number.")
    except ZeroDivisionError:
            print("Someone, among us, tried divind from 0. And it wasn't me.")

calc()