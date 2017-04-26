symfeat
=======

.. image:: https://travis-ci.org/Ohjeah/symfeat.svg?branch=master
    :target: https://travis-ci.org/Ohjeah/symfeat
.. image:: https://badge.fury.io/py/symfeat.svg
    :target: https://badge.fury.io/py/symfeat
.. image:: https://img.shields.io/pypi/pyversions/symfeat.svg
    :target: https://pypi.python.org/pypi/symfeat/
.. image:: https://zenodo.org/badge/79949716.svg
    :target: https://zenodo.org/badge/latestdoi/79949716
    

**symfeat** is a rule based feature engineering library to be used as a
preprocessor for regression tasks.

It is based on:

    Mcconaghy, T. (2011). FFX: Fast, Scalable, Deterministic Symbolic Regression Technology. Genetic Programming Theory and Practice IX, 235-260. `DOI: 10.1007/978-1-4614-1770-5\_13 <http://dx.doi.org/10.1007/978-1-4614-1770-5_13>`_


Features
--------
- Builds a features based on all valid rule specified combinations
- Discards non-finite transformations
- Remove equivalent based on expressions or numeric values


Installation
------------

``pip install symfeat``


Usage
-----

.. code-block:: python

    import numpy as np
    import symfeat as sf

    operators = {"sin": np.sin}
    exponents = [1, 2, -1, -2]

    x = np.random.normal(size=10).reshape(-1, 1)

    sym = sf.SymbolicFeatures(exponents=exponents, operators=operators)
    features = sym.fit_transform(x)
    names = sym.names
