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
