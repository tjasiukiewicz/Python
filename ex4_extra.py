#
# Decorator cache
#
import functools
import time

def cached_decorator(func):
    cache = {}
    @functools.wraps(func)
    def internal(*args, **kwargs):
        key = args, tuple(kwargs)
        if key not in cache:
            print("CACHE MISS!!")
            cache[key] = func(*args, **kwargs)
        else:
            print("CACHE HIT!!!")
        return cache[key]
    return internal

@cached_decorator
def big_fat_function(a, b):
    time.sleep(1)
    return a + b
# miss cache
print(big_fat_function(2, 3))
print(big_fat_function(2, 2))
print(big_fat_function(2, 1))
# hit cache
print(big_fat_function(2, 1))
print(big_fat_function(2, 2))

@cached_decorator
def fibonacci(idx):
    x0, x1 = 1, 1
    if idx < 2:
        return x0
    return fibonacci(idx - 2) + fibonacci(idx - 1)

print(fibonacci(35))
print(fibonacci(35))