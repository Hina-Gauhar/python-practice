# Problem 15: Write a list comprehension that can flatten a nested list
# Input
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
a=[]
for i in matrix:
    for j in i:
        a.append(j)
        
print(a)

result=[j for i in matrix for j in i]    # outer loop is on right and inner loop is on left same like if
print(result)
