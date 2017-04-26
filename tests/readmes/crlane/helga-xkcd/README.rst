==========
helga-xkcd
==========

Description
===========

The helga-xkcd plugin provides a helga_ command for retrieving xkcd comics through that site's `JSON based api`_. Requires MongoDB >= 2.6 for full text search.

--------

Usage:
======
Get the latest xkcd
.. code-block:: none
    !xkcd

Get a random xkcd comic
.. code-block:: none
    !xkcd random

Get xkcd comic number <n>. For example, to fetch comic number 10:
.. code-block:: none
    !xckd number 10


Get a comic about a given text string. Using text indexing
.. code-block:: none
    !xkcd about pi


Features:
=========

Provides commands for fetching official xkcd comic images and displaying its hidden text

- [o] fetch the latest comic `!xkcd`
- [o] fetch a specific comic `!xkcd number [n]`
- [o] fetch a comic about a keyword: `!xkcd about [keyword]`
- [ ] automatically populate database when the plugin is loaded
- [ ] periodically refreshes index of comics it knows about

.. _helga: https://github.com/shaunduncan/helga
.. _`JSON based api`: https://xkcd.com/json.html


