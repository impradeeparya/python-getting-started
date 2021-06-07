# Use the Brown corpus reader nltk.corpus.brown.words() or the Web text corpus reader nltk.corpus.webtext.words() to
# access some sample text in two different genres.
from nltk.corpus import brown
from nltk.corpus import webtext

brown_genres = brown.categories()
print(brown_genres)
print(brown.sents(categories=brown_genres[-1]))

webtext_genres = webtext.fileids()
print(webtext_genres)
print(webtext.words(webtext_genres[1]))
