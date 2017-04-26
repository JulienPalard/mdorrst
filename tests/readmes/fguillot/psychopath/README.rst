Psychopath
==========

.. image:: https://travis-ci.org/fguillot/psychopath.svg?branch=master
    :target: https://travis-ci.org/fguillot/psychopath

.. image:: https://badge.fury.io/py/psychopath.svg
    :target: https://badge.fury.io/py/psychopath

.. image:: https://readthedocs.org/projects/psychopath/badge/?version=latest
    :target: http://psychopath.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Psychopath is a thin wrapper around :code:`psycopg2` to provide helpers for Postgresql.

Features
--------

- Parse automatically the environment variable :code:`DATABASE_URL`
- Helpers to simplify SQL statement writing
- Basic schema migration tool

Requirements
------------

- Python >= 3.4
- psycopg2 >= 2.7
- Postgresql 9.x

Installation
------------

.. code:: bash

    pip install psychopath

Running tests
-------------

.. code:: bash

    pip install tox
    tox

Usage
-----

Initialize a new connection pool:

.. code:: python

    from psychopath import db

    db.init('postgres://postgres:postgres@localhost/psychopath_tests', maximum_connections=10)

You could also use an environment variable :code:`DATABASE_URL` to configure automatically the connection.

.. code:: python

    db.init()


Execute a SQL statement:

.. code:: python

    from psychopath import db

    db.run('CREATE TABLE foobar (id serial PRIMARY KEY, value text)')

Get table records as :code:`namedtuple`:

.. code:: python

    from psychopath import db

    records = db.find_all('SELECT * FROM foobar ORDER BY id DESC')

    for record in records:
        print(record.id)
        print(record.value)

Get only one record:

.. code:: python

    from psychopath import db

    record = db.find_one('SELECT * FROM foobar')
    print(record.value)

Get first column value:

.. code:: python

    from psychopath import db

    print(db.first('SELECT value FROM foobar'))

Get numeric value:

.. code:: python

    from psychopath import db

    print(db.count('SELECT count(*) FROM foobar'))

Insert a new record:

.. code:: python

    from psychopath import db

    db.run('INSERT INTO integration_test (value) VALUES (%s)', ['something'])

:code:`db.run()` is a wrapper around psycopg2 cursors.

Transactions:

.. code:: python

    from psychopath import db

    with db.transaction() as t:
        t.execute('CREATE TABLE test_create_table (value text)')
        t.execute('DROP TABLE test_create_table')

Author
------

Frédéric Guillot

License
-------

Psychopath is distributed under Apache 2.0 LICENSE.
