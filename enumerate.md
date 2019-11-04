# Example
```py
l1 = ['asd', 'wer', 'rty', 'vbn']
for i, l in enumerate(l1):
    print(i, l)
```

# Same solution using list index
```py
for i in range(len(l1)):
    print(i, l1[i])
```

# Result
```py
0 asd
1 wer
2 rty
3 vbn
0 asd
1 wer
2 rty
3 vbn
```

# Summary
enumerate 更方便更简洁，而且可以调整起始点的index，不一定从0开始

# Example
```py
l1 = ['asd', 'wer', 'rty', 'vbn']
for i, l in enumerate(l1,10):
    print(i, l)
```

# Result
```py
10 asd
11 wer
12 rty
13 vbn
```
