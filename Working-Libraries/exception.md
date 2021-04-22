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
```py
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print(error)
    raise OtherError(str(error)) from error
```
