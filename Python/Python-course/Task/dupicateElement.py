list =[1,2,3,4,4,4,5,5]
listitem = []
count = []

for i in range(len(list)):
   
    if (list.count(list[i])>1 and list[i] not in listitem):
        listitem.append(list[i])
        count.append(list.count(list[i]))
print(listitem)       
if(listitem):
    print(f"{listitem} is repeated !",)

else:
    print(f"Item are not repeated")
print(count)