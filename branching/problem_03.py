# Problem 1:
# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

a=int(input("enter 1st angle"))
b=int(input("enter 2nd angle"))
c=int(input("enter 3rd angle"))

if((a+b+c)>=180):
  print("its a triangle")
else:
  print("not a triangle")
  
