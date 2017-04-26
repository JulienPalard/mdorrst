[![Travis](https://img.shields.io/travis/w1sm3rhi11/pycol.svg)](https://travis-ci.org/w1sm3rhi11/pycol)
[![Code Climate Coverage](https://img.shields.io/codeclimate/coverage/github/w1sm3rhi11/pycol.svg)](https://codeclimate.com/github/w1sm3rhi11/pycol)
[![Code Climate Rank](https://img.shields.io/codeclimate/github/w1sm3rhi11/pycol.svg)](https://codeclimate.com/github/w1sm3rhi11/pycol)
[![Code Climate Issues](https://img.shields.io/codeclimate/issues/github/w1sm3rhi11/pycol.svg)](https://codeclimate.com/github/w1sm3rhi11/pycol)
[![PyPI Version](https://img.shields.io/pypi/v/pycol.svg)](https://pypi.python.org/pypi/pycol)
[![PyPI Python](https://img.shields.io/pypi/pyversions/pycol.svg)](https://pypi.python.org/pypi/pycol)
[![PyPI Status](https://img.shields.io/pypi/status/pycol.svg)](https://pypi.python.org/pypi/pycol)
[![Waffle.io Ready](https://img.shields.io/waffle/label/w1sm3rhi11/pycol/ready.svg)](http://waffle.io/w1sm3rhi11/pycol)
[![Waffle.io In Progress](https://img.shields.io/waffle/label/w1sm3rhi11/pycol/in%20progress.svg)](http://waffle.io/w1sm3rhi11/pycol)

pycol is a collections framework for python 3.3+ usable in a fluent way,
inspired by the [eclipse-collections](https://github.com/eclipse/eclipse-collections) project.
All collections methods are using iterators for lazy evaluation.

# Installation

The easiest and preferred way is to run `pip install pycol`.
Otherwise you can download the sources on the [pypi repository](https://pypi.python.org/pypi/pycol),
extract the tar.gz archive and run `python setup.py install`

# Examples

```python
from pycol.factory import *
from collections.abc import Mapping
import json
import operator

# All collections.abc.Collection implementations are supported such as list, tuple, set, frozenset, etc.

# 1. reject all elements lower than 20 == [88, 22]
# 2. divide each of them by 2 == [44, 11]
# 3. evaluate if they all are greater than 10 == True (final result)
iterable([1, 88, 12, 10, 22]).reject(operator.lt, 20).map(lambda el: el / 2).all_satisfy(operator.gt, 10)

# 1. select all int greater than 10 == [108, 22]
# 2. print them
select({108, 1, 10, 22, 'foo', -15}, lambda el: isinstance(el, int) and el > 10).each(print)

# print indented json output of each dictionary in the list:
map_(({'a': 1, 'b': {'b1': 10, 'b2': 11}}, {'foo': 'bar'}), json.dumps, indent=2).each(print)

# All collections.abc.Mapping implementations are supported such as dict, defaultdict, UserDict etc.

# 1. reject items value that are a Mapping object == {'a': 1, 'b': 2, 'd': 'foo'}
# 2. multiply by 4 items value == {'a': 4, 'b': 8, 'd': 'foofoofoofoo'}
# 3. map items value to be {'val': <value>} == {'a': {'val': 4},
#                                               'b': {'val': 8},
#                                               'd': {'val': 'foofoofoofoo'}} (final result)
d = reject({'a': 1, 'b': 2, 'c': {'x': 100, 'y': -4}, 'd': 'foo'}, isinstance, Mapping)\
        .map(operator.mul, 4).map(lambda v: {'val': v})
print(dict(d)) # or defaultdict(d) or any other collections.abc.Mapping implementations
```

# Tests

See tests under the test package for more examples

To run the tests:

1. `pip install pytest` in a virtual environment
1. Go to the project folder and run py.test
1. (For developers only) `pip install pytest-cov` and run `py.test -v --cov pycol --cov-report term-missing` instead

# Developer notes

* (*optional*) Translate README.md to README.rst with `pandoc --from=markdown --to=rst --output=README.rst README.md`
* Create a distribution with `python setup.py sdist bdist_wheel`
* Sign the distribution with `gpg --detach-sign -a dist/<dist_name>`
* Upload the distribution with `twine upload [-r <repo>] dist/<dist_name> dist/<dist_name>.asc`
