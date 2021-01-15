from nltk.book import *


def percentage(word, text):
    word_count = 0
    for t in text:
        if t == word:
            word_count += 1
    return 100 * word_count / len(text)


percentage('the', text1)
