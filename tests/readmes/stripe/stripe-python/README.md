# Stripe Python Library [![Build Status](https://travis-ci.org/stripe/stripe-python.svg?branch=master)](https://travis-ci.org/stripe/stripe-python)

The Stripe Python library provides convenient access to the Stripe API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the Stripe
API.

## Documentation

See the [Python API docs](https://stripe.com/docs/api/python#intro).

## Installation

You don't need this source code unless you want to modify the gem. If you just
want to use the package, just run:

    pip install --upgrade stripe

or

    easy_install --upgrade stripe

Install from source with:

    python setup.py install

### Requirements

* Python 2.6+ or Python 3.3+ (PyPy supported)

## Usage

The library needs to be configured with your account's secret key which is
available in your [Stripe Dashboard][api-keys]. Set `stripe.api_key` to its
value:

``` python
import stripe
stripe.api_key = "sk_test_..."

# list charges
stripe.Charge.list()

# retrieve single charge
stripe.Charge.retrieve("ch_1A2PUG2eZvKYlo2C4Rej1B9d")
```

### Per-request Configuration

For apps that need to use multiple keys during the lifetime of a process, like
one that uses [Stripe Connect][connect], it's also possible to set a
per-request key and/or account:

``` python
import stripe

# list charges
stripe.Charge.list(
    api_key="sk_test_...",
    stripe_account="acct_..."
)

# retrieve single charge
stripe.Charge.retrieve(
    "ch_1A2PUG2eZvKYlo2C4Rej1B9d",
    api_key="sk_test_...",
    stripe_account="acct_..."
)
```

### Configuring a Client

The library can be configured to use `urlfetch`, `requests`, `pycurl`, or
`urllib2` with `stripe.default_http_client`:

``` python
client = stripe.http_client.UrlFetchClient()
client = stripe.http_client.RequestsClient()
client = stripe.http_client.PycurlClient()
client = stripe.http_client.Urllib2Client()
stripe.default_http_client = client
```

Without a configured client, by default the library will attempt to load
libraries in the order above (i.e. `urlfetch` is preferred with `urllib2` used
as a last resort). We usually recommend that people use `requests`.

### Configuring a Proxy

A proxy can be configured with `stripe.proxy`:

``` python
stripe.proxy = "https://user:pass@example.com:1234"
```

### Logging

The library can be configured to emit logging that will give you better insight
into what it's doing. The `info` logging level is usually most appropriate for
production use, but `debug` is also available for more verbosity.

There are a few options for enabling it:

1. Set the environment variable `STRIPE_LOG` to the value `debug` or `info`
   ```
   $ export STRIPE_LOG=debug
   ```

2. Set `stripe.log`:
   ```py
   import stripe
   stripe.log = 'debug'
   ```

3. Enable it through Python's logging module:
   ```py
   import logging
   logging.basicConfig()
   logging.getLogger('stripe').setLevel(logging.DEBUG)
   ```

## Development

Run all tests (modify `-e` according to your Python target):

    tox -e py27

Run a single test suite:

    tox -e py27 -- --test-suite stripe.test.resources.test_updateable.UpdateableAPIResourceTests

Run a single test:

    tox -e py27 -- --test-suite stripe.test.resources.test_updateable.UpdateableAPIResourceTests.test_save

Run the linter with:

    pip install flake8
    flake8 stripe

[api-keys]: https://dashboard.stripe.com/account/apikeys
[connect]: https://stripe.com/connect

<!--
# vim: set tw=79:
-->
