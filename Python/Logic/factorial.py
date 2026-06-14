fact = 1
def factorial(n):
  global fact
  if n>0:
    fact = fact * n
    factorial(n-1)
  return fact

value = factorial(10)
print(f"The factorial of 5 is : {value}")