we-get: command-line tool for searching torrents.
#################################################

.. image:: https://img.shields.io/pypi/v/we-get.svg
    :target: https://pypi.python.org/pypi/we-get

.. image:: https://img.shields.io/pypi/l/we-get.svg
    :target: https://pypi.python.org/pypi/we-get

.. image:: https://img.shields.io/pypi/pyversions/we-get.svg
    :target: https://pypi.python.org/pypi/we-get

.. class:: no-web

    .. image:: https://raw.githubusercontent.com/wiki/levisabah/we-get/screenshots/we_get.gif
        :alt: we-get gif
        :width: 100%
        :align: center

.. class:: head

.. contents::

.. section-numbering::

Installation
============

we-get can be installed directly by running:

.. code-block:: bash

    $ python setup.py install


alternatively you can use `pip` 

.. code-block:: bash

    $ pip install we-get


Dependencies
============

`Python <https://www.python.org/>`_ 3.5 or above

and the following Python packages:

* `colorama <https://github.com/tartley/colorama>`_
* `docopt <https://github.com/docopt/docopt>`_
* `prompt_toolkit <https://github.com/jonathanslenders/python-prompt-toolkit>`_
 
Platforms
==========

* Linux
* BSD
* Mac
* Windows

Basic Usage
===========

.. code-block:: bash

    $ we-get --search "Linux.iso" --target  the_pirate_bay,1337x --filter "2016"

advanced example:

.. code-block:: bash

    $ we-get -s "Linux.iso" -t all -f "2016,2012,2014" -n10

General options
---------------

============ =============
-h --help    Help message.
-v --version Show version.
============ =============

Options
-------

===================== =====================================================
-s --search=<text>    Search for a torrent.                                
-l --list             List top torrents from modules.                      
-t --target=<target>  Select module to use or 'all'.                       
-L --links            Output results as links.                             
-J --json             Output results in JSON format.                       
-G --get-list         List targets (supported web-sites).                  
-f --filter=<str>     Match text or regular expression in the torrent name.
-n --results=<n>      Number of results to retrieve.                       
-S --sort-type=<type> Sort torrents by name/seeds (default: seeds).        
===================== =====================================================

Video options
-------------

================ ==================================================================
-q --quality=<q> Try to match quality for the torrent (720p,1080p, ...).           
-g --genre=<g>   Try to select video genre for the torrent (action, comedy, etc..).
================ ==================================================================


See also ``we-get --help``.

Supported websites
------------------

* 1337x
* thepiratebay
* eztv
* yts

to list the supported websites run:

.. code-block:: bash

    $ we-get -G

Contributing
------------

Any collaboration is welcome!

Licence
-------

`MIT <https://github.com/levisabah/we-get/blob/master/LICENSE>`_
