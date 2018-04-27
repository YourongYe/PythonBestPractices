class StudentInfo:
  name = ""
  major = ""
  score = {}
  register = []
  
  def __init__(self, in_name, in_major):
    self.name = in_name
    self.major = in_major
    
  def setScore(self, course, subscore):
    self.score[course] = subscore
  
  def registration(self, x):
    self.register.append(x)
  
  def register_amount(self):
    return sum(self.register)
  
  def averageScore(self):
    sum = 0
    for x in self.score:
      sum += self.score[x]
    return sum/len(self.score)

a = StudentInfo("yoyo", "finance")
a.setScore("math", 90)
a.setScore("trading", 80)
a.setScore("derivatives", 75)
a.registration(0)
a.registration(1)



print (a.name, a. major, a.score, a.register)
print (a.averageScore())
print (a.register_amount())
