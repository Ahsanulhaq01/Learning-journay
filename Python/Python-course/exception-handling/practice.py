# n = int(input("Enter the Number"))

# try:
#   assert n %2 ==0
#   print("The number is even")
# except AssertionError as Ae:
#   print("The number is odd ",Ae)

class Noteven(Exception):
  """The Class will specify that the number is even or odd """
  pass

def iseven(n):
 
    if n%2==0:
      print("The number you entered is even ")
    else:
      raise Noteven("The number you entered is Odd")
  

try:
    n = int(input("Enter the number "))
    iseven(n)
except Noteven as Ne:
   print(Ne)
except ValueError as VE:
   print("Opertion can be perform only on integer")
