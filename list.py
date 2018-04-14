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

#list 不分大小顺序，可以重复

b = [1,2,3]
b.append(78)
b.append(56)
b.append(87)
b.append(66)

print (b)

print (b.pop(0)) #剔除第一个数
print (b.pop(4)) #剔除第五个数
print (b[4]) #print出第五个数字（数第几个的时候是从0开始）


for x in b:
  print (str(x/100)+"%")
