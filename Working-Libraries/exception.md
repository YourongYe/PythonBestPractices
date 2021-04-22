# Create custom exception class
```py
class RecordAlreadyExistsError(Exception):
    pass
```

# Raise exception in a script
```py
if self.id == None:
    raise ValueError('id should not be None')
```
# Use try except to raise an exception
### A simple way of raising whatever exception it is
```py
try:
    response.raise_for_status()  # raise_for_status() this function will 
except:
    raise
```
### If you wanna catch specific exception:
```py
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(error)
    raise AnotherError("this is another error defined by yourself")
```
### Chaining exception 
If you want to have both the generic error (built-in exceptions like ValueError) and your custom error (e.g RequestIdFailedError) at the same time,   
so that people who get the error have more info for debugging

```py
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(error)
    raise OtherError(str(error)) from error
```
