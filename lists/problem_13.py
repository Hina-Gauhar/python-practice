# Problem 8: Split String of list on K character.

# Example :

# Input:

# ['CampusX is a channel', 'for data-science', 'aspirants.']
# Output:

# ['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']
l=['CampusX is a channel', 'for data-science', 'aspirants.']
result=[]
for i in l:
    a=i.split(' ')
    for j in a:
        result.append(j)
print(result)
        
