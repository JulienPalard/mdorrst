typepy
======

.. image:: https://badge.fury.io/py/typepy.svg
    :target: https://badge.fury.io/py/typepy

.. image:: https://img.shields.io/pypi/pyversions/typepy.svg
   :target: https://pypi.python.org/pypi/typepy

.. image:: https://img.shields.io/travis/thombashi/typepy/master.svg?label=Linux
    :target: https://travis-ci.org/thombashi/typepy

.. image:: https://img.shields.io/appveyor/ci/thombashi/typepy/master.svg?label=Windows
    :target: https://ci.appveyor.com/project/thombashi/typepy

.. image:: https://coveralls.io/repos/github/thombashi/typepy/badge.svg?branch=master
    :target: https://coveralls.io/github/thombashi/typepy?branch=master

.. image:: https://img.shields.io/github/stars/thombashi/typepy.svg?style=social&label=Star
   :target: https://github.com/thombashi/typepy

Summary
-------

A python library for variable type checker/validator/converter at run time.

Usage
=====

Type Check Method
----------------------

.. code:: pycon

    >>> from typepy.type import Integer
    >>> Integer(1).is_type()
    True
    >>> Integer(1.1).is_type()
    False


Type Validation Method
--------------------------------------------

.. code:: pycon

    >>> from typepy.type import Integer
    >>> Integer(1).validate()
    >>> try:
    ...     Integer(1.1).validate()
    ... except TypeError as e:
    ...     print(e)
    ...
    invalid value type: expected=INTEGER, actual=<type 'float'>


Type Conversion Methods
--------------------------------------------

convert
~~~~~~~~~~~~~~
.. code:: pycon

    >>> from typepy.type import Integer
    >>> from typepy import TypeConversionError
    >>> Integer("1").convert()
    1
    >>> try:
    ...     Integer(1.1).convert()
    ... except TypeConversionError as e:
    ...     print(e)  # convert method will raise TypeConversionError when conversion failed
    ...
    failed to convert from float to INTEGER

try_convert
~~~~~~~~~~~~~~
.. code:: pycon

    >>> from typepy.type import Integer
    >>> Integer("1").try_convert()
    1
    >>> print(Integer(1.1).try_convert())  # try_convert method will return None when conversion failed
    None

force_convert
~~~~~~~~~~~~~~
.. code:: pycon

    >>> from typepy.type import Integer
    >>> Integer("1").force_convert()  # force_convert will forcibly convert the value
    1
    >>> Integer(1.1).force_convert()
    1

For more information
====================

Type check/validate/convert results will be changed according to
``strict_level`` value which can be passed to constructors as an argument.
More information can be found in the 
`API reference <http://typepy.rtfd.io/en/latest/pages/reference/index.html>`__.

Features
========

The association between Python types and typepy classes is as follows:

==================  =======================================================================================================
Python Type         typepy Class
==================  =======================================================================================================
``bool``            `Bool <http://typepy.rtfd.io/en/latest/pages/reference/type.html#bool-type-class>`__
``datetime``        `DateTime <http://typepy.rtfd.io/en/latest/pages/reference/type.html#datetime-type-class>`__
``dict``            `Dictionary <http://typepy.rtfd.io/en/latest/pages/reference/type.html#dictionary-type-class>`__
``inf``             `Infinity <http://typepy.rtfd.io/en/latest/pages/reference/type.html#infinity-type-class>`__
``int``             `Integer <http://typepy.rtfd.io/en/latest/pages/reference/type.html#integer-type-class>`__
``float``           `RealNumber <http://typepy.rtfd.io/en/latest/pages/reference/type.html#real-number-type-class>`__
``NaN``             `Nan <http://typepy.rtfd.io/en/latest/pages/reference/type.html#nan-type-class>`__
``None``            `None <http://typepy.rtfd.io/en/latest/pages/reference/type.html#none-type-class>`__
``str`` (not null)  `String <http://typepy.rtfd.io/en/latest/pages/reference/type.html#string-type-class>`__
``str`` (null)      `NullString <http://typepy.rtfd.io/en/latest/pages/reference/type.html#null-string-type-class>`__
==================  =======================================================================================================

Installation
============

::

    pip install typepy


Dependencies
============
Python 2.7+ or 3.3+

- `mbstrdecoder <https://github.com/thombashi/mbstrdecoder>`__
- `python-dateutil <https://dateutil.readthedocs.io/en/stable/>`__
- `pytz <https://pypi.python.org/pypi/pytz/>`__
- `six <https://pypi.python.org/pypi/six/>`__


Test dependencies
-----------------
- `pytest <http://pytest.org/latest/>`__
- `pytest-runner <https://pypi.python.org/pypi/pytest-runner>`__
- `tox <https://testrun.org/tox/latest/>`__

Documentation
=============

http://typepy.rtfd.io/

