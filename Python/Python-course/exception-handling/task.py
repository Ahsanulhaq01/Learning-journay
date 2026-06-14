
# def compute():
#   try:
#     num  = int(input("Enter a number"))

#     result = 100/num
#     print(f"Result:{result}")
#   except ZeroDivisionError :
#     print("input value cannot by zero ")
#   except ValueError:
#     print("Only integer are valid !")

# compute()

# def read_file():
#   try:
#     filename = open('prog1.py','r')
    
#     print(filename)

#   except FileNotFoundError:
#     print("file is not found")
#   except Exception as e:
#     print("An error occured : " , e)

# read_file()
import math
class WrongPin(Exception):
  """Raised when Pin is inorrect""" #doc string
  pass

# def incorrectpin(pin):
#   code = 1234
#   try:
#     if code == pin:
#       print("transication Successful")
#     else:
#       raise WrongPin("you enter the wrong Password")
#   except WrongPin as Wp:
#     print(Wp)
    

# pin = int(input("Enter Your Pin"))

# incorrectpin(pin)

# print(WrongPin.__doc__)
print(math.__dict__)

