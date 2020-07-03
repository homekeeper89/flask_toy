import re

target = "hello"

the_list = re.compile('.*({}).*'.format(target), re.I)

word = 'HeLLo'

if the_list.match(word):
    print("in", word)
else:
    print("not",word)