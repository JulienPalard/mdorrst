Python Client for QuadrigaCX
----------------------------

.. image:: https://travis-ci.org/joowani/quadriga.svg?branch=master
    :target: https://travis-ci.org/joowani/quadriga

.. image:: https://badge.fury.io/py/quadriga.svg
    :target: https://badge.fury.io/py/quadriga
    :alt: Package version

.. image:: https://img.shields.io/badge/python-2.7%2C%203.4%2C%203.5%2C%203.6-blue.svg
    :target: https://github.com/joowani/quadriga
    :alt: Python Versions

.. image:: https://coveralls.io/repos/github/joowani/quadriga/badge.svg?branch=master
    :target: https://coveralls.io/github/joowani/quadriga?branch=master
    :alt: Test Coverage

.. image:: https://img.shields.io/github/issues/joowani/quadriga.svg
    :target: https://github.com/joowani/quadriga/issues
    :alt: Issues Open

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/joowani/quadriga/master/LICENSE
    :alt: MIT License

|

Introduction
============

**Quadriga** is a Python client for QuadrigaCX_, a cryptocurrency exchange
platform based in Vancouver, BC, Canada. It wraps the latest version of the
`REST API`_ provided by the exchange and facilitates the process of trading
bitcoin and ether.

.. _QuadrigaCX: https://www.quadrigacx.com
.. _REST API: https://www.quadrigacx.com/api_info


Requirements
============

- Python 2.7.x, 3.4.x, 3.5.x or 3.6.x
- QuadrigaCX API secret, API key and client ID


Installation
============

To install a stable version from PyPi_:

.. code-block:: bash

    ~$ pip install quadriga


To install the latest version directly from GitHub_:

.. code-block:: bash

    ~$ pip install -e git+git@github.com:joowani/quadriga.git@master#egg=quadriga

Note: ``sudo`` may be required depending on the environment.

.. _PyPi: https://pypi.python.org/pypi/quadriga
.. _GitHub: https://github.com/joowani/quadriga


Getting Started
===============

Here are some usage examples:

.. code-block:: python

    from quadriga import QuadrigaClient

    # Initialize the QuadrigaCX client
    client = QuadrigaClient(
        api_key='api_key',
        api_secret='api_secret',
        client_id='client_id',
        default_book='btc_usd'
    )

    # Get the latest trading summary
    client.get_summary()

    # Get all public open orders
    client.get_public_orders()

    # Get recently completed public trades
    client.get_public_trades()

    # Get the user's open orders
    client.get_orders()

    # Get the user's completed trades
    client.get_trades()

    # Get the user's account balance
    client.get_balance()

    # Buy 10 bitcoins at the market price
    client.buy_market_order(10)

    # Buy 10 bitcoins at limit price of $1000 USD
    client.buy_limit_order(10, 1000)

    # Sell 20 bitcoins at the market price
    client.sell_market_order(20)

    # Sell 20 bitcoins at limit price of $1300 USD
    client.sell_limit_order(20, 1300)

    # Look up an order by its ID
    client.lookup_order('order_id')

    # Cancel an open order by its ID
    client.cancel_order('order_id')

    # Return the deposit address used for funding bitcoin
    client.get_deposit_address('bitcoin')

    # Return the deposit address used for funding ether
    client.get_deposit_address('ether')

    # Withdraw 15 bitcoins from QuadrigaCX to the given address
    client.withdraw('bitcoin', 15, 'withdrawal_address')

    # Withdraw 20 ethers from QuadrigaCX to the given address
    client.withdraw('ether', 20, 'withdrawal_address')

Check out the full `API documentation`_ for more details!

.. _API documentation:
    http://quadriga.readthedocs.io/en/latest/index.html
