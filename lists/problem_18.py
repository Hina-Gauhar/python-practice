# Problem 13: Write a list comprehension to print the following matrix
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
l=[]
a=[]
for i in range(0,3):
    for j in range(0,3):
        a.append(j +(i*3))
    l.append(a)
    a=[]
print(l)

[[i + j*3 for i in range(3)] for j in range(3)]

# [i + j*3 for i in range(3)] this creates a list bcz of square brackets around them 
