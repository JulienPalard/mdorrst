Takumi: Thrift service framework
================================

.. image:: https://travis-ci.org/elemepi/takumi.svg?branch=master
    :target: https://travis-ci.org/elemepi/takumi



This package defines the interfaces for writing Takumi thrift services.

Install
-------

.. code:: bash

    pip install takumi


Example
-------

To define a simple app:

.. code:: python

    # app.py
    from takumi import Takumi

    app = Takumi('TestService')

    @app.api
    def say_hello(name):
        return 'Hello ' + name


To Run the app, install `takumi-cli <https://github.com/elemepi/takumi-cli>`_ first, then
create the following config:

.. code:: thrift

    # ping.thrift
    service TestService {
        string say_hello(1: required string name)
    }

.. code:: yaml

    # app.yaml
    app_name: test_app
    app: app:app
    thrift_file: ping.thrift

Run the following command:

.. code:: bash

    $ takumi serve
