# 神奇的Cache
```py
from functools import lru_cache
import time


@lru_cache(maxsize=30)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib1(n):
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)
start_time = time.time()
print([fib(n) for n in range(20)])
print('first using time: ', time.time()-start_time)
start_time = time.time()
print([fib1(n) for n in range(20)])
print('first using time: ', time.time()-start_time)
```

# Result
```py
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
first using time:  0.0002319812774658203
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
first using time:  0.0060999393463134766
```
