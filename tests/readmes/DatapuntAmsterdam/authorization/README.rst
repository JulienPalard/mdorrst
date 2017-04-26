Datapunt Authorization
======================

.. image:: https://img.shields.io/badge/python-3.4%2C%203.5%2C%203.6-blue.svg
    :target: https://www.python.org/

.. image:: https://img.shields.io/badge/license-MPLv2.0-blue.svg
    :target: https://www.mozilla.org/en-US/MPL/2.0/

---------------------

Interface to authorization logic in the backend of Amsterdam's (Netherlands)
open data distribution platform, [Datapunt](http://data.amsterdam.nl).

In Datapunt authorization levels associated with users are stored in a central
database. When a user accesses a resource she needs to provide a
cryptographically secure token. That token contains the user's authorization
level. The resource in turn uses that information to decide what information
the user can access.

Install
-------

::

	$ pip install datapunt-authorization

In order to use this library you need to have access to a Postgress database.

Usage
-----

::

	import authorization
	import authorization_levels  # pip install datapunt-authorization-levels
	
	authzmap = authorization.AuthzMap(**psycopgconf)

	if authzmap['myuser'] == authorization_levels.LEVEL_EMPLOYEE:
		...  # do some eployee-e things

Contribute
----------

Activate your virtualenv, install the egg in `editable` mode, and start coding:

::

	$ source env/bin/activate
	$ pip install -e .

Testing:

::

	make test

Documentation
-------------

The docs can be found at [datapunt-authorization.readthedocs.io](https://datapunt-authorization.readthedocs.io).
