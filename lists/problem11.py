# Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
# Input:

# ['1ac21', '23fg', '456', '098d','1','kls']
# [2,6,120,0,1,1]
# Output:

# ['456', '23fg', '1ac21', '1', 'kls', '098d']

l=['1ac21', '23fg', '456', '098d','1','kls']

product_list=[]
for i in range(len(l)):
    product_value=1
    j=l[i]
    for i in range(len(j)):
        if(j[i].isdigit()):

            k=int(j[i])
            product_value*=k
    product_list.append(product_value)
print(product_list)
print(l)
lee=list(zip(l,product_list))
print(lee)

#  sorting tuples based on product value
lee.sort(key=lambda item:item[1],reverse=True)    
# the key parameter tells sort do sorting on the basis of value that is inside me
# this says that do sort the tuples on the basis of 2 item in each tuple
print(lee)

output=[]
for item in lee:
    output.append(item[0])
print(output)

        
