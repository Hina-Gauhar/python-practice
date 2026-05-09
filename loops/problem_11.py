# Problem 11:Write a program to print whether a given number is a prime number or not
num=int(input("enter a number"))
i=2
if(num<=1):
    print("not prime")
else:
    while(i<num):
        if(num%i==0):
            print("not prime")
            break
        i+=1
    else:
        print(num," is a prime number")
    
