from functools import reduce


def multiply(fn):
    def wrapper(*numbers):
        result = reduce(lambda a, b: a * b, numbers)
        fn(result)
    return wrapper


@multiply
def func(x):
    print(x)


numbers = map(int, input().split())
func(*numbers)

# in  > 1 2 3
# out > 6
