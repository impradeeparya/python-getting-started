from nltk.corpus import webtext

phrases = webtext.words()
print(phrases)
sub_phrases = phrases[100:150]
print(sub_phrases)
print(sorted(sub_phrases))
