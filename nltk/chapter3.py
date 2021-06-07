import re
from test import monty


def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


print(stem('processing'))
print(re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))
print(re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))
print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))
print('python'[-6])
print('monty'[::2])
print('hello World\t THis\t\t is natural language tool kit. let\'s go 1 2 3..'.split())
print('hello World THis\t is natural language tool kit. let\'s go 1 2 3..'.split(' '))
words = 'hello World\t THis\t\t is natural language tool kit. let\'s go 1 2 3..'.split()
print(words.sort())
print(sorted(words))
print(monty)
