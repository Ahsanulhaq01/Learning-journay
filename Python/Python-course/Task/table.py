# for i in range(1,11):
#     print(f"2 * {i} :  {2 * i}")

num = 2
rnge = 11

table =[f"{num} * {i} =  {num*i}"for i in range(1,rnge)]
table

for i in range(len(table)):
    print(table[i])


