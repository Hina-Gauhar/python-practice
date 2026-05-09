#question No.5
# write a program that can check wheather a given string is a palindrome or not
# palondrome is noon ,1001, pop, radar,rotator
a=input(" enter any string : ")
c=a[::-1]
if(a==c):
    print("it is palondrome")
else:
    print("not a palondrome")    
