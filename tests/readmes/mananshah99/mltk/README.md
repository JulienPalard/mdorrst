# mltk: A Machine Learning Toolkit ([docs](http://mltk.rtfd.io))
[![Build Status](https://travis-ci.org/mananshah99/mltk.svg?branch=master)](https://travis-ci.org/mananshah99/mltk) [![Documentation Status](https://readthedocs.org/projects/mltk/badge/?version=latest)](http://mltk.readthedocs.io/en/latest/?badge=latest) [![Coverage Status](https://coveralls.io/repos/github/mananshah99/mltk/badge.svg?branch=master)](https://coveralls.io/github/mananshah99/mltk?branch=master) [![PyPI version](https://badge.fury.io/py/mltk.svg)](https://badge.fury.io/py/mltk) 

mltk is a library of utilities dedicated to streamlining the 
analysis of supervised and unsupervised classifiers. Built on 
top of common libraries including `numpy`, `scipy`, and supporting
functions from `sklearn`, mltk includes methods to visualize,
analyze, and optimize existing models in a more efficient manner. 

Starting with `mltk` is quite simple: simply install the latest 
release from PyPI with `pip install mltk` and begin development
with 

```python
# import any one of the sub-directories of mltk
from mltk.metrics import * 

# use exposed functionality within parameter requirements
print auc([0,1], [.5, .5])
```
Installation
------------

Install mltk by running

    $> pip install mltk

Contribute
----------

- Issue Tracker: https://github.com/mananshah99/mltk/issues 
- Source Code: https://github.com/mananshah99/mltk/

Support
-------

If you are having issues, please let me know at manan.shah.777@gmail.com

License
-------

The project is licensed under the MIT license.

