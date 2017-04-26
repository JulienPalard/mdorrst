# nCephes

[![PyPI-License](https://img.shields.io/pypi/l/ncephes.svg?style=flat-square)](https://pypi.python.org/pypi/ncephes/) [![PyPI-Version](https://img.shields.io/pypi/v/ncephes.svg?style=flat-square)](https://pypi.python.org/pypi/ncephes/) [![Anaconda-Version](https://anaconda.org/conda-forge/ncephes/badges/version.svg)](https://anaconda.org/conda-forge/ncephes) [![Anaconda-Downloads Badge](https://anaconda.org/conda-forge/ncephes/badges/downloads.svg)](https://anaconda.org/conda-forge/ncephes) [![Documentation Status](https://readthedocs.org/projects/ncephes/badge/?style=flat-square&version=latest)](https://ncephes.readthedocs.io/)

This package provides a python interface for the
[Cephes](http://www.netlib.org/cephes/) library.
It also supports [Numba](http://numba.pydata.org) and its ``nopython`` mode.

## Usage

```python
from ncephes import cprob
print(cprob.incbet(1., 3., 0.3))
```
prints ``0.657``.

You can also call them inside a numba function
```python
from ncephes import cprob
from numba import jit

@jit
def numba_incbet(a, b, x):
    return cprob.incbet(a, b, x)

print(numba_incbet(1., 3., 0.3))
```
and with nopython mode and nogil enabled
```python
from ncephes import cprob
from numba import jit

incbet = cprob.incbet

@jit(nogil=True, nopython=True)
def numba_incbet(a, b, x):
    return incbet(a, b, x)

print(numba_incbet(1., 3., 0.3))
```

One can also statically link the compiled Cephes libraries `ncprob` and
`ncellf`. Please, have a peek at the `examples/prj_name` for a minimalistic
example.

## Install

The recommended way of installing it is via
[conda](http://conda.pydata.org/docs/index.html)
```bash
conda install -c conda-forge ncephes
```

An alternative way would be via pip
```bash
pip install ncephes
```

## Running the tests

After installation, you can test it
```
python -c "import ncephes; ncephes.test()"
```
as long as you have [pytest](http://docs.pytest.org/en/latest/).

## Authors

* **Danilo Horta** - [https://github.com/Horta](https://github.com/Horta)

## License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details
