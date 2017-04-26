==============================================
searchcolor - Extract colors from web searches
==============================================

|version| |github| |python35| |license| |format|

.. |version| image:: https://img.shields.io/pypi/v/searchcolor.svg
    :target: https://pypi.python.org/pypi/searchcolor
.. |python35| image:: https://img.shields.io/badge/Python-3.5-brightgreen.svg
    :target: https://www.python.org/
.. |license| image:: https://img.shields.io/badge/License-MIT-blue.svg
    :target: https://github.com/Tathorack/searchcolor/blob/master/LICENSE.md
.. |github| image:: https://img.shields.io/github/tag/Tathorack/searchcolor.svg
   :target: https://github.com/Tathorack/searchcolor
.. |format| image:: https://img.shields.io/pypi/format/searchcolor.svg
    :target: https://pypi.python.org/pypi/searchcolor

---------------------------------------------------------------------------------------
This module uses imagecolor with PIL(Pillow) to extract colors from web image searches.
---------------------------------------------------------------------------------------

Available functions
===================
average_image_url(url, name)
============================
Averages a single image from a url into RGB color values. Returns a dictionary with the following keys: ``name``, ``red``, ``green``, ``blue``

* ``url`` - image url.
* ``name`` - name to return. Generally passed from the function that generates the url.
* ``timeout`` - ``requests`` timeout in seconds.
* ``max_size`` - maximum size of image to fetch in MB.


\_image_search_average(url_list, max_threads=20)
================================================
Averages all urls in a list into a singular RGB average.

* ``url_list`` - path to directory
* ``max_threads`` - max processes to spawn.
* ``timeout`` - ``requests`` timeout in seconds. This gets passed to ``average_image_url``
* ``max_size`` - maximum size of image to fetch in MB. This gets passed to ``average_image_url``

google_average(search_term, num_results, api_key, cse_id, max_threads=20)
=========================================================================
Does a Google image search and averages all the images into a singular RGB search average. Returns a dictionary with the following keys: ``name``, ``red``, ``green``, ``blue``

* ``search_term`` - Google image search term.
* ``num_results`` - Number of results to include.
* ``api_key`` - Google API key.
* ``cse_id`` - Google CSE ID.
* ``max_threads`` - max processes to spawn. This gets passed to ``\_image_search_average``
* ``timeout`` - ``requests`` timeout in seconds. This gets passed to ``average_image_url``
* ``max_size`` - maximum size of image to fetch in MB. This gets passed to ``average_image_url``

Future work
===========
* add more information to readme
* build offline tests
