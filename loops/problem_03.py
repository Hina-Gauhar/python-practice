# Problem 3 - Exercise 12: Display Fibonacci series up to 10 terms.
# Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34
n=int(input("enter number for fibnocci series : "))
i=1
prev=0
curr1=1
while(i<=n):
    print(prev,end=" ")
    curr2=curr1+prev
    prev=curr1
    curr1=curr2
    i+=1
