# PyLU

Small nogil-compatible Cython-based solver for linear equation systems `A x = b`.


## Introduction

The algorithm is LU decomposition with partial pivoting (row swaps). The code requires only NumPy and Cython.

The main use case for PyLU (over `numpy.linalg.solve`) is solving many small systems inside a `nogil` block in Cython code, without requiring SciPy (for its `cython_lapack` module).

Python and Cython interfaces are provided. The API is designed to be as simple to use as possible.

The arrays are stored using the C memory layout.

A rudimentary banded solver is also provided, based on detecting the band structure (if any) from the initial full LU decomposition. For cases where `L` and `U` have small bandwidth, this makes the `O(n**2)` solve step run faster. The LU decomposition still costs `O(n**3)`, so this is useful only if the system is small, and the same matrix is needed for a large number of different RHS vectors. (This can be the case e.g. in integration of ODE systems with a constant-in-time mass matrix.)


## Examples

Basic usage:

```python
import numpy as np
import pylu

A = np.random.random( (5,5) )
b = np.random.random( 5 )

x = pylu.solve( A, b )
```

For a complete tour, see [`pylu_test.py`](test/pylu_test.py).

The main item of interest, however, is the Cython API in [`dgesv.pxd`](pylu/dgesv.pxd). The main differences to the Python API are:

 - Function names end with `_c`.
 - Explicit sizes must be provided, since the arrays are accessed via raw pointers.
 - The result array `x` must be allocated by the caller, and passed in as an argument. See [`dgesv.pyx`](pylu/dgesv.pyx) for examples on how to do this in NumPy.


## Installation

### From PyPI

Install as user:

```bash
pip install pylu --user
```

Install as admin:

```bash
sudo pip install pylu
```

### From GitHub

As user:

```bash
git clone https://github.com/Technologicat/pylu.git
cd pylu
python setup.py install --user
```

As admin, change the last command to

```bash
sudo python setup.py install
```


## Dependencies

- [NumPy](http://www.numpy.org)
- [Cython](http://www.cython.org)


## License

[BSD](LICENSE.md). Copyright 2016-2017 Juha Jeronen and University of Jyväskylä.


#### Acknowledgement

This work was financially supported by the Jenny and Antti Wihuri Foundation.

