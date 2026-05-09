# question No.7
# write a program that convert a string into title case without using title()
a=input("enter a string ")
c=""
d=""
i=0
for char in a:
    i+=1
    if(char==" "):
        c=c.capitalize()
        d=d+c+" "
        c=""
    else:
        c+=char
    if(i==len(a)):
        c=c.capitalize()
        d=d+c
print(d)
        
