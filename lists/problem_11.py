# Problem 6: Find list of common unique items from two list. and show in increasing order
# Input

# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# Output:

# [34, 67, 89]


num1 = [23,45,67,78,89,34,67]
num2 = [34,89,55,56,39,67]

l=[]
for i in num1:
    if i in num2:
        if(i not in l):
            l.append(i)
l=sorted(l)
print(l)
