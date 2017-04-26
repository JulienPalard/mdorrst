===============================
markovipy
===============================


.. image:: https://img.shields.io/pypi/v/markovipy.svg
        :target: https://pypi.python.org/pypi/markovipy

.. image:: https://img.shields.io/travis/prodicus/markovipy.svg
        :target: https://travis-ci.org/prodicus/markovipy

.. image:: https://readthedocs.org/projects/markovipy/badge/?version=latest
        :target: https://markovipy.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/prodicus/markovipy/shield.svg
     :target: https://pyup.io/repos/github/prodicus/markovipy/
     :alt: Updates


Sentence generation using Markov Chains

============
Installation
============

To install markovipy, run this command in your terminal:

.. code-block:: console

    $ pip install markovipy

This is the preferred method to install markovipy, as it will always install the most recent stable release. 

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


=====
Usage
=====

To use markovipy in a project::

    >>> from markovipy.markovipy import MarkoviPy
    >>> # create MarkoviPy object
    >>> obj = MarkoviPy("/Users/tasrahma/development/projects/markovipy/corpus/ts_eliot/Gerontion_utf8.txt", 3)
    >>> # arguments passes is the initial corpus file and the markov chain length(defaults to 2 if nothing passed)
    >>> obj.generate_sentence()
    'Cammel, whirled Beyond the circuit of the shuddering Bear In fractured atoms.'
    >>> obj.generate_sentence()
    'After such knowledge, what forgiveness? Think now History has many cunning passages, contrived corridors And issues, deceives with whispering ambitions, Guides us by vanities.'
    >>> obj.generate_sentence()
    'Gull against the wind, in the windy straits Of Belle Isle, or running on the Horn, White feathers in the snow, the Gulf claims, And an old man, a dull head among windy spaces.'
    >>> obj.generate_sentence()
    'Silvero With caressing hands, at Limoges Who walked all night in the field overhead; Rocks, moss, stonecrop, iron, merds.'
    >>> obj.generate_sentence()
    "Gives too soon Into weak hands, what's thought can be dispensed with Till the refusal propagates a fear."


* Free software: GNU General Public License v3
* Documentation: https://markovipy.readthedocs.io.


Features
--------

* More tests to be added. As of now, some minimal tests have been written. Contributions more than welcome.
* Create a web-interface with some fancy buttons/UI which would give you random quotes.


