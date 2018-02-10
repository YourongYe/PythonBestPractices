# LIST

a = [1,2,3,4,5,6]
print(a)

b = []
b.append(2)
b.append(3)
b.append(4)
print(b)

c = list(range(1,10))
print(c)

d = list(range(10))
print(d)

e = list(range(1,10,2))
print(e)

f = [1,2,5,2,6,2,7]
# C++
# for(int i=0; i<f.size(); i++){
#    std::cout<<f[i]<<std::endl;  
# }
for x in f:
  print(x)
