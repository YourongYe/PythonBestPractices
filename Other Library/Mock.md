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

datetime_mock.datetime.today.return_value = "2021/06/05" # 如果把datetime_mock换成datetime，就可以替换掉datetime这个library，让它按照我们自己的test设计来return任何值
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
- ***.side_effect*** can be set to be a class, function or iterable
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
        requests.get.side_effect = Timeout  # here Timeout is a class

        with self.assertRaises(Timeout):
            get_holidays()

        assert requests.get.call_count == 1
  
if __name__ == "__main__":
    unittest.main()
```
- ***.side_effect*** take iterables: it means the mocked function will behave differently, in the order of the iterable
```py
requests = Mock()

def get_holidays():
    r = requests.get("http://fakeurl.com")
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):

    def test_get_holidays_retry(self):
        requests.get.side_effect = [Timeout, ConnectionError]

        with self.assertRaises(Timeout): # first time mock function gets called
            get_holidays()
        
        with self.assertRaises(ConnectionError):  # second time mock function gets called, they will behave differently
            get_holidays()

        assert requests.get.call_count == 2
  
if __name__ == "__main__":
    unittest.main()
```

- ***.side_effect*** can set to be function: so it will behave the same as that function, it will also pass the argument too
```py
from unittest import mock
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
    def log_request(self, url):  # here we define the function we want to redirect to, note the argument should be same type as the function being mocked
        print(f"connected to {url}")

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
          '12/25': 'Christmas',
          '7/4': 'Independence Day',
        }

        return response_mock

    def test_get_holidays_retry(self):
        requests.get.side_effect = self.log_request  # here we mock request.get and redirect it to another function
        
        r = get_holidays()
        assert r['12/25'] == "Christmas"

        assert requests.get.call_count == 1
  
if __name__ == "__main__":
    unittest.main()
```
## Scope of Mock
1. Local scope  
### Bad Example 1: mock the library outside the test function (without specifying the affected scope, meaning that all functions in this scope will be affected)
```py
requests = Mock()

def get_holidays():
    print("In function scope: ", requests)
    r = requests.get("http://fakeurl.com")
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):

    def test_get_holidays_1(self):
        # requests = Mock()
        requests.get.side_effect = [Timeout, ConnectionError]
        print("In test scope: ", requests)

        with self.assertRaises(Timeout):
            get_holidays()

    def test_get_holidays_2(self): #因为mock obj被定义在global，所以即使这个test function内部没有定义get，也还是在影响范围内
        with self.assertRaises(ConnectionError):
            get_holidays()

        assert requests.get.call_count == 2
  
if __name__ == "__main__":
    unittest.main()
```
Results:
```py
In test scope:  <Mock id='1606455477640'>
In function scope:  <Mock id='1606455477640'>
.In function scope:  <Mock id='1606455477640'>
```

### Bad Example 2: mock the library inside the function
```py
# requests = Mock() # 这一行不能写在test里，否则会报错

def get_holidays():
    print("In function scope: ", requests)
    r = requests.get("http://fakeurl.com")
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):

    def test_get_holidays_1(self):
        requests = Mock()  # mock object only exists in local scope
        requests.get.side_effect = [Timeout, ConnectionError]
        print("In test scope: ", requests)

        with self.assertRaises(Timeout):
            get_holidays() # 出了这个function，requests mock就不再有效了

    def test_get_holidays_2(self):
        with self.assertRaises(ConnectionError):
            get_holidays()

        assert requests.get.call_count == 2
  
if __name__ == "__main__":
    unittest.main()
```
Results:
```py
In test scope:  <Mock id='1922625937928'>
In function scope:  <module 'requests' from 'C:\\Users\\yye\\AppData\\Roaming\\Python\\Python37\\site-packages\\requests\\__init__.py'>
In function scope:  <module 'requests' from 'C:\\Users\\yye\\AppData\\Roaming\\Python\\Python37\\site-packages\\requests\\__init__.py'>
```
### Good Example: control the scope you wanna impact
1. Using Patch decorator
```py
import main
from unittest.mock import patch # 如果get_holidays在另一个py文件里，则test文件可以不用import requests
from requests.exceptions import Timeout, ConnectionError
from unittest.mock import Mock
import unittest

class TestCalendar(unittest.TestCase):

    @patch("main.requests")
    def test_get_holidays_1(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        print("test_get_holidays_1: ")
        print("In test scope: ", mock_requests)

        with self.assertRaises(Timeout):
            main.get_holidays()

    @patch("main.requests")
    def test_get_holidays_2(self, mock_requests):
        mock_requests.get.side_effect = ConnectionError
        print("test_get_holidays_2: ")
        print("In test scope: ", mock_requests)

        with self.assertRaises(ConnectionError):
            main.get_holidays()

  
if __name__ == "__main__":
    unittest.main()
```
Results:
```py
test_get_holidays_1:
In test scope:  <MagicMock name='requests' id='2229835241224'>
In function scope:  <MagicMock name='requests' id='2229835241224'>
.test_get_holidays_2:
In test scope:  <MagicMock name='requests' id='2229835278920'>
In function scope:  <MagicMock name='requests' id='2229835278920'>
```
