import nltk
from nltk.corpus import gutenberg
from nltk.corpus import wordnet as wn

# from nltk.corpus import inaugural
# from nltk.corpus import swadesh

# from nltk.corpus import webtext

print(gutenberg.fileids(), end='\n')
print(len(gutenberg.words('austen-persuasion.txt')))
#
# for fileid in gutenberg.fileids():
#     num_chars = len(gutenberg.raw(fileid))
#     num_words = len(gutenberg.words(fileid))
#     num_sents = len(gutenberg.sents(fileid))
#     num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
#     print(int(num_chars / num_words), int(num_words / num_sents), int(num_words / num_vocab), fileid)
#
# milton_paradise_sentences = gutenberg.sents('milton-paradise.txt')
# print('milton_paradise_sentences', milton_paradise_sentences, end='\n')
#
# for fileid in webtext.fileids():
#     print(fileid, webtext.raw(fileid)[:65])

# chat_room = nps_chat.posts('10-19-20s_706posts.xml')
# print(chat_room[213:300])

# print(brown.categories())
# print(brown.words(categories=['news', 'mystery']))

# news_text = brown.words(categories='news')
# fdist = nltk.FreqDist([w.lower() for w in news_text])
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# for m in modals:
#     print(m, fdist[m])

# cfd = nltk.ConditionalFreqDist(
#     (genre, word)
#     for genre in brown.categories()
#     for word in brown.words(categories=genre)
# )

# genres = ['new', 'religions', 'hobbies', 'science_fiction']
# modals = ['can', 'could', 'may', 'might', 'must', 'will']
# print(cfd.tabulate(conditions=genres, samples=modals))

# cdf = nltk.ConditionalFreqDist(
#     (target, fileid[:4])
#     for fileid in inaugural.fileids()
#     for w in inaugural.words(fileid)
#     for target in ['america', 'citizen']
#     if w.lower().startswith(target)
# )
# # cfd.plot()
#
# puzzle_letters = nltk.FreqDist('egivrvonl')
# obligatory = 'r'
# word_list = nltk.corpus.words.words()
# # print([w for w in word_list if len(w) >= 4 and obligatory in w and nltk.FreqDist(w) <= puzzle_letters])
#
# print(swadesh.fileids())
# print(swadesh.words('en'))
# en_2_fr = swadesh.entries(['en', 'fr'])
# translate = dict(en_2_fr)
# print(translate['dog'])


motorcar = wn.synsets('motorcar')
print(motorcar)
print(wn.synset('car.n.01').lemma_names())
print(wn.synset('car.n.01').definition())
print(wn.synsets('car'))
print(wn.synset('car.n.01').hyponyms())
print(wn.synset('car.n.01').hyponyms()[26])
print(sorted([lemma.name() for synset in wn.synset('car.n.01').hyponyms() for lemma in synset.lemmas()]))

nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt')).concordance('however', lines=10)
