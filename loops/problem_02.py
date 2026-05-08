#The current population of a town is 10,000. The population of the town is increasing at a rate of 10% per year. 
# You have to write a program to find out the population at the end of each  of the last 10 year.

pop=10000
b=2020
for i in range(1,11):
    a=(pop*10)/100
    pop+=a
    print("The population at the end of year ",b," is ",pop)
    b+=1
    
