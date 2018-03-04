# map<int, StudentInfo>
# class是把一堆信息封装起来，下面是C++的class写法
# StudentInfo{
#    string name;
#    string address;
#    int phone;
#    int scores;
# };

#####################################################################
# 1. Basic class
#####################################################################

class StudentInfo:
  name = ""
  address = ""
  phone = 0
  score = 0
  
a = StudentInfo()
a.name = "mincong"
a.address = "N1"
a.phone = 2123
a.score = 100

print(a.name)
print(a.address)
print(a.phone) 

#####################################################################
# 2. Class with __init__ member function
#####################################################################

class StudentInfo:
  name = ""
  address = ""
  phone = 0
  score = 0
  
  def __init__(self, in_name, in_address, in_phone, in_score):
    self.name = in_name
    self.address = in_address
    self.phone = in_phone
    self.score = in_score
  
#a = StudentInfo()
#a.name = "mincong"
#a.address = "N7"
#a.phone = 2123
#a.score = 100

b = StudentInfo("yourong","SW1", 123, 100)

print(b.name)
print(b.address)
print(b.phone)

#####################################################################
# 3. Class with "changeAddress" and "deduceScore" member function
#####################################################################

class StudentInfo: 
  #以下四个都是member variables
  name = ""
  address = ""
  phone = 0
  score = 0

  #__init__是属于class的特殊函数（前后有两条下划线），用来初始化class的
  # 这是属于class的member function
  def __init__(self, in_name, in_address, in_phone, in_score): 
    self.name = in_name     
    self.address = in_address
    self.phone = in_phone
    self.score = in_score
    
  def changeAddress(self, new_address):
    self.address = new_address
  
  def deduceScore(self, num):
    self.score -= num

b = StudentInfo("yourong","SW1", 123, 100)

print(b.address)
b.changeAddress("N1")
print(b.address)
print(b.score)
b.deduceScore(10)
print(b.score)

#####################################################################
# 4. Class with multiple scores member variables, storing in dictionary
#####################################################################

class StudentInfo:
  name = ""
  address = ""
  phone = 0
  scores = {}

  #__init__是属于class的特殊函数（前后有两条下划线），用来初始化class的
  # 这是属于class的member function
  def __init__(self, in_name, in_address, in_phone): 
    self.name = in_name     
    self.address = in_address
    self.phone = in_phone
    
  def changeAddress(self, new_address):
    self.address = new_address
  
  def setScore(self, course, score):
    self.scores[course] = score

b = StudentInfo("yourong","SW1", 123)

print(b.address)
b.changeAddress("N1")
print(b.address)

print(b.scores)
b.setScore("Math", 100)
print(b.scores)

#####################################################################
# 5. Class to calculate average scores
#####################################################################
d = {}
d["mincong"] = 90
d["yoyo"] = 100

sum = 0
for x in d:
  sum += d[x]
  
avg = sum/len(d)
print(avg)
