def volume(a,b): #相当于C++中的function，python中没有type的概念
  c = a*b #volume不需要定义是int还是double
  return c
  
def volume(area,height): 
  v = area*height
  return v
#最好在一开始就定义变量是什么，否则以后会忘记a代表什么，b代表什么
  
x = volume(1,2)
print(x)
print(volume(2,2))

def circle_area(radius):
  area = radius*radius*3.14 #radius**2 （次方）
  return area 
  
def square_area(a):
  return a**2
  
print (circle_area(2.8))
print (square_area(4))

#https://www.python-course.eu/python3_variables.php
#https://www.python-course.eu/python3_list_manipulation.php
#https://www.python-course.eu/python3_functions.php
