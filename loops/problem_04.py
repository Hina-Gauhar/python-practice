# Problem 4 - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.

# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Output:

# 120

num=int(input("enter a number: "))
i=1
mul=1
j=num
while(i<=j):
    if(num!=1):
        print(num," x",end=" ")
    else:
          print(num,end=" = ")
    mul*=num
    num=num-1
    i+=1

print(mul)
