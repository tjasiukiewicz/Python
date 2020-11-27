#
# Decorator cache
#
import time
import functools

def cache_decorator(func):
    cache = {}
    pass

@cache_decorator
def big_fat_function(a, b):
    time.sleep(2)
    return a + b

# miss cache
print(big_fat_function(2, 3))
print(big_fat_function(2, 2))
print(big_fat_function(2, 1))
# hit cache
print(big_fat_function(2, 1))
print(big_fat_function(2, 2))