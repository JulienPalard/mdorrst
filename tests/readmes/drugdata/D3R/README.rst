======================================
Drug Design Data Resource CELPP Runner
======================================

.. image:: https://img.shields.io/travis/drugdata/D3R.svg
        :target: https://travis-ci.org/drugdata/D3R.svg?branch=master

.. image:: https://img.shields.io/pypi/v/D3R.svg
        :target: https://pypi.python.org/pypi/D3R
        
.. image:: https://coveralls.io/repos/github/drugdata/D3R/badge.svg?branch=master 
        :target: https://coveralls.io/github/drugdata/D3R?branch=master


Drug Design Data Resource is a suite of software to enable 
filtering, docking, and scoring of new sequences from 
`wwpdb <http://www.wwpdb.org/>`_.

For more information please visit our wiki page:

https://github.com/drugdata/d3r/wiki


Compatibility
-------------

 * Works with Python 2.6, 2.7


Dependencies
------------

 * `argparse <https://pypi.python.org/pypi/argparse>`_
 * `lockfile <https://pypi.python.org/pypi/lockfile>`_
 * `psutil <https://pypi.python.org/pypi/psutil>`_
 * `biopython <https://pypi.python.org/pypi/biopython>`_
 * `xlsxwriter <https://pypi.python.org/pypi/xlsxwriter>`_
 * `ftpretty <https://pypi.python.org/pypi/ftpretty>`_
 * `NCBI Blast <https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download>`_ (needed by blastnfilter.py)
 * `rdkit <http://www.rdkit.org/>`_ (needed by blastnfilter.py and proteinligprep.py)
 * `schrodinger <https://www.schrodinger.com/>`_ (needed by proteinligprep.py, glidedocking.py, chimera_proteinligprep.py & vinadocking.py)
 * `babel <http://openbabel.org/wiki/Main_Page>`_ (needed by chimera_proteinligprep.py)
 * `Autodock Vina <http://vina.scripps.edu/>`_ & `MGL Tools <http://mgltools.scripps.edu/downloads>`_ (needed by vinadocking.py)


Installation
------------

.. code:: bash

  pip install d3r

Usage
-----

Run

.. code:: bash
  
  celpprunner.py --help


License
-------

See LICENSE.txt_

Bugs
-----

Please report them `here <https://github.com/drugdata/D3R/issues>`_


Acknowledgements
----------------

* This work is funded in part by NIH grant 1U01GM111528 from the National Institute of General Medical Sciences

* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _LICENSE.txt: https://github.com/drugdata/D3R/blob/master/LICENSE.txt 
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
