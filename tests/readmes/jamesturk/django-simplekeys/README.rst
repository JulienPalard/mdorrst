django-simplekeys
=================

django-simplekeys is a reusable Django app that provides a simple way to add
API keys to an existing Django project, regardless of API framework.

    * GitHub: https://github.com/jamesturk/django-simplekeys
    * Documentation: https://django-simplekeys.readthedocs.io/en/latest/

.. image:: https://travis-ci.org/jamesturk/django-simplekeys.svg?branch=master
    :target: https://travis-ci.org/jamesturk/django-simplekeys

.. image:: https://img.shields.io/pypi/v/django-simplekeys.svg
    :target: https://pypi.python.org/pypi/django-simplekeys

.. image:: https://readthedocs.org/projects/django-simplekeys/badge/?version=latest
    :target: https://django-simplekeys.readthedocs.io/en/latest/


Features
--------

* `Token bucket <https://en.wikipedia.org/wiki/Token_bucket>`_ rate limiting, for limiting requests/second with optional bursting behavior.
* Quota-based rate limiting (e.g. requests/day)
* Ability to configure different usage tiers, to give different users different rates/quotas.
* Ability to configure different 'zones' so that different API methods can have different limits.  (e.g. some particularly computationally expensive queries can have a much lower limit than cheap GET queries)
* Provided views for very simple email-based API key registration.

