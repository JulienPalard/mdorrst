A Theano-based Python implementation of factorization machines, based on
the model presented in *Factorization Machines* (Rendle 2010).

Features
--------

-  Sample weighting
-  For binary classification, this implementation uses a logit function
   combined with a cross entropy loss function.
-  Extensibility of algorithms for: regularization, loss function optimization, and the error function

Installation
------------

`pyfms <https://pypi.python.org/pypi/pyfms>`__ is available on PyPI, the Python Package Index.

::

    $ pip install pyfms

Documentation
-------------

See `documentation.md <https://github.com/dstein64/PyFactorizationMachines/blob/master/documentation.md>`__.

Example Usage
-------------

See `example.py <https://github.com/dstein64/PyFactorizationMachines/blob/master/example.py>`__.

License
-------

PyFactorizationMachines has an `MIT License <https://en.wikipedia.org/wiki/MIT_License>`__.

See `LICENSE <https://github.com/dstein64/PyFactorizationMachines/blob/master/LICENSE>`__.

Acknowledgments
---------------

RMSprop code is from
`Newmu/Theano-Tutorials <https://github.com/Newmu/Theano-Tutorials/blob/master/4_modern_net.py>`__.

References
----------

Rendle, S. 2010. “Factorization Machines.” In 2010 IEEE 10th
International Conference on Data Mining (ICDM), 995–1000.
doi:10.1109/ICDM.2010.127.
