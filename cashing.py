import functools


@functools.cache
def foo(arg: int):
    print(666666666666)
    return arg * 3


print(foo(10))
print(foo(10))
