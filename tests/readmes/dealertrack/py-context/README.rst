==========
Py-Context
==========

.. image:: https://badge.fury.io/py/py-context.png
    :target: http://badge.fury.io/py/py-context

.. image:: https://travis-ci.org/dealertrack/py-context.png?branch=master
    :target: https://travis-ci.org/dealertrack/py-context

.. image:: https://coveralls.io/repos/dealertrack/py-context/badge.png?branch=master
    :target: https://coveralls.io/r/dealertrack/py-context?branch=master

Python dict with stacked context data

* Free software: MIT license
* GitHub: https://github.com/dealertrack/py-context

Installing
----------

You can install ``py-context`` using pip::

    $ pip install py-context

Example
-------

::

    >>> context = Context({"user": "Fred", "city": "Bedrock"})
    >>> context['user']
    'Fred'
    >>> context['city']
    'Bedrock'
    >>> context.push({"user": "Barney"})
    >>> context['user']
    'Barney'
    >>> context['city']
    'Bedrock'
    >>> context.pop()
    {'user': 'Barney'}
    >>> context['user']
    'Fred'

Testing
-------

To run the tests you need to install testing requirements first::

    $ make install

Then to run tests, you can use ``nosetests`` or simply use Makefile command::

    $ nosetests -sv
    # or
    $ make test
