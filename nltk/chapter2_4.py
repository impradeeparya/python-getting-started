# Read in the texts of the State of the Union addresses, using the state_union corpus reader. Count occurrences of
# men, women and people in each document. What has happened to the usages of these words over time?
import nltk
from nltk.corpus import state_union

fileids = state_union.fileids()
print(fileids)
print(fileids[1][:4])
print(state_union.words(fileids[1])[:100])

cfd = nltk.ConditionalFreqDist(
    (gender, fileid[:4])
    for fileid in state_union.fileids()
    for word in state_union.words(fileid)
    for gender in ['men', 'women', 'people']
    if word.lower().startswith(gender)
)
cfd.plot()
