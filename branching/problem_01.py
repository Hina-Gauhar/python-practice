# find the minimum of 3 numbers
a=int(input("enter a number : "))
b=int(input("enter a number : "))
c=int(input("enter a number : "))

if(a<b and a<c):
    print(a, " is the smallest")
elif(b<a and b<c):
    print(b, " is the smallest")
else:
    print(c," is the smallest")
