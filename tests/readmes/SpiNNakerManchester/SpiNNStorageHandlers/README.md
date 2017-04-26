This package provides classes to handle data storage, both in memory (through
a bytearray buffer) and in a file. The file may be permanent or temporary.

Requirements
============
In addition to a standard Python installation, this package depends on:

 - six

These requirements can be install using `pip`:

    pip install six

User Installation
=================
If you want to install for all users, run:

    sudo pip install SpiNNStorageHandlers

If you want to install only for yourself, run:

    pip install SpiNNStorageHandlers --user

To install in a virtualenv, with the virtualenv enabled, run:

    pip install SpiNNStorageHandlers

Developer Installation
======================
If you want to be able to edit the source code, but still have it referenced
from other Python modules, you can set the install to be a developer install.
In this case, download the source code, and extract it locally, or else clone
the [git repository](https://github.com/SpiNNakerManchester/SpiNNStorageHandlers.git)

To install as a development version which all users will then be able to use,
run the following where the code has been extracted:

    sudo python setup.py develop

To install as a development version for only yourself, run:

    python setup.py develop --user

To install as a development version in a `virtualenv`, with the `virutalenv`
enabled, run:

    python setup.py develop

Documentation
=============
[SpiNNStorageHandlers python documentation](http://spinnstoragehandlers.readthedocs.io)

[Combined python documentation](http://spinnakermanchester.readthedocs.io)