# write a program that count the number of words in a string without using spilt()
a=input("enter a string : ")
c=""
d=[]
i=0
for char in a:
    i+=1
    if(char==" "):
        d.append(c)
        c=""
    else:
        c+=char
    if(i==len(a)):  # d appears earlier in ' hina is doing good' so its not good
         d.append(c)
print(d)
