
# lst1 = []
# total = 0
# print("Enter Your Marks Of all Subject :")
# # for i in range(6):
# #     mark = int(input())
# #     lst1.append(mark)
# #     total = total + lst1[i]
# # print(f"The total marks of Student as : {total}")

# while(len(lst1)<6):

#     mark = int(input())
#     lst1.append(mark)
#     total = total + mark
# average = (total/len(lst1))

# if average<20:
#     print("Wish You Best of luck Try Next Time")
# elif average <40:
#     print("You are Passed ")
# elif average < 70 :
#     print("You are consider as Averavge")
# else:
#     print("You are in toper list")
# print(f"The total marks of Student as : {total} and the average as :{average}")

# student = {1: "ahsan",2:"abdali",3:"haris",4:"Waseem"}

# print(student)

# value1 = student.setdefault(5)
# print(student)
# print(value1)

# value = student.setdefault(6,"paksitan")
# del student[5]
# print(student)
# print(value)

# sum= input('enter two numbers sepearted by commas')
# print(sum)


# try:
#     f= open('prog.cpp','r')
#     print(f.read())
#     print("ashan is in our class")
#     # f.close()
# except Exception as e:
#     print('error is',e)
# else:
#     print("Pakistan is our country ")


name  = "sifat ali shah"
try:
    for i in range(1,len(name)+1):
     print(name[len(name)-i],end="")
  
except IndexError as IE:
    print("You are going outside of range ")    
else:
      print()
