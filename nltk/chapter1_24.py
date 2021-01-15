from nltk.book import *


def find(text):
    words = []
    for w in text:
        if w.istitle() and ('z' in w) and ('pt' in w) and w.endswith('ize'):
            words.insert(0, w)
    return words


print(find(text6))
