bhasa
######

.. image:: https://badge.fury.io/py/bhasa.svg
    :target: https://badge.fury.io/py/bhasa
    
.. image:: https://travis-ci.org/hanmajid/bhasa.svg?branch=master
   :target: https://travis-ci.org/hanmajid/bhasa

.. image:: https://codecov.io/gh/hanmajid/bhasa/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/hanmajid/bhasa

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
   :target: https://github.com/hanmajid/bhasa/blob/master/LICENSE

Installation
-------------
You can install bhasa with pip::

    $ pip install bhasa


You can test the installation in Python console::

    >>> import bhasa
    >>> print bhasa.smile()

Features
---------
1. Spelling

We are currently using Peter Norvig's `article <http://norvig.com/spell-correct.html>`_ as a reference. But since it's using English, we'll update it to Bahasa soon.
Usage::

    >>> from bhasa.spell import correction
    >>> correction('typwriter')
    'typewriter'

Development
------------
1. Clone this repository::
    
    $ git clone https://github.com/hanmajid/bhasa.git bhasa
2. Go into the folder::

    $ cd bhasa
3. We recommend using `Miniconda <https://conda.io/miniconda.html>`_ for package manager. Download and install Miniconda on your computer, and create a new environment::

    $ conda env create -f environment.yml
    
4. Activate the environment::
    
    # Linux/Mac OS
    $ source activate bhasa_env

    # Windows
    $ activate bhasa_env

Testing
------------
We use `coverage <https://coverage.readthedocs.io/en/coverage-4.3.4/>`_ for testing. You can run test with::
    
    $ coverage run bhasa/tests/tests.py
