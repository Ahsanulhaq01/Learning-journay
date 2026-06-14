lst1 = [1,2,3,4,20]
lst2 = [2,10,50,20,0,20,20]
lst3 =[]




for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i]==lst2[j] and lst1[i] not in lst3:
            lst3.append(lst1[i])
        else:
                print(end="")
# else:
#     print("There is no common element")  
print(lst3)



# print([lst3.append(lst1[i]) for i in range(len(lst1)) for j in range(lst2) if lst1[i]==lst2[j] and lst1[i] not in lst3])

# # print(lst3)


lst = [i for i in lst1 if i in lst2]
print(lst)