def interleave(*iterables):
    result = []
    max_len = max(len(iterable) for iterable in iterables)

    for i in range(max_len):
        for iterable in iterables:
            if i < len(iterable):
                result += [iterable[i]]

    return result


def interleave_gen(*iterables):
    max_len = max(len(iterable) for iterable in iterables)

    for i in range(max_len):
        for iterable in iterables:
            if i < len(iterable):
                yield iterable[i]


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))

lst = []
gen = interleave_gen('abc', [1, 2, 3], ('!', '@', '#'))
for c in gen:
    lst += [c]
print(lst)
