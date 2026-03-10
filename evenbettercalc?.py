#def choice():
#   operators = ['+','-','*','/']
 #   for i in operators:
  #      print(i)
   # choose = input("\n Eneter the operator from the list above : ")
#
 #   if choose in operators:
  #      return choose
   # else :
    #    print("Put on your Glasses, Buddy.")    

#def calc():
 #   try :
  #      x = float(input("Enter your 1st no. : "))
   #     y = float(input("Enter your 2nd no. : "))
    #    
     #   decision = choice()
#
 #       if decision == "+":
  #          print(x+y)
   #     elif decision == "-":
    #        print(x-y)
     #   elif decision == "*":
      #      print(x*y)
       # elif decision == "/":            
        #    print(x/y)
        #else:
         #   print("Enter a valid charecter : ")
        
    #except ValueError:
     #       print("Enter a valid number.")
    #except ZeroDivisionError:
     #       print("Someone, among us, tried divind from 0. And it wasn't me.")

#calc()

# Let's make this better even betttteerrrrrrrrr !!!

def choice():
    operators = ['+','-','*','/']
    for i in operators:
        print(i)
    
    while True :
        choose = input("\n Eneter the operator from the list above : ")
        if choose in operators:
            return choose
        else :
            print("Put on your Glasses, Buddy. And Try Again.")    

def reps():
    while True:
        try :
            nor = int(input("Enter the total digits you wanna use in the calculation : ")) # nor = no. of repeteiton ,, or sth like that
            if nor<2:
                print("You need atleast 2 digits to do maths, buddy.")
            else:
                return nor    
        except ValueError:
            print("Enter an integer.")

def calc():
    try :
        n = reps() # n is just the toat no. for calculations here.
        x = float(input("Enter your 1st no. : "))
        
        for i in range(1,n):
            decision = choice()
            other_no = float(input(f"Enter your {i+1} no. : "))

            if decision == '+':
                x += other_no
            elif decision == '-':
                x -= other_no
            elif decision == '*':
                x *= other_no
            elif decision == '/':
                x /= other_no
        print(f"Result : {x}")       
    except ValueError:
            print("Enter a valid number.")
    except ZeroDivisionError:
            print("Someone, among us, tried divind from 0. And it wasn't me.")

calc()

#apparently, while the logic is great, but if someone fumbled up 9th out 0f 10 digits, the code crasehes, and its irritating to restart............
#but this issss even betterrrrr then the better i last made.
#next will just shift to UI instead of going writing while true/ try except for every single  if block of code in the for loop for accumlated claculation.