import numpy as np

arr = np.arange(16,32).reshape(4,4)  #4 x 4 array 
arr1 = np.arange(2,18).reshape(4,4)
# print(arr)
# print(arr1)

# print(arr1.dot(arr))
#************************************************

#question 3 
 
# arr = [2,3,4,4,5,4,2,1,5,8]

# mean of it 

# print(np.mean(arr))

# Median 

# print(np.median(arr))

# standard Deviation 
# print(np.std(arr))

#*******************************************

#question no 4 :

# arr = np.arange(0,25).reshape(5,5)
# print(arr)
# print(arr[1:4,1:4])


#question no 5

# arr5 = np.array([[1,2,3],[4,5,6]]).reshape(3,2)
# print(arr5)

# print(np.ravel(arr5))

#question 6 

# arr6 = np.identity(5)
# print(arr6)

#question 7 :
# arr7a = [1,2,3,4,5]
# arr7b = [6,7,8,9,10]

# print(np.vstack((arr7a,arr7b)))
# print()
# print(np.hstack((arr7a,arr7b)))

#question 8:

# arr8 = np.arange(42,62)

# for i in arr8:
#   if(i>50):
#     print(i,end=",")

#question 9

# arr9  = np.arange(-5,5)

# for i in arr9:
#   if(i<0):
#     i = 0
#   print(i)

#question 10 ;

# arr10 = np.arange(9).reshape(3,3)

# for i in arr10:
#   print(i+5)

#question 11 catch division error

# def division(a,b):
#   return a/b

# try:
#   division(2,0)
# except ZeroDivisionError as ze:
#   print("Dinomanator must be greater than  zero")
# except NameError as ve:
#   print("value must be numeric ")

#question 12 :

# def openfile():
#   f = open("data.txt","r")
#   print("Element is successfully open ")
#   f.close()

# try:
#   openfile()
# except FileNotFoundError as FN:
#   print("The file not exist")

#question 13 :

# try:
#   num = int(input("Enter number :"))
#   if(num<0):
#     raise ValueError("Negative are not allowed ")
  
# except ValueError as ve:
#   print(ve)


#question 14 :

# a = int(input("Enter the first Number"))
# b = int(input("Enter the 2nd number "))

# try:
#   print(f"The divsion is equal to : {a/b}")
# except ZeroDivisionError as ze:
#   print("Denominator must be greater than zero ")
# except NameError as ne:
#   print("Only integar are allowed ")

# else:
#   print("Divsion successful ")

# finally:
#   print("Program ended")

#question 15

# class SmallNumberError(Exception):
#   """raise error if the number is less than 5"""
#   pass

# num = int(input("Enter the number"))
# try:
#   if(num<5):
#     raise Exception("Number is less than 5 ")
# except SmallNumberError:
#   print(SmallNumberError)
# else:
#   print("The number is greater than 5")