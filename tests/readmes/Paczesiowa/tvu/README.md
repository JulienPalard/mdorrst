# Type Value Unifier

# Intro
tvu library allows you to abstract code, that is usually present at the beginning of most
functions/methods, and handles parameter checking, validation and unification.
The goal is to share most of this code to be usable with many functions and
provide helpful exceptions to users of your code. tvu does not force you
to use all of available type-checking, unification and validation features,
if you don't need them.

```python
import tvu
```

# Typechecking
## Rationale
The following code:

```python
def foo(x, y):
    ....
    m = re.match(y, 'bar')
    ...

foo(None, 2)
```

Results in an exception that is thrown from re.match(), but the user-error
was made when calling foo() with int instead of string. It would be more
user-friendly to get an exception, at the exact place error was made,
that mentions specifically what was the problem.

## Usage
Most basic feature of tvu is simple type-checking of function/method's arguments.
This is the simplest tvu, that checks if function argument is an integer:

```python
class IntTVU(tvu.TVU):
    TYPES = (int,)
```

To actually use it, you can use whole tvu module as a function decorator,
with previously defined IntTVU as value of parameter x (it must match
function argument name):
```python
@tvu(x=IntTVU)
def foo(x):
    print "I'm an integer %d" % x
```

If foo() is called with int parameter it work as expected, but calling it
with anything else results in a nice exception:

```
>>> foo('3')
Traceback (most recent call last):
  File "test.py", line 12, in <module>
    foo('3')
  File "/tmp/tvu-0.1/tvu/_tvu.py", line 70, in inner_wrapper
    validator(arg).unify_validate(args_values[arg])
  File "/tmp/tvu-0.1/tvu/_tvu.py", line 38, in unify_validate
    self.type_check()
  File "/tmp/tvu-0.1/tvu/_tvu.py", line 34, in type_check
    raise TypeError(err_msg)
TypeError: x must be int, not '3'
```

This case of checking if argument is instance of one specific type can be done
with a instance wrapper:

```python
@tvu(x=tvu.instance(int))
def foo(x):
    print "I'm an integer %d" % x
```

Subclasses of TVU can provide more types in TYPES tuple, to check arguments
against more available types:

```python
class NumberTVU(tvu.TVU):
    TYPES = (int, float)

@tvu(x=NumberTVU)
def double(x):
    return 2 * x
```
# Unification
The goal of unification is to allow wider selection of types as a function's argument,
but to unify them to a common value/type before supplying it to a function.

For example, in python2 you might need a unicode text argument, but don't want 
to discourage use of plain strings when they are ascii-only. The following TVU
allows you to think only about unicode values but still allow ascii byte strings:

```python
class Text(tvu.TVU):

    TYPES = (unicode, str)

    def unify(self, value):
        if isinstance(value, str):
            try:
                return value.decode('ascii')
            except UnicodeDecodeError:
                self.error(u'unicode text, or ascii-only bytestring')
        return value

@tvu(x=Text)
def write(x):
    with open('/tmp/text.txt', 'wb') as f:
        f.write(x.encode('utf-8'))

write(u'żółw')
write('ascii')
```

Better version of Text is available as tvu.tvus.Text

# Validation
Validation is about validating function's arguments to restrict value space.
The following TVU disallows non-positive integers:

```python
class PositiveInt(tvu.TVU):
    TYPES = (int,)

    def validate(self, value):
        if value <= 0:
            self.error('positive number')
```

# FAQ
* **How to install it?**

pip install tvu
* **But python is about duck typing?**

There's nothing stopping you from using tvu in duck typing way by checking existence of
certain methods in TVU.validate() method.
* **Does it work with python3?**

tvu has been tested with python-2.7 and python-3.6
