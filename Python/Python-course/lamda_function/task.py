

# words = ["python","lambda","map","filter"]

# capital = list(map(lambda word : word.capitalize(),words))
# print(capital)

# a =[1,2,3]
# b =[4,5,6]

# sum = list(map(lambda x,y: x+y,a,b))
# print(sum)
#program to calculate its prime number
# number = [2,4,7,9,11,13,16]
# even = list(filter(lambda n : n/n!=0 ,number))
# print(even)


# words = ["apple","banana","orange","grape","umbrella"]

# vowel = "aeiou"

# startvowel = list(filter(lambda v :v[0] in vowel,words))
# print(startvowel)


# words = ["cat","elephant","tiger","hippopotamus"]

# large =reduce(lambda x,y : x if len(x)>len(y) else y,words)

# print(large)

# code to filter out the largest senteces 
# from functools import reduce 
# lst = ["the sun","the beatiful flower bloom in the garden","the big brown bear climbed up high mountain","she ate a delicous sandwich for her lunch","The amazing fireworks","i like swimming",""]

# lst1 = list(filter(lambda x : len(x.split()) >3,lst))
# print(lst1)

# lst1 = list(reduce(lambda x,y: x + [y] if len(y.split())>3  else x,lst,[]))

# print(lst1)


#**********
# lst = [1,2,3,4,5]
# lst1 = [6,7,8,9,10]

# result = lambda x,y:x.extend(y) or x
# print(result(lst,lst1))

#///////////////////////////////////////////////
#calculation of temp using map function
# celsius = [0,20,37,100]
# fah = list(map(lambda c :(9/5)*c +32,celsius))
# print(fah)

#function to calculate its product using reduce()
# from functools import reduce
# number = [1,2,3,4,5]
# result = reduce(lambda x,y:x*y,number)
# print(result)

#function to convert string to uppercase
# lst = ["apple","banana","cherry","kiwi"]
# result = list(map(lambda x:x.upper(),filter(lambda x : len(x)>5,lst)))
# print(result)


# function to calculate the power of even number
# from functools import reduce

# lst =[ 1,2,3,4,5,6]
#by map method
# result = list(map(lambda x : x**2,filter(lambda x : x%2==0,lst)))
#by reduce  method
# # result = list(reduce(lambda x,y : x + [ y**2] if y%2 ==0 else x ,lst,[]))
# print(result)


#converting list into iterator 
# lst = [1,2,3,4]
# lst1 = iter(lst)

# print(next(lst1))
# print(next(lst1))
# print(next(lst1))
# print(next(lst1))


#function to calculate that either its prime or not

# print(result)
#//////////////////////
#function to iterate manualyy !
# lst = [1,2,3,4]
# it = iter(lst)

# for i in it:
#     print(i)
#/////////////////////
# function to find the fibonacci series of  ********
# lst = [11,21,32,42,5,6]
# it = iter(lst)
# a = next(it)
# b = next(it)
# sum = a + b
# print(sum ,end=" ")
# for i in range(len(lst)):
#    try:
#       a= next(it)
#       sum = sum + a
#       print(sum, end=" ")
#    except StopIteration:
#       break 
# print()

#/////////////////////
#function to solve stopiteration exception
# def excep(lst):
#     i = iter(lst)
#     while True:
#       try:
#          print(next(i))
#       except StopIteration:
#          break
    

# lst1 = [1,2,3,4]
# excep(lst1)

