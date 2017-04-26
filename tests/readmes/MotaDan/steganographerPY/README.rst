==============
steganographer
==============
.. image:: https://travis-ci.org/MotaDan/steganographerPY.svg?branch=master
   :target: https://travis-ci.org/MotaDan/steganographerPY
.. image:: https://coveralls.io/repos/github/MotaDan/steganographerPY/badge.svg?branch=master
   :target: https://coveralls.io/github/MotaDan/steganographerPY?branch=master
.. image:: https://landscape.io/github/MotaDan/steganographerPY/master/landscape.svg?style=flat
   :target: https://landscape.io/github/MotaDan/steganographerPY/master
   :alt: Code Health


Hide messages and files inside an image. 


Description
===========

Given an image and a message or a file steganographer will hide the message or file in the bits of the image. Works best when PNGs are passed in. Will convert JPGs to PNGs because of compression.

Compatiable with python 3 and up.

To install:
pip install steganographer

For development:
After cloning run
pip-sync dev-requirements.txt requirements.txt test-requirements.txt

https://pypi.python.org/pypi/steganographer
