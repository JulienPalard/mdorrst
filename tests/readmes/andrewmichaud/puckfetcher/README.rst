puckfetcher
===========

| |BSD3 License|
| |Build Status|
| |Coverage Status|
| |Issue Count|
.. image:: https://badge.fury.io/py/puckfetcher.svg
    :target: https://badge.fury.io/py/puckfetcher
.. image:: https://badge.waffle.io/andrewmichaud/puckfetcher.png?label=ready&title=Ready 
 :target: https://waffle.io/andrewmichaud/puckfetcher
 :alt: 'Stories in Ready'

A simple command-line podcatcher.

Supports Python 3.5+. Feel free to report any issues here, and I’ll investigate when/if I can.

| You’ll need setuptools (https://pypi.python.org/pypi/setuptools) to
  run this in its current state. Go get it, clone this repo, and you
| can run the below commands. Should work on OSX and Linux, from the
  command line. You’ll want a default config file, name it config.yaml
| and look at example\_config.yaml to see how it should be structured.

Directory for config file:

-  OSX: /Users/[USERNAME]/Application Support/puckfetcher/config.yaml
-  Linux: /home/[USERNAME]/.config/puckfetcher/config.yaml

Build + Install:

::

    python3 setup.py install

Test:

::

    python3setup.py test

Features
--------
-  Download any podcast with an RSS URL.
-  Download newest episodes on demand.
-  Download any episode from a podcast's backlog.
-  Respects podcast authors' websites - rate limits, checks when feed was last updated when trying
   to refresh.
-  Provides progress on downloads.
-  Provides summary of recently-downloaded podcasts per-session, as well as summary of
   recently-downloaded episodes per-podcast.


Future releases
---------------
-  Text-based progress for other time-consuming actions.
-  Add MP3 tag support to clean up tags based on feed information if
   it’s messy.
-  Support PyPy (when it supports 3.5+).
-  Allow parallel downloading.

.. |BSD3 License| image:: http://img.shields.io/badge/license-BSD3-brightgreen.svg
   :target: https://tldrlegal.com/license/bsd-3-clause-license-%28revised%29
.. |Build Status| image:: https://travis-ci.org/andrewmichaud/puckfetcher.svg?branch=master
   :target: https://travis-ci.org/andrewmichaud/puckfetcher
.. |Coverage Status| image:: https://coveralls.io/repos/andrewmichaud/puckfetcher/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/andrewmichaud/puckfetcher?branch=master
.. |Issue Count| image:: https://codeclimate.com/github/andrewmichaud/puckfetcher/badges/issue_count.svg
   :target: https://codeclimate.com/github/andrewmichaud/puckfetcher
