.. image:: https://img.shields.io/pypi/v/labpack.svg
    :target: https://pypi.python.org/pypi/labpack
.. image:: https://img.shields.io/pypi/l/labpack.svg
    :target: https://pypi.python.org/pypi/labpack

=======
labPack
=======
*A Collection of Methods for Data Collection & Processing*

:Downloads: http://pypi.python.org/pypi/labPack
:Source: https://github.com/collectiveacuity/labPack

============
Installation
============
From PyPi::

    $ pip install labpack

From GitHub::

    $ git clone https://github.com/collectiveacuity/labPack
    $ cd labPack
    $ python setup.py install

Getting Started
---------------
This module is designed to make the process of retrieving, managing and processing data more uniform across a variety of different sources and structures. The classes and methods in this module aggregate and curate python resources and online APIs to provide a set of best practices for handling data across laboratory projects.

Create an unique ID for records::

    from labpack.records.id import labID

    id = labID()
    url_safe_id_string = id.id48
    id_datetime = id.epoch
    id_mac_address = id.mac

Save record data in local user data::

    from labpack.storage.appdata import appdataClient

    msg_key = '%s/%s.yaml' % (id_mac_address, id_datetime)
    msg_details = { 'dt': id_datetime, 'mac': id_mac_address, 'msg': 'Text me back' }
    msg_client = appdataClient('Outgoing', 'My Team', 'My App')
    mgs_client.create(msg_key, msg_details)

For more details about how to use labPack, refer to the
`Reference Documentation on GitHub
<https://github.com/collectiveacuity/labPack/blob/public/REFERENCE.rst>`_