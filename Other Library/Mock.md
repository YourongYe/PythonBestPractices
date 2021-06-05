# When to use mock?
-> When your test has dependencies, you want to test your code in a controlled environment   
-> Certain conditions that are hard to satisfy (Eg. if, except statement), mock these conditions can help improve your code coverage.  
-> The usage of mock objects can be tracked. (Eg. function A has been called 2 times in this test)  


## Basics
1. Mock a function
```py
from unittest.mock import Mock
import datetime

# This is the function you wanna mock
today = datetime.datetime.today()
print("Real Function: ")
print(f"Today is {today}")

# mock the library and then define the return value of the function you wanna mock
datetime_mock = Mock()

datetime_mock.datetime.today.return_value = "2021/06/05"
today_by_mock = datetime_mock.datetime.today()

print("Mock Function: ")
print(f"Today is {today_by_mock}") 
```

2. Mock an object
- If the input of our test is an object, and it behaves differently based on the object, in this case, we can mock different object as inputs to test it.  
- If a function within our test returns an object, which will affect how the rest of the test behaves, then we need to mock the returned obj based on different scenarios.  
```py
class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    

person_A = Person("Ana", 15, "F")
print("Real Instance: ")
print(person_A.name, person_A.age, person_A.gender)

# Mock the instance
person_A_mock = Mock()
person_A_mock.name = "Ana"
person_A_mock.age = 15
person_A_mock.gender = "F"

print("Mock Instance: ")
print(person_A_mock.name, person_A_mock.age, person_A_mock.gender)
```
