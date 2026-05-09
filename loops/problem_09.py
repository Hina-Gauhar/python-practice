# Problem 9: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.
for i in range(1000,3001):
    digi1=(i//1000)%10
    digi2=(i//100)%10
    digi3=(i//10)%10
    digi4=(i//1)%10
    if(digi1%2==0 and digi2%2==0 and digi3%2==0 and digi4%2==0 ):
        print(i,end=" ")
