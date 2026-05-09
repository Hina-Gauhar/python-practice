# write a program that convert an integer into a string without using str()
a=int(input("enter a number: "))
result=''
digits='0123456789'
#123
while(a!=0):
    result=digits[a%10]+result
    a//=10
print(result,type(result))
