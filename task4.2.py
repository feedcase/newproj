from itertools import chain


def log(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        fn_name = fn.__name__
        fn_args = chain(map(str, args), map(lambda key: '%s=%s' % (key, kwargs[key]), kwargs))
        fn_call = '%s(%s)' % (fn_name, ', '.join(fn_args))
        print('%s -> %s' % (fn_call, result))
        return result
    wrapper.__name__ = 'print_%s' % fn.__name__
    return wrapper


@log
def a(x):
    return -x


@log
def b(x, y):
    return x * y


@log
def c(x, y, *args):
    result = x + y
    for arg in args:
        result += arg
    return result


a(1)
b(2, y=3)
c(1, 2, 3)