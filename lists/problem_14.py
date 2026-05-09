# Problem 9: Convert Character Matrix to single String using string comprehension.
# Example 1:

# Input:

# [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
# Output:

# campux is best channel
l=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]

sentence=''
for i in range(len(l)):
    word=''
    k=l[i]
    for j in range(len(k)):
        word+=k[j]
    if(sentence==''):
        sentence+= word
    else:
        sentence=sentence+ ' ' + word
print(sentence)

l=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
result=''
result=' '.join([''.join(i) for i in l])
# join works like for loop it iterates over all i in a list and join then
# step 1 (1st join make words)
# each i in l after join becomes ['campusx','is','best','channel']
# 2nd join join these i of new list with space and make sentence



# beehavious of join()
# join() takes a list(or set,tuple etc) of strings(strictly) and convert them into a single strings such as here
# ['c', 'a', 'm', 'p', 'u', 'x']  -> 'campusx'    here separator is '' empty
# or ['campusx', 'is' , 'best' ,'channel']   ->   campusx is best channel   here separator is ' ' space
# it does not work on integers or other data types bcz internally it does string concatenation
print(result)
