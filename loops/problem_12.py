# Problem 12:Print all the Armstrong numbers in a given range.
# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
lower=int(input("enter a number: "))
upper=int(input("enter a number: "))

# 12345
for i in range(lower,upper+1):
    temp=i
    while(temp>0):
        sum+=(temp%10)**3
        temp=temp//10
    if(sum==i):
        print(i)
    
