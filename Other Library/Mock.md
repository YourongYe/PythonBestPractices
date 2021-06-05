# When to use mock?
-> When your test has dependencies, you want to test your code in a controlled environment   
-> Certain conditions that are hard to satisfy (Eg. if, except statement), mock these conditions can help improve your code coverage.  
-> The usage of mock objects can be tracked. (Eg. function A has been called 2 times in this test)  


## Basics
1. Mock a function
- Note that we use ***.return_value*** to mock the return value of a function
- Note that we ***don't use .return_value*** when we just wanna mock an attribute of an object
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
Results
```py
Real Function:
Today is 2021-06-05 17:43:05.066949
Mock Function:
Today is 2021/06/05
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
person_A_mock.name = "Ana"  # here we don't use .return_value cus its not a function, name is just an attribute
person_A_mock.age = 15
person_A_mock.gender = "F"

print("Mock Instance: ")
print(person_A_mock.name, person_A_mock.age, person_A_mock.gender)
```
Results:
```py
Real Instance:
Ana 15 F
Mock Instance:
Ana 15 F
```

3. Mock an exception
- We use ***.side_effect*** to mock exception, but it can also be used to redirect to another function
```py
import requests
from requests.exceptions import Timeout
from unittest.mock import Mock
import unittest

requests = Mock()

def get_holidays():
    r = requests.get("http://fakeurl.com")
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):

    def test_get_holidays_retry(self):
        requests.get.side_effect = Timeout

        with self.assertRaises(Timeout):
            get_holidays()

        assert requests.get.call_count == 1
  
if __name__ == "__main__":
    unittest.main()
```
