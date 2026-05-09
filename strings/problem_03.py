#question No. 3 
# count the frequency od a particular character in a given string
a=input("enter a sentence: ")
i=input("which char u wnat to count in this sentence ")
# print(a.count(i))   dont use count()
j=0
for char in a:
    if(char==i):
        j+=1
print(j)
