# write a program to check if a list is in ascending order or not
l=[10,1.2,8,22,3,66,11,99,1011,24]
copy_list=l.copy()
copy_list.sort()

if l== copy_list:
    print('yes it is in ascending order')
else:
    print('no it is not in ascending order')
