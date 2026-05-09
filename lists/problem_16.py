# Problem 11: Write a program that can perform union operation on 2 lists
# Example:

# Input:

# [1,2,3,4,5,1]
# [2,3,5,7,8]
# Output:

# [1,2,3,4,5,7,8]

l1=[1,2,3,4,5,1]
l2=[2,3,4,5,7,8]
l=[]
for i in l1:
    if i not in l:
        l.append(i)
for i in l2:
    if  i not in l:
        l.append(i)
print(l)


# cleaner version
for i in l1 + l2:    # l1 + l2 [1,2,3,4,5,1,2,3,4,5,7,8]
    if i not in l:
        l.append(i)
print(l)
    
