# 神奇的Cache
通常也称为caching，可以让function变快，以function的decorator形式出现

# How does a cache work?
It holds frequently requested data and instructions so that they are immediately available to the CPU when needed. Cache memory is used to reduce the average time to access data from the Main memory. The cache is a smaller and faster memory which stores copies of the data from frequently used main memory locations.

```py
from functools import lru_cache
import time


@lru_cache(maxsize=30) # cache 的用法是在想提高速度的函数上加decorator
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

fib.cache_clear() # uncache the return values
```

# Result
```py
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181] # 因为每个结果都被retained所以会快很多
first using time:  0.0002319812774658203
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
first using time:  0.0060999393463134766
```

# Retest
```py
start_time = time.time()
print(fib(20)) #for n in range(20)])
print('first using time: ', time.time()-start_time)
start_time = time.time()
print(fib1(20)) #for n in range(20)])
print('first using time: ', time.time()-start_time)
```

# Result
```py
6765
first using time:  5.888938903808594e-05 
6765
first using time:  0.0030510425567626953
```
