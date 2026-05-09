# Problem 14: Write a list comprehension that can transpose a given matrix
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# output:
# [[1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# [[1, 4, 7],[2, 5, 8],[3, 6, 9]]

b=[]
for i in range(3):
    a=[]
    for j in matrix:
        a.append(j[i])
    b.append(a)
    
print(b)

[[(j[i]) for j in matrix]for i in range(3)]
