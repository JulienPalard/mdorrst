istruct
=======
Immutable struct built on top of ``collections.namedtuple`` with sane defaults

Goals
-----
- Immutable, dictionary-like data structure (Note: ``istruct`` is *not* an immutable version of the existing ``struct`` in Python)
- Minimal
- Support required *and* optional fields (with default values)
- Strictly disallow positional arguments

Installation
------------

``pip install istruct``

Quick Start
-----------
First, create an ``istruct`` object called ``person`` where ``first_name`` and ``last_name`` are *required* whereas ``middle_name``, ``dob`` and ``email`` are *optional* (with default values specified).

.. code-block::

    >>> from istruct import istruct
    >>> person = istruct("first_name", "last_name", middle_name="", dob="2000-01-01", email=None)

Then, create an instance of ``person`` with ``first_name``, ``last_name`` and ``middle_name``.

.. code-block::

    >>> p = person(first_name="Jim", last_name="Raynor", middle_name="Eugene")
    >>> p
    istruct(first_name='Jim', last_name='Raynor', email=None, dob='2000-01-01', middle_name='Eugene')

You can retrieve field values like you would normally do.

.. code-block::

    >>> p.first_name
    'Jim'
    >>> p.dob
    '2000-01-01'

``p`` is immutable, meaning that it cannot be modified after created. Thus, set/delete operations like below would fail, raising an ``AttributeError``.

.. code-block::

    >>> p.first_name = "James"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: can't set attribute
    >>> del p.email
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: can't delete attribute

``istruct`` only accepts named/keyword arguments. It strictly disallows positional arguments by design.

.. code-block::

    >>> p = person("Jim", "Raynor")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Users/microamp/src/microamp/istruct/istruct/__init__.py", line 52, in _istruct
        "(%d found)" % (len(positional),))
    TypeError: No positional arguments are allowed in istruct (2 found)

``istruct`` would raise a ``TypeError`` when one or more *required* fields are omitted.

.. code-block::

    >>> p = person(last_name="Raynor")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Users/microamp/src/microamp/istruct/istruct/__init__.py", line 56, in _istruct
        return nt(**merge_dicts(kwargs, attrs))
    TypeError: __new__() missing 1 required positional argument: 'first_name'

Versions Tested
---------------
- Python 2.7
- Python 3.2
- Python 3.3
- Python 3.4
- Python 3.5
- Python 3.6
- PyPy
- PyPy3

TODO
----
- Find ways to annotate types

License
-------
MIT
