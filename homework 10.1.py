def prime_generator(value):

    for x in range(1, (value + 1)):
        result = []

        for y in range(1, value + 1):
            if x % y == 0:
                result.append(y)
        if len(result) == 2:
            yield x

from inspect import isgenerator

gen = prime_generator(10)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')