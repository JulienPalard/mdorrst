========
tinyflow
========

Experiments in data flow programming.

.. image:: https://travis-ci.org/geowurster/tinyflow.svg?branch=master
    :target: https://travis-ci.org/geowurster/tinyflow?branch=master

.. image:: https://coveralls.io/repos/geowurster/tinyflow/badge.svg?branch=master
    :target: https://coveralls.io/r/geowurster/tinyflow?branch=master

After some experimentation, Apache Beam's Python SDK got the API right.
Use that instead.


Standard Word Count Example
===========================

Grab the 5 most common words in ``LICENSE.txt``

.. code-block:: python

    from collections import Counter

    from tinyflow.serial import ops, Pipeline


    pipe = Pipeline() \
        | "Split line into words" >> ops.flatmap(lambda x: x.lower().split()) \
        | "Remove empty lines" >> ops.filter(bool) \
        | "Produce the 5 most common words" >> ops.counter(5) \
        | "Sort by frequency desc" >> ops.sort(key=lambda x: x[1], reverse=True)

    with open('LICENSE.txt') as f:
        results = dict(pipe(f))


Using only Python's builtins:

.. code-block:: python

    from collections import Counter
    import itertools as it

    with open('LICENSE.txt') as f:
        lines = (line.lower().split() for line in f)
        words = it.chain.from_iterable(lines)
        count = Counter(words)
        results = dict(count.most_common(10))


Developing
==========

.. code-block:: console

    $ git clone https://github.com/geowurster/tinyflow.git
    $ cd tinyflow
    $ pip install -e .\[all\]
    $ pytest --cov tinyflow --cov-report term-missing


License
=======

See ``LICENSE.txt``


Changelog
=========

See ``CHANGES.md``
