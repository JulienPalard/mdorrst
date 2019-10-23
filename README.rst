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

The package exposes a single function, ``sniff(content)``, trying to
deduce the format used, returning it as a string: ``md``, ``rst`` or
``txt``::

  >>> import mdorrst
  >>> mdorrst.sniff("[hey](http://example.com)")
  'md'
  >>> mdorrst.sniff("`hey <http://example.com>`__")
  'rst'
