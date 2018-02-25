# map<int, StudentInfo>
# class是把一堆信息封装起来，下面是C++的class写法
# StudentInfo{
#    string name;
#    string address;
#    int phone;
#    int scores;
# };

#####################################################################
# Basic class
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
# Class with __init__ member function
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
# Class with "changeAddress" member function
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
    
  def changeAddress(self, new_address):
    self.address = new_address

b = StudentInfo("yourong","SW1", 123, 100)

print(b.address)
b.changeAddress("N1")
print(b.address)
