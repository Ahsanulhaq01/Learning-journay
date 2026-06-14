# marks = [85,60,59,75,88]
# print(["A+" if i >= 85 else "A" if i > 80 and i<85 else "B" if i>70 and i <80 else "C" if i>=60 and i<70 else "D" if i > 50 and i < 60 else "Fails" for i in marks])


text = "Liat comprehensin is powerfull "
vowel = [char for char in text if char in "aeiou" ]
# print(vowel)
duplicate = []

# for i in vowel:
#     if i not in duplicate:
#     duplicate.append(i)

# print(duplicate)
print(vowel)
# duplicate.count()
for i in range(len(vowel)):
    if (vowel.count(vowel[i])) == 1 :
       duplicate.append(vowel[i])
    #   
    else:
        duplicate.pop(vowel[i])


# print(duplicate)

# sentences =["hi students of low Gpa ","hello engineers","Ai in boom","Machine Failed","Code Excuted"]

# print([sent for sent in sentences if len(sent.split())>2])
