from collections import deque
from functools import reduce
from random import randint
import math

n = int(input('Input count of numbers: '))
a = [randint(0, 9) for i in range(n)]

print('List of numbers: ', a)

reducer, mapper, predicate = input('Input what you want to do with it: ').split()


def sum(x):
    return math.fsum(x)


def multiply(x):
    return math.prod(x)


def join(x):
    dec = 1
    i = -1
    for item in range(len(x)):
        b = dec * x[i]
        i -= 1
        dec *= 10
        return b


def unite(x: set, y):
    x.add(y)
    return x


def reverse(x: deque, y):
    x.appendleft(y)
    return x


def negated(x):
    return -x


def inverted(x):
    return 1 / x


def squared(x):
    return x * x


def odds(x):
    return x % 2 == 1


def evens(x):
    return x % 2 == 0


def primes(x):
    return x in {1, 2, 3, 5, 7}


filters = {x.__name__: x for x in (odds, evens, primes)}
mappers = {x.__name__: x for x in (negated, inverted, squared)}
reducers = {x.__name__: x for x in (sum, multiply, join, unite, reverse)}
initials = {
    'sum': lambda: 0,
    'multi[ly': lambda: 1,
    'join': lambda: 0,
    'unite': set,
    'reverse': list
}

reducer = reducers[reducer]
initial = initials[reducer]
mapper = mappers[mapper]
predicate = filters[predicate]
res = reduce(reducer, map(mapper, filter(predicate, a), initial()))


print('Result: ', res)
