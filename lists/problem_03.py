# write apython program that can convert a 2d list into 1d list
l1=[1,2,3,4,[5,6],7,8,[9,10]]
# for i in range(len(l1)):
#     if type(l1[i]) == list:
#         l2=l1[i]
#         for j in l2:
#             l1.append(j)
#         del l1[i]
# print(l1)
new_list=[]
for i in range(len(l1)):
    
    if type(l1[i]) != list:
        new_list.append(l1[i])
    else:
        l2=l1[i]
        for j in range(len(l2)):
            new_list.append(l2[j])
        
print(new_list)
