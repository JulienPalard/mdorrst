# Logerator
A Python package that contains the decorator, `before_and_after`. The decorator implements before and after event logging using the Python Logentries package


## Installation
 
 * Install the file.
 
 `pip install logerator`
 
 * Make sure you have an log setup on Logentries.
 
 * Add your API key to the environment variable,  `LOGENTRIES_TOKEN`

`LOGENTRIES_TOKEN=MY_LOGENTRIES_API_KEY`

 * Set the environment variable `PRINT_BEFORE_AND_AFTER` to `true` should you want the decorator the send logging information to console
 
 `PRINT_BEFORE_AND_AFTER = true`
 
## Usage
 
```python
from logerator import before_and_after

 
@before_and_after
def turn_to_upper(strng):
    return str(strng).upper()
```
Result of decorator: Two entries to the logentries log: an entry `before` executing, `upper()`, and an entry `after` executing `.upper()`.
 
```python
Sat Apr 22 17:07:05 PDT 2017 : INFO, {"args": {"py/tuple": ["some lower case data"]}, "event": "before", "filename": "/Users/reselbob/Documents/source-tree/logerator/tests/test_logerator.py", "function": "turn_to_upper", "kwarg": {}, "line_number": 7}
Sat Apr 22 17:07:05 PDT 2017 : INFO, {"args": {"py/tuple": ["some lower case data"]}, "event": "after", "filename": "/Users/reselbob/Documents/source-tree/logerator/tests/test_logerator.py", "function": "turn_to_upper", "kwarg": {}, "line_number": 7, "result": "SOME LOWER CASE DATA"}


```