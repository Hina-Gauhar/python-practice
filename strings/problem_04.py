# question No.4 
# write a program which removes a particular charcter from a string
a=input(" enter any string : ")
b=input("which charcter u want to remove: ")
c=""
for char in a:
    if(char!= b):
        c+=char
print(c)     
