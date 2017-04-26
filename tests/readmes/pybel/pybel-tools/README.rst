PyBEL Tools |develop_build| |develop_coverage| |develop_documentation| |pypi_license|
=====================================================================================
`PyBEL Tools <http://pybel-tools.readthedocs.io/>`_ is a suite of tools built on top of
`PyBEL <http://pybel.readthedocs.io>`_ to facilitate data management, integration, and analysis.

This package was developed at `Fraunhofer SCAI <https://www.scai.fraunhofer.de/>`_
with support from the `IMI <https://www.imi.europa.eu/>`_ projects: `AETIONOMY <http://www.aetionomy.eu/>`_ and
`PHAGO <http://www.phago.eu/>`_.

Installation |pypi_version| |python_versions|
---------------------------------------------
PyBEL Tools can be installed easily from `PyPI <https://pypi.python.org/pypi/pybel_tools>`_ with the following code in
your favorite terminal:

.. code-block:: sh

    $ python3 -m pip install pybel_tools

or from the latest code on `GitHub <https://github.com/pybel/pybel-tools>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/pybel/pybel-tools.git@develop

Getting Data
------------
Before running the service, some data can be pre-loaded in your cache.

Loading Selventa Corpra
~~~~~~~~~~~~~~~~~~~~~~~
The Selventa Small Corpus and Large Corpus are two example BEL documents distributed by the
`OpenBEL framework <https://wiki.openbel.org/display/home/Summary+of+Large+and+Small+BEL+Corpuses>`_. They are good
examples of many types of BEL statements and can be used immediately to begin exploring. Add :code:`-v` for more
logging information during compilation. This is highly suggested for the first run, since it takes a while to cache
all of the namespaces and annotations. This only has to be done once, and will be much faster the second time!

Small Corpus:

.. code-block:: sh

    $ python3 -m pybel_tools ensure small_corpus -v

Large Corpus:

.. code-block:: sh

    $ python3 -m pybel_tools ensure large_corpus -v

Uploading Precompiled BEL
~~~~~~~~~~~~~~~~~~~~~~~~~
A single network stored as a PyBEL gpickle can quickly be uploaded using the following code:

.. code-block:: sh

    $ python3 -m pybel_tools io upload -p /path/to/my_network.gpickle

More examples of getting data into the cache can be found `here <http://pybel-tools.readthedocs.io/en/latest/cookbook.html#getting-data-in-to-the-cache>`_.

Web Services
------------
PyBEL Tools deploys a Flask web application that allows you to interact with your networks and apply filters/algorithms.

Multiple services are available. Use :code:`--help` for a description. To run the web services, type:

.. code-block:: sh

    $ python3 -m pybel_tools web

By default, Flask deploys on ``localhost`` at port ``5000``. These can be changed respectively with the ``--host`` and
``--port`` arguments. Additionally, logging can be shown with ``-v``. More documentation on the web services can be found `here <http://pybel-tools.readthedocs.io/en/latest/web.html>`_.

Documentation and Examples
--------------------------
- Documentation at http://pybel-tools.readthedocs.io
- Cookbook at https://github.com/pybel/pybel-notebooks

Links
-----
- Documented on `Read the Docs <http://pybel-tools.readthedocs.io/>`_
- Versioned on `GitHub <https://github.com/pybel/pybel-tools>`_
- Tested on `Travis CI <https://travis-ci.org/pybel/pybel-tools>`_
- Distributed by `PyPI <https://pypi.python.org/pypi/pybel-tools>`_
- Chat on `Gitter <https://gitter.im/pybel/Lobby>`_

.. |develop_build| image:: https://travis-ci.org/pybel/pybel-tools.svg?branch=develop
    :target: https://travis-ci.org/pybel/pybel-tools
    :alt: Development Build Status

.. |develop_coverage| image:: https://codecov.io/gh/pybel/pybel-tools/coverage.svg?branch=develop
    :target: https://codecov.io/gh/pybel/pybel-tools?branch=develop
    :alt: Development Coverage Status

.. |develop_documentation| image:: https://readthedocs.org/projects/pybel-tools/badge/?version=latest
    :target: http://pybel-tools.readthedocs.io/en/latest/
    :alt: Development Documentation Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/pybel-tools.svg
    :alt: Stable Supported Python Versions

.. |pypi_version| image:: https://img.shields.io/pypi/v/pybel-tools.svg
    :alt: Current version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/pybel-tools.svg
    :alt: Apache 2.0 License
