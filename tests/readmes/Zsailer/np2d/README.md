# Np2d: 2-D NumPy operations

2-D arrays are a common data-structure in scientific computing, and there are a few
2-D operations I find myself repeatedly writing in my research. While simple, these operations
are too specific for the general NumPy scope (and thus, do not warrant a pull request to NumPy).
So, I'm collecting a set of fast, 2-D NumPy operations here. Maybe you'll find them
useful too.

## List of functions

### `np2d.random.choice()`

Choose random samples from a 2-D array. Get the samples and their indices.

```python
import numpy as np
import np2d

# Construct a random array
a = np.random.uniform(size=(4,5))

# Construct weights
weights = np.random.random(shape=(4,5))
weights = weights / weights.sum() # normalize

# Sample from a
samples, indices = np2d.random.choice(a, p=weights)
```

### `np2d.kmin()`

Find the `k` smallest elements in the 2-D array.

```python
import numpy as np
import np2d

# Create a random array
a = np.random.uniform(size=(4,5))

# Draw the k smallest values
k = 3
k_smallest_elements, indices = np2d.kmin(a, k)
```


### `np2d.kmax()`

```python
import numpy as np
import np2d

# Create a random array
a = np.random.uniform(size=(4,5))

# Draw the k largest values
k = 3
k_largest_elements, indices = np2d.kmax(a, k)
```

## Installation

To install the latest release from PyPi:
```
pip install np2d
```

To install a development version, clone this repo and install from the command line:
```
pip install -e .
```

## Suggestions

If there is a NumPy function or module you'd like extended to 2-D, or a new NumPy-like operation
you'd like me to add to this package, feel free to open an [Issue](https://github.com/Zsailer/np2d/issues/new).

## Tests

To run tests for np2d, run:

```
nosetests
```
