# FUNCTION
#block of statment that perform specfic task,but here we are doing more thing (multiple task)  for this we use (HIGH ORDER FUNCTION (i.e :built in function HOF(MAP,reduce and filter)) basically use lambda or regular function with help of it they perfom varios opertion or behavoir on input  using helper ftn and they might be lambda ftn )
#
#               CODE
# greet = lambda i :"even" if i%2==0 else "odd"
# print(greet(31))

#               CODE 
# lst = [1,2,3,4,5,6,3,3,4,5,5,6,4,3]
# def return_sum(lst):  #def is used to define the function 
#     evens = 0
#     odd = 0
#     div3_ = 0
    
#     for i in lst:
#         if i %2==0:
#             print(i,end="")
#         if i%


#SYNTAX OF HOF 
    #expect ftn and iterable (two argument the first one is ftn and other is iterable (everything which obey loop))

# lst = [1,2,3,4,5,6,7,8,9,10]
# def return_sum(func,lst):
#     return lst

# x = lambda x : x%2==0

# y = lambda y : y%2!=0

# z = lambda z : z%3==0

# print(return_sum(x,lst))

# result = lambda :1 * 2 * 2
# print(result()) :1 * 2 * 2
# print(result())

# student = [{'name':'Jhon','age':30},{'name':'ahsan','age':21}]
# print(student)
# student.sort(key = lambda x : x['age'])

# print(student)

# function to find the factorial of the number 
from functools import reduce
n = int(input("Enter the number : "))

fact = reduce(lambda x,y:x*y,range(1,n + 1))
print(fact)
