# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('i am wrapper')
#         func(*args, **kwargs)
#         print('after func')
#         return
#     return wrapper
#

def log_level(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('i am wrapper')
            func(*args, **kwargs)
            print('after func')
            print('my level', level)
        return wrapper
    return decorator

# @log_level('wwwww')
# # @decorator
# def foo(a):
#     print('i am foo,a', a)
#
# foo('lll')

#
# b = 'global'
# def foo1():
#     b = 'local'
#     def inner():
#         bb = 'inner'
#         print b
#         print locals()
#     inner()
#     print locals()
#     print globals()
#
# foo1()


import functools
def a(b=6,c=8,d=7,e=2):
    print b,c,d,e

pa = functools.partial(a, 1,2,)
print pa(9)
