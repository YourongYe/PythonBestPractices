# LIST

a = 2
b = 3.5
c = a*b
print (c)

a = [1,2,3,4,5,6] #list,相当于C++里的vector
print (a)

b = []
b.append(2)
b.append(3)
b.append(4)
print (b)

c = list(range(1,10)) #初始化list
print (c)

d = list(range(10)) #默认从0开始，默认间隔是1
print (d)

e = list(range(1,10,2)) #最后一个是间隔
print (e)

f = [1,2,5,2,6,2,7]
for x in f: #for循环，格式很重要，要空两格才属于循环里的东西
  print (x*2)


