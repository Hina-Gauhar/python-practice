# Problem 4: Running Sum on list
# Write a program to print a list after performing running sum on it.

# i.e:

# Input:

# list1 = [1,2,3,4,5,6]
# Output:

# [1,3,6,10,15,21]

list1 = [1,2,3,4,5,6]
l=[]
# [1,previous 2, previous and here previous,


prev=0
l.append(list1[prev])

for prev in range(1,len(list1)):
    l.append(list1[prev]+l[-1])
    
    
# a=
print(l)

    
