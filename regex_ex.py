import re

word = input('Insert word here: ')

#for i in range(len(word)):
#    if re.search('[A-Za-z]', word[i]):
#        print(word[i])
#
#    else:
#        print('NOT FOUND')

#if re.search('[A-Za-z]', word[0]) and re.search('[A-Za-z]', word[1]):
#    print('Is Valid!')
#
#else:
#    print('Not Valid!')
for i in word:
    if not (re.search('[A-Za-z0-9]', i)):
        print('Invalid character ')
        break