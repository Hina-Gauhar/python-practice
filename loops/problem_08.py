# Problem 8: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.
i=0
user=1
sum=0
while(user!=0):
    user=int(input("enter a  number: "))
    if(user==0):
        break
    sum+=user
    
    i+=1

print(sum)
avg=sum/i
print(avg)
