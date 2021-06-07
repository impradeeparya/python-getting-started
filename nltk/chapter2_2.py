# Use the corpus module to read austen-persuasion.txt. How many word tokens does this book have? How many word types?
from nltk.corpus import gutenberg

words = gutenberg.words('austen-persuasion.txt')
print(len(words))
print(len(set(words)))
