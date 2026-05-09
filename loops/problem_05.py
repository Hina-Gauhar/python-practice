# Problem 7 - Reverse a given integer number.
# Example:

# Input:

# 76542
# Output:

# 24567

num=int(input("enter a number"))
reverse=0
while(num>0):
    a=num%10
    reverse=reverse*10+a
    num//=10

print(reverse)
