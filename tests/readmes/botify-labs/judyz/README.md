# judyz

judyz is another (pair of) Python wrapper(s) for the [Judy](http://judy.sourceforge.net/)
library.

It implements both a [CFFI](https://cffi.readthedocs.org/) and a [Cython](http://http://cython.org/)
wrapper.

Note that the Cython wrapper is currently unmaintained: it doesn't work with PyPy, unlike CFFI.

`judyz-cython` must be compiled, unlike `judyz-cffi`.

## Compilation Requirements

* libjudy-dev
* cython
* libffi-dev
* python-cffi (or pypy)
* ...


## Distribution

`judyz-cffi` is distributed as source:

    python setup.py sdist

`judyz_cython` can be distributed as an egg:

    python setup.py bdist_egg

To compile `judyz-cython` inplace:

```
cd src/judycython
python setup.py build_ext -i
cd ../..
nosetests
```

## Installation From Local Build

If `pip install` doesn't work:
`pip install --pre --no-index --find-links .../judyz/src/judyzcffi/dist/judyz_cffi-0.1.tar.gz judyz-cffi`

`easy_install .../judyz/src/judyzcython/dist/judyz_cython-0.1-py2.7-linux-x86_64.egg`


## Usage Requirements

* libjudydebian1 (not the Ubuntu 14.04 buggy one)
* `judyz-cffi`: libffi6
