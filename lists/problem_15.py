# Problem 10: Add Space between Potential Words.
# Example:

# Input:

# ['campusxIs', 'bestFor', 'dataScientist']
# Output:

# ['campusx Is', 'best For', 'data Scientist']

l=['campusxIs', 'bestFor', 'dataScientist']
l1=[]
for i in range(len(l)):
    flag=False
    lower=''
    upper=''
    for j in l[i]:
        if j.isupper():
            flag=True
        if not flag:
            lower+=j
        else:
            upper+=j
            
    l1.append(lower + ' ' + upper)

print(l1)
            
    
    
