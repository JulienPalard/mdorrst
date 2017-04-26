python-simplestream
===================

A python library that provides an interface to the `SimpleStream API`_.

-  **Author**: `Hut 42`_
-  **Version**: 0.3
-  **License**: Apache 2.0

Dependencies
------------

-  `Requests`_ is used to make the HTTP request.

Installation
------------

python-simplestream can be installed in any number of the usual ways:

::

    pip install python-simplestream

::

    git clone git://github.com/hut42/python-simplestream.git
    cd python-simplestream
    python setup.py install

Usage
-----

Get available VODs by stream id:

::

    >>> import simplestream
    >>> api = simplestreamapi.Api(api_key='yourapikeyhere')
    >>> # get a range of vods - by default today until the end of time
    >>> vods = api.get_vod_range(900)
    >>> [<simplestream.models.Vod object at 0x7ffaa00ef080>, <simplestream.models.Vod object at 0x7ffaa00ef438>...]

Get a specific date range (use python datetime objects):

::

    >>> vods = api.get_vod_range(900, start=..., end=...)
    >>> [<simplestream.models.Vod object at 0x7ffaa00ef080>, <simplestream.models.Vod object at 0x7ffaa00ef438>...]

By default categories are not returned in VOD range call - use true flag
to enable. This does incur an extra API call per VOD object:

::

    >>> vods = api.get_vod_range(900, category=True)
    >>> [<simplestream.models.Vod object at 0x7ffaa00ef080>, <simplestream.models.Vod object at 0x7ffaa00ef438>...]

Get single VOD info by uvid:

::

    >>> vod = api.get_vod(90000)
    >>> <simplestream.models.Vod object at 0x7ffaa00ef080>]

Issues
------

-  SimpleStream API on VOD range does not add category by default
-  No time in VOD range call works except midnight for ``start``
   parameter

.. _SimpleStream API: http://www.simplestream.com/
.. _Hut 42: http://hut42.co.uk
.. _Requests: http://python-requests.org/
