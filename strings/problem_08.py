#question No.8
# write a program that convert an integer into a string without using str()
a=int(input("enter a number"))

digits='0123456789'
result=''
while(a!=0):
    result=digits[a%10] + result
    a//=10
print(result)
