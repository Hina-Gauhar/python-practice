# Problem 1: Combine two lists index-wise(columns wise)
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given List:

# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]
# Output:

# [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]

list1 = ["M", "na", "i", "Kh",'sama']
list2 = ["y", "me", "s", "an",'sama']
l=[]

l=list(zip(list1,list2))

    
# print(l)

min_len=min(len(list1),len(list2))
if(len(list1)>len(list2)):
    max_list=list1
else:
    max_list=list2


for i in range(min_len,len(max_list)):
    l.append(max_list[i])
print(l)



# max compare lexicographically
# max(list1,list2) does not return list with longer length but rather lexicographical comparison occurs

