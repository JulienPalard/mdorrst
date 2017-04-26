filecho
=======

.. image:: https://img.shields.io/badge/license-Apache 2-blue.svg
    :target: https://github.com/jadbin/filecho/blob/master/LICENSE


Overview
--------

A web server for serving static files based on `aiohttp`_.


Requirements
------------

- Python >= 3.5
- `aiohttp`_

.. _aiohttp: https://pypi.python.org/pypi/aiohttp


Installation
------------

You can install filecho from PyPI with:

::

    $ pip install filecho


Usage
-----

Run web server with:

::

    $ filecho -d DIR -p PORT

where ``DIR`` is the root directory of static files, ``PORT`` is the serving port.
The default serving port is ``80`` without setting ``-p``.


By the way, you can view the help message for usage with:

::

    $ filecho -h

