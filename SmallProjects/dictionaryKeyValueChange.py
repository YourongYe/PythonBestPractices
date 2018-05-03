#dictionary的key是唯一的值（unique），但value可以相同重复
#如果key重复了，那么后者对应的value会覆盖（overwrite）前者

d = {1:"yoyo",2:"min",3:"min"}
d1 = {}
for x in d:
  d1[d[x]] = x

print(d1)
print(d1["min"])
