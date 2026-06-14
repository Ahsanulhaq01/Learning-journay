from functools import reduce
#/////////////////////
# try:
#     value = input("enter a value")
#     print(value/value)
# except:
#     print("bad input...")
# except ZeroDivisionError:
#     print("very bad input...")
# except TypeError:
#     print("very very bad input..")
# except:
#having error in it
#     print("boo!")


#////////////////////////////
# class A:
#     def str(self):
#         return 'a'
# class B(A):
#     def str(self):
#         return 'b'
# class C(A,B):
#     pass

# obj = C()
#having error
# print(obj)

#///////////////////////

#code to print different cases in string:

# s = "Pakistan is our country 123"
# upper_count =lower_count=digit_count= special_count= 0
# for char in s:
#     if char.isupper():
#         upper_count+=1
#     elif char.islower():
#         lower_count +=1
#     elif char.isdigit():
#         digit_count+=1
#     else:
#         special_count+=1

# lst = [upper_count,lower_count,digit_count,special_count]

# for i in lst:
#     print(f"The character type as : {i}" )

# print(f"The uppercase char are: {upper_count}")
# print(f"The lowercase char are : {lower_count}")
# print(f"The digit  are : {digit_count}")
# print(f"The special char are : {special_count}")

#//////////////////////////////

#code to print tuple having age less than 25 :
# lst = [('alice',30,'HR'),('bob',25,"eng"),('charlie',35,'marketing')]

# young_employee =[lst[i] for i in range(len(lst)) if lst[i][1] <30]

# print(young_employee)

#/////////////////////////
#code to print GPA:
# student = {"henry":3.6,"clark":3.1,"joe":2.6,"tony":2.3}

# grae_mapper = lambda x : "A" if student.values()>3.5  "B" elif student.values() >3.0 and student.values()<3.5 "C" elif student.values() >=2.5 else "D"


# lst = dict(map(grae_mapper,student))

# print(lst)

#/////////////////////

#code to print sum and average of list number :

# lst =[1,2,3,4,5]
# sum = 0
# for i in lst:
#     sum += i

# aver = sum/len(lst)
# print(sum)
# print(aver)
#///////////////////////
#code to remove the duplicate element from the list

# lst = [1,2,3,3,4,5]
# lst1 = []
# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
    
# print(lst1)

#//////////////////////////////////

#code to sort tuple according to 2nd element :

# tup= (1,2,3,1,5,4,7,5)
# t = []
# t2 =[]
# # print(type(t))
# # for i in range(len(tup)):
# #     t.append(tup[i+1])

# for i in range(len(tup)):
#     t.append(tup[i])
# for i in range(len(t)):
#     t2.append(i+1)
#     t2.sort(i+1)

# print(t2)   


#////////////////////////////
# code to reverse element in the list :

# lst1 = [1,2,3,4,5]
# lst2 =[]

# for i in range(len(lst1)):
#     i+=1
#     lst2.append(lst1[len(lst1)-i])
# print()

# print(lst2,end=" ")

#////////////////////////////
#using lambda multiply two number :
# mul = lambda x,y:x*y
# print(mul(2,3))

#//////////////////////////////////
#code to print square of number till 10:
# lst =[1,2,3,4,5,6,7,8,9,10]
# sq = list(map(lambda x : x**2,lst))

# print(sq)

#//////////////////////////////////
#code to filer the names 
# lst =["ahsan","Waqas-ahmad","ahsanulhaq"]

# fil = list(filter(lambda x :len(x)>5 ,lst ))

# print(fil)

#//////////////////////////
#code to find that the number is even or odd 
# is_even = lambda x : "even" if x%2==0 else "odd"
# print(is_even(3))


#///////////////////////////////
#code to double each number in the list 

# lst = [1,2,3,4,5]

# double = list(map(lambda x : x+x,lst))
# print(double)

#/////////////////////////////////
#code to convert list of string into integer

# lst =["ahsan","karak","pakistan","peshawar"]

# integer = list(map(lambda x :len(x),lst))
# print(integer)

#///////////////////////////////////////
#code to celsius to ferhenheight
# lst = [32.3,45.3,75.9,10.2,2]

# fer = list(map(lambda x :( 9/5*x )+ 32,lst))
# print(fer)

#/////////////////////////////////////////
#code to find the product of element in list using reduce function
# from functools import reduce
# lst = [1,2,3,4,5]
# prod = list(reduce(lambda x,y:x+[y*y],lst,[]))
# print(prod)

#///////////////////////////////////////////
#code to find max number in list using reduce :
# lst  = [1,2,3,4,5]
# large = (reduce(lambda x,y:x if x>y else y ,lst))
# print(large)

#/////////////////////////////////////////
#code to concatenate list of string in single string:

# lst =['ahsan','waqas','hassan','haris']
# cont = (reduce(lambda x,y:x+y,lst,""))
# print(cont)

#///////////////////////////////////
#code to filter even number from list using filter and lambda:

# lst = [1,2,3,4,5,6]
# even = list(filter(lambda x:x%2==0,lst))
# print(even)

#//////////////////////
#code to filter out the palindrome string

# def check(s):
#     s1 = ''
#     for i in range(len(s)):
#         i+=1
#         s1 = s1 + s[len(s)-i]
#     return s1    
# lst = ["rar","SAS","waqas","ihsan"]

# palin = list(filter(lambda x :check(x)==x,lst ))
# print(palin)

#////////////////////////////////////
#code to filter out negative integer from list

# lst =[1,2,3,-2,-4,-5]
# neg = list(filter( lambda x:x>0,lst))
# print(neg)

#////////////////////////////////////
#code to enter string and return count of vowels 

# def count_of_vowels():
#     count=0
#     s= input("Enter the string ")
#     vowel ='aeiou'
#     for i in s:
#         if i in vowel:
#             count+=1
#     return count

# count = count_of_vowels()
# print(count)

#//////////////////////////////////
#Q:24 function that excep list and return 2nd largest number:

#/////////////////////////////////
#Q:26 code to iterate manually on list using next and iter function

# lst = [1,2,3,4,5]
# iterator = iter(lst)
# for i in range(len(lst)):
#     print(next(iterator))

#///////////////////////////////////////
#Q 27:checking of iterable
# import collections
# lst = [1,2,3,4,5]
# print(collections.abc.Iterable)
   
#/////////////////////////////
#last question 
# lst = []
# n = int(input("input the number "))
# for i in range(1,n+1):
#    lst.append(i)
# it = iter(lst)
# a = next(it)
# b = next(it)
# sum = a + b
# # print(sum ,end=" ")
# for i in range(len(lst)):
#    try:
#       a= next(it)
#       sum = sum + a
#     #   print(sum, end=" ")
#    except StopIteration:
#       break 
# print(sum)
