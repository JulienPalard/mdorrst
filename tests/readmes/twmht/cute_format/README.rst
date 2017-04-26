cute_format
=========

pack random data and fast retrieval in python


Quick Install
-------------

Quick install for debian/ubuntu like linux distributions.

.. code-block:: bash

    $ pip install cute_format


Quick Usage Guide
-----------------

.. code-block:: python

    from cute.cute_reader import CuteReader
    from cute.cute_writer import CuteWriter
    cw = CuteWriter('tmp')
    a = 1000
    b = 2000
    cute_writer.write(bytes(a))
    cute_writer.write(bytes(b))
    cute_writer.close()
    cr = CuteReader('tmp')
    # get the object by index
    assert cr.num_data == 2
    byte_object = cr.get(1)
    assert int(byte_object) == a
    byte_object = cr.get(2)
    assert int(byte_object) == b
