`Jaeum Modifier`_
=================

.. image:: https://readthedocs.org/projects/jaeum-modifier/badge/?version=latest
    :target: http://jaeum-modifier.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

`jaeum_modifier` module modifies a single Jaeum of a Hangul syllable among the given Hangul word or sentence.

.. code-block:: python

    from jaeum_modifier import modify
    message = u'안녕하세요'
    print(modify(message, index=1, jaeum=u'ㅉ')) # 안쪙하세요

``jaeum_modifier.modify`` replaces Jaeum of the indexed syllable to the given Jaeum(``JJ(u'ㅉ')``).


Installation
------------
Jaeum Modifier can be installed via ``pip``:

.. code-block:: console

    $ pip install jaeum-modifier

You can also install from `Github repository`__:

.. code-block:: console

    $ git clone git@github.com:hyunchel/jaeum_modifier.git
    $ cd jaeum_modifier/
    $ python setup.py install
      
.. _Jaeum Modifier: https://github.com/hyunchel/jaeum_modifier
__ https://github.com/hyunchel/jaeum_modifier
     

Documentation
-------------
Lastest Version
    https://jaeum-modifier.readthedocs.io
