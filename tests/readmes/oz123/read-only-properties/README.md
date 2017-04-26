Python Read Only Property
=========================

Background:
-----------

 > Generally, Python programs should be written with the assumption that
 > all users are consenting adults, and thus are responsible for using things
 > correctly themsel0aves.

[Silas Ray][1] in Stackoverflow. Thus, generally speaking, Python doesn't hide
much. There is no notion of `private` vs. `public` in Python, hence everything
is writable.

But what if you or users of your code forget?
What if you really can't assume everyone is ?

Do we give up on having read only properties in Python?

Short introduction:
-------------------
This module allows you to make class attribute read only, with needing to
use `@property` or `__getattr__`.

Why not use `@property`?

Because it's verbose, and you need to create a function which returns
something.

```
    class MyClass:

        @property
        def a(self):
            return 1

```

The above can be shortened:

```
@read_only_properties('a')
class MyClass(object):
    def __init__(self, a, b, c):
        self.readonly = a
```

Once assigned in the constructor, you can't change it.

Usage:
------

This package installs a single Python module `rop.py`, containing a single
decorator `read_only_properties`. To use it, simply import the decorator and
decorate your classes.

```
from rop import read_only_properties

@read_only_properties('b')
class Foo:
    def __init__(self, a, b):
        self.a
        self.b
```


Moving from @property:
----------------------

If you have a class with many attributes that you want to
refactor to properties:

```
class AClassWithManyAttributes:
    def __init__(a, b, c, d, e ...)
        self.a = a
        self.b = b
        self.c = c
```

The above class would be very verbose (an IDE will save you a lot of
typing, but it won't make the code shorter:

```
class AClassWithManyAttributes:
    '''refactored to properties'''
    def __init__(a, b, c, d, e ...)
        self._a = a
        self._b = b
        self._c = c
    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b
    @property
    def b(self):
        return self._c
    # you get this ... it's long

```

Now imagine you can simply do that:

```
@read_only_properties('a', 'b', 'c')
class AClassWithManyAttributes:
     def __init__(a, b, c, d, e)
         self.a = a
         self.b = b
         self.c = c
         self.d = d
         self.e = e
```

This makes the attributes `a, b, c` read only, trying to re-assign a value
to any of them will raise an exception, other class attribute stay unaffected.


The code for this module originated from the
[author's answer in stackoverflow][2].


[1]: http://stackoverflow.com/a/14594174/492620
[2]: http://stackoverflow.com/a/35906068/492620
