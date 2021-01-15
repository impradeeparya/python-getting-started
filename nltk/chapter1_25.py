def print_a(words):
    return [word for word in words if word.startswith('sh')]


def print_b(words):
    return [word for word in words if len(word) > 4]


sent = 'she sells sea shells by the sea shore'.split(' ')
print('a : ', print_a(sent))
print('b : ', print_b(sent))
