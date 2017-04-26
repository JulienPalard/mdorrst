takumi_thrift
=============

.. image:: https://travis-ci.org/elemepi/takumi-thrift.svg?branch=master
    :target: https://travis-ci.org/elemepi/takumi-thrift


Thriftpy instruments for passing metadata bidirectional.


Example
-------

.. code:: python

    # Server
    class Ctx(object):
        pass
    ctx = Ctx()
    ctx.response_meta = {'server': 'test'}

    class Handler(object):
        def say_hello(name):
            assert ctx.meta == {'hello': 'test', 'client_name': 'test_client'}
            return Response('Hello ' + name, meta={'api': 'say_hello'})

    processor = Processor(ctx, service, Handler())

    # Client
    client = Client(service, proto, meta={'client_name': 'test_client'})
    res = client.call('say_hello', 'world', meta={'hello': 'test'})
    assert res.meta == {'api': 'say_hello', 'server': 'test'}
    assert res.value == 'Hello world'


Data frame change
-----------------

Request data frame::

    before: message_begin args message_end
    after:  meta_begin meta meta_end message_begin args message_end

Response data frame::

    before: message_begin result message_end
    after:  meta_begin meta meta_end message_begin result message_end
