# system library
```py
import sys
import os
```

# Get complete directory of current py file
```py
dir_path = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(dir_path + '222.csv')
```

# Get command line filename
想用一个python文件对多个file进行循环操作, 且file input在command line里，只有在runtime才知道有哪些
```py
filename_list = sys.argv
for file in filename_list:
    with open(file_name) as file:
         for i, l in enumerate(file):
             pass
```


