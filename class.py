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
a.name = "min"
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
  
  #__init__(self..是member function的固定格式，注意init两边的下划线是两条连着的。括号里的相当于是input，function中相当于要让class里的值和input值一一对应
  def __init__(self, in_name, in_address, in_phone, in_score):
    self.name = in_name
    self.address = in_address
    self.phone = in_phone
    self.score = in_score
  
#a = StudentInfo()
#a.name = "min"
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
# 5. Method to calculate average score for a student
#####################################################################
############# Dictionary
d = {}
d["min"] = 90
d["yoyo"] = 100

sum = 0
for x in d:
  sum += d[x]
  
avg = sum/len(d) #"len"是length，同size
print(avg)

############# Practice
class StudentInfo:
  name = ""
  address = ""
  phone = 0
  scores = {}
  
  def setScore(self, course, score):
    self.scores[course]=score
  
  #区分self.scores, self.scores[], b.average(). 带括号是调用function，不带括号是调用它的variable
  #带括号的表示, 调用getAverage()function, 然后那个function return的东西就会被print出来
  #不带括号, 表示print它的getAverage变量, 然后它发现没有变量, 就给你print一些乱七八糟的东西了
  
  def average(self):
    sum=0
    for x in self.scores:
      sum += self.scores[x]
    return sum/len(self.scores)

b=StudentInfo()
b.setScore("Math",100)
b.setScore("English",90)
print (b.average())

#####################################################################
# 6. Inherit
#####################################################################
# If we want to add teacher info, teacher and student can be the same
# parameters (name, address, phone), and we don't want to duplicate them
# So we can have a base class storing the abstracted data (name,address,phone)


#继承的好处：避免重复，有一定的逻辑联系才可以用继承
class Info:
  name = ""
  address = ""
  phone = 0
  
  def __init__(self,n):
    self.name = n
    
  def getName(self):
    return self.name
  
#类的继承:此处Info是父类(base class/parent class)，StudentInfo是子类(derive class/child class)
class StudentInfo(Info):
  scores = {}
  
  #在类的继承中，如果重定义某个方法，该方法会覆盖父类的同名方法，但有时，我们希望能同时实现父类的功能，这时，我们就需要调用父类的方法了，可通过使用 super 来实现
  #super 的一个最常见用法可以说是在子类中调用父类的初始化方法了,Python3 可使用 super().__init__(a, b)
  #最原始的写法是：super(StudentInfo, self).__init__(a, b)，下面是简化的写法，并不是没有调用self，而是省略了
  def __init__(self,n):
    super().__init__(n)
  
  def setScore(self, course, score):
    self.scores[course]=score
    
  def average(self):
    total_score=0
    for x in self.scores:
      total_score += self.scores[x]
    return total_score/len(self.scores)

class TeacherInfo(Info):
  salary = 0

  def __init__(self,n):
    super().__init__(n)
    
  def setSalary(self,s):
    self.salary = s

  def getSalary(self):
    return self.salary

b=StudentInfo("student1")
b.setScore("Math",100)
b.setScore("English",90)
print (b.name +" has avg score: "+ str(b.average()))

t = TeacherInfo("teacher1")
t.setSalary(2000)
print(t.name + " has salary: "+str(t.getSalary()))

print("\nPrinting all people name")
people = [b,t]
for i in people:
  print(i.getName())
  
#####################################################################
# 7. Encapsulation
#####################################################################
#class has private，public and protected，the above is public because it can be accessed outside the class
#private: 1. can be accessed and modified within the class. eg. member function 2. there are other ways, not mentioned here.
#private:是在member variable前面加两个下划线，这样这个member variable就不能被访问或者被修改
#注意：__init__ 是前后都有两个下划线，叫magic function（method），是python里面特有的特殊的function

#下面print不出来：
class Info:
  __name = ""
  __address = ""
  __phone = 0
  
  def __init__(self, n, a, p):
    self.__name = n
    self.__address = a 
    self.__phone = p 
    
    
class StudentInfo(Info):
  __major = ""
  __score = {}
  
  def __init__(self, n, a, p, m):
    super().__init__(n, a, p)
    self.__major = m
  
  def setScore(self, course, __score):
    self.__score[course] = __score

  
class teacherInfo(Info):
  salary = 0
  
  def __init__(self, n, a, p, s):
    super().__init__(n, a, p)
    self.salary = s
    
print (a.__name,  a.__phone, a.__major)

#可以print出来的方法：
class Info:
  __name = ""
  __address = ""
  __phone = 0
  
  def __init__(self, n, a, p):
    self.__name = n
    self.__address = a 
    self.__phone = p 
    
  def printInfo(self):
    print(self.__name,self.__address,self.__phone)
    
class StudentInfo(Info):
  __major = ""
  __score = {}
  
  def __init__(self, n, a, p, m):
    super().__init__(n, a, p)
    self.__major = m
  
  def setScore(self, course, __score):
    self.__score[course] = __score
    
  def printInfo(self):
    super().printInfo()
    print(self.__major)
  
class teacherInfo(Info):
  salary = 0
  
  def __init__(self, n, a, p, s):
    super().__init__(n, a, p)
    self.salary = s
    
#print (a.__name,  a.__phone, a.__major)

a0 = Info("chouyou","beijing",123213)
a0.printInfo()

a1 = StudentInfo("chouchou", "london", 5431, "computer")
a1.printInfo()

#####################################################################
# 8. Polymorphism
#####################################################################

# class(oo programming)的第四个性质：多态性。有继承关系但是是不同类型的objects放在同一个list里，在运行期python会自动去判断同名的member function
# 三个关键词：run time, dynamic, find a appropriate function



class Info:
  __name = ""
  __address = ""
  __phone = 0
  
  def __init__(self, n, a, p):
    self.__name = n
    self.__address = a 
    self.__phone = p 
    
  def printInfo(self):
    print ("\nprinting information")
    print(self.__name,self.__address,self.__phone)
    
class StudentInfo(Info):
  __major = ""
  __score = {}
  
  def __init__(self, n, a, p, m):
    super().__init__(n, a, p)
    self.__major = m
  
  def setScore(self, course, __score):
    self.__score[course] = __score
    
  def printInfo(self):
    super().printInfo()
    print(self.__major)
    print("is a student")
  
class teacherInfo(Info):
  salary = 0
  
  def __init__(self, n, a, p, s):
    super().__init__(n, a, p)
    self.salary = s
    
  def printInfo(self):
    super().printInfo()
    print (self.salary)
    print("is a teacher")
    
#print (a.__name,  a.__phone, a.__major)

a0 = Info("chouyou","beijing",123213)

a1 = StudentInfo("chouchou", "london", 5431, "computer")

a2 = teacherInfo("choucong", "6JB", 52153, 9000)

a3 = StudentInfo("xiangcong", "N1", 98623, "finance")

a4 = teacherInfo("xiangyou", "SW1W", 38652, 400000)

a5 = StudentInfo("miaomiao", "9NF", 23895, "quant")

a_list = [a0,a1,a2,a3,a4,a5]
for x in a_list:
  x.printInfo()
