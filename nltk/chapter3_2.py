# We can use the slice notation to remove morphological endings on words. For example, 'dogs'[:-1] removes the last
# character of dogs, leaving dog. Use slice notation to remove the affixes from these words (we've inserted a hyphen
# to indicate the affix boundary, but omit this from your strings): dish-es, run-ning, nation-ality, un-do, pre-heat.


def stem(word):
    for suffix in ['es', 'ning', 'ality', 'do', 'heat']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word


s = ['dishes', 'running', 'nationality', 'undo', 'preheat']
for index in range(len(s)):
    print(stem(s[index]))
