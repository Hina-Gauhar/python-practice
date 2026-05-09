# write a program to replace one of the duplicate intem in the list
l1=[1,2,3,4,1,5,5,6,7,3]
# replace 3 with 300

# for i in l1:
#     for j in range(1,len(l1)):
#         if(l1.index(i)!=j):
#             if(i==l1[j]):
#                 l1[j]='duplicate'

# print(l1)
flag=False
for i in range(0,len(l1)):
    if(l1[i]==3):
        
        if flag:
            l1[i]=300
            
        flag=True   
print(l1)       
        
