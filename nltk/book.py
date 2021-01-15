from nltk.book import *


def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage(count, total):
    return 100 * count / total


V = set(text1)
long_word = [w for w in V if len(w) > 15]

names = ['Monty', 'Python']
print(names * 3)
print([w for w in text5 if w.startswith('b')])

text2.dispersion_plot('Elinor Marianne Edward Willoughby'.split(' '))
