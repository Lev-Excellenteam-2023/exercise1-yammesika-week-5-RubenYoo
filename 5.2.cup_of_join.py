def join(*args: list, sep: str = '-') -> list:
    if not args:
        return []
    elif len(args) == 1:
        return args[0]
    return args[0] + [sep] + join(*args[1:], sep=sep)


print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())
