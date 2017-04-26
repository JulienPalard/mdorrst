Django Markdowny
****************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-markdowny.svg
.. _PyPI version: https://pypi.python.org/pypi/django-markdowny

.. |Build status| image::
   https://travis-ci.org/richardcornish/django-markdowny.svg?branch=master
.. _Build status: https://travis-ci.org/richardcornish/django-markdowny

**Django Markdowny** is a `Django <https://www.djangoproject.com/>`_ `template tag <https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/>`_ application to convert `Markdown <http://daringfireball.net/projects/markdown/>`_ to HTML.

Unlike other Django/Markdown filters, Markdowny supports all of the options available in `Python Markdown <https://pythonhosted.org/Markdown/reference.html>`_ via `settings <https://django-markdowny.readthedocs.io/en/latest/settings.html>`_.

* `Package distribution <https://pypi.python.org/pypi/django-markdowny>`_
* `Code repository <https://github.com/richardcornish/django-markdowny>`_
* `Documentation <https://django-markdowny.readthedocs.io/>`_
* `Tests <https://travis-ci.org/richardcornish/django-markdowny>`_

Install
=======

.. code-block:: bash

   $ pip install django-markdowny

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'markdowny',
   ]

Usage
=====

.. code-block:: django

   {% load markdowny_tags %}

   {% markdowny %}
   # Hello, world!
   {% endmarkdowny %}

Result:

.. code-block:: html

   <h1>Hello, world!</h1>
