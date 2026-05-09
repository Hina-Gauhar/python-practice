# write a program to remove duplicate items from the list
l1=[1,2,1,2,3,4,5,3,4]
l2=[]
for i in range(len(l1)):
    if l1[i] not in l2:
        l2.append(l1[i])
print(l2)
