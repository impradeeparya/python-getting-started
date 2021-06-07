# Describe the class of strings matched by the following regular expressions.
#
# [a-zA-Z]+
# [A-Z][a-z]*
# p[aeiou]{,2}t
# \d+(.\d+)?
# ([^aeiou][aeiou][^aeiou])*
# \w+|[^\w\s]+
# Test your answers using nltk.re_show().

import nltk

reg_ex = ['[a-zA-Z]+', '[A-Z][a-z]*', 'p[aeiou]{,2}t', '\d+(.\d+)?', '([^aeiou][aeiou][^aeiou])*', '\w+|[^\w\s]+']
for index in range(len(reg_ex)):
    nltk.re_show(reg_ex[index], 'hello World THis is natural language tool kit. let\'s go 1 2 3..')
