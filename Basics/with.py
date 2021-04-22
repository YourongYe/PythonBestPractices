# with statement用法
```py
with open('path','读写模式‘) as f:
    do something
```

# 等价于
```py
f = open('path','读写模式')
do something
f.close()
```

# Summary
with statement 会自动close和exit文件，并且还可以handle exception
