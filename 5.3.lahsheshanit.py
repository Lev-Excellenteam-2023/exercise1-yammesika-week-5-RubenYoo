import string

ALPHABET = list(string.ascii_lowercase)
HIT = '!'
BLOCK_SIZE = 1
MAX_SIZE_BLOCK = 46  # longest word in english is 45 (+ 1 for '!')
PATH = 'logo.jpg'


def is_in_alphabet(s):
    for c in s:
        if c not in ALPHABET:
            return False
    return True


def print_word(s):
    word = ''
    for c in reversed(s):
        if c in ALPHABET:
            word = c + word
        else:
            return word + HIT
    return word + HIT


def func():
    with open(PATH, encoding="utf8", errors='ignore') as file:
        while True:
            block = file.read(BLOCK_SIZE)
            while HIT not in block:
                if len(block) == MAX_SIZE_BLOCK:
                    block = block[1:]
                app = file.read(BLOCK_SIZE)
                if app:
                    block += app
                else:
                    return
            yield block


gen = func()
lst = []
for i in gen:
    if len(i) > 5 and is_in_alphabet(i[i.index(HIT)-5:i.index(HIT)]):
        lst += [print_word(i[:i.index(HIT)])]

print(lst)
