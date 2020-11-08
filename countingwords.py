introstring = input('enter string')
charactercount = 0
wordcount = 1
for i in introstring:
    charactercount = charactercount + 1
    if(i==' '):
        wordcount=wordcount + 1
print('number of word in the string') 
print(wordcount)
print('number of characters in the string')
print(charactercount)
