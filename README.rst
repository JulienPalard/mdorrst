=======
mdorrst
=======


.. image:: https://img.shields.io/pypi/v/mdorrst.svg
        :target: https://pypi.python.org/pypi/mdorrst

.. image:: https://img.shields.io/travis/JulienPalard/mdorrst.svg
        :target: https://travis-ci.org/JulienPalard/mdorrst

Tell appart Markdown and reStructuredText.


* Free software: MIT license

Usage
-----

The package exposes two functions, ``from_text`` and ``from_file``,
which both return one of ``md``, ``rst`` or ``txt`` according to the
*content* given.

``mdorrst.from_file(path)`` only reads the content of the file
 (without being influenced by the filename)::

  >>> import mdorrst
  >>> mdorrst.from_file("./README.rst")
  'rst'

``mdorrst.from_text`` works the same way, given a string::

  >>> import mdorrst
  >>> mdorrst.from_text("[hey](http://example.com)")
  'md'
  >>> mdorrst.from_text("`hey <http://example.com>`__")
  'rst'


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
