# Define a conditional frequency distribution over the Names Corpus that allows you to see which initial letters are
# more frequent for males versus females

import nltk
from nltk.corpus import names

name_fileids = names.fileids()
print(name_fileids)
print(names.words(name_fileids[1]))

cfd = nltk.ConditionalFreqDist(
    (fileid, word[0])
    for fileid in names.fileids()
    for word in names.words(fileid)
)

cfd.plot()
cfd.tabulate()
