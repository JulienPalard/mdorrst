Sorna Client
============

[![PyPI](https://badge.fury.io/py/sorna-client.svg)](https://pypi.python.org/pypi/sorna-client)
[![Python Versions](https://img.shields.io/pypi/pyversions/sorna-client.svg)](https://pypi.org/project/sorna-client/)
[![Travis Build Status](https://travis-ci.org/lablup/sorna-client.svg?branch=master)](https://travis-ci.org/lablup/sorna-client)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/5h6r1cmbx2965yn1/branch/master?svg=true)](https://ci.appveyor.com/project/achimnol/sorna-client/branch/master)
[![Code Coverage](https://codecov.io/gh/lablup/sorna-client/branch/master/graph/badge.svg)](https://codecov.io/gh/lablup/sorna-client)

The API client library for [Sorna](http://sorna.io)

Usage
-----

You should set the access key and secret key as environment variables to use the API.
Grab your keypair from [cloud.sorna.io](https://cloud.sorna.io) or your cluster admin.

```sh
export SORNA_ACCESS_KEY=...
export SORNA_SECRET_KEY=...

# optional (for local clusters)
export SORNA_ENDPOINT="https://my-precious-cluster/"
```

Synchronous API
---------------

```python
from sorna.kernel import Kernel

kern = Kernel.get_or_create('lua5', client_token='abc')
result = kern.execute('print("hello world")', mode='query')
print(result['console'])
kern.destroy()
```

You need to take care of `client_token` because it determines whether to
reuse kernel sessions or not.
Sorna cloud has a timeout so that it terminates long-idle kernel sessions,
but within the timeout, any kernel creation requests with the same `client_token`
let Sorna cloud to reuse the kernel.

Asynchronous API
----------------

```python
import asyncio
from sorna.asyncio.kernel import AsyncKernel

async def main():
    kern = await AsyncKernel.get_or_create('lua5', client_token='abc')
    result = await kern.execute('print("hello world")', mode='query')
    print(result['console'])
    await kern.destroy()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
```

All the methods of `AsyncKernel` objects are exactly same to the synchronous version,
except that they are coroutines.

Additionally, `AsyncKernel` offers async-only method `stream_pty()`.
It returns a `StreamPty` object which allows you to access a pseudo-tty of the kernel.
`StreamPty` works like an async-generator and provides methods to send stdin inputs
as well as resize the terminal.
