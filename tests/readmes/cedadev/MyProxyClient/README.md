MyProxy Client Package
======================
This a pure* Python implementation of a client to the MyProxy Credential
Management Server (http://grid.ncsa.uiuc.edu/myproxy/).  It provides both a
Python API and a command line interface.

* i.e. MyProxy C client libraries are not required for this package.

It uses pyOpenSSL to make an SSL connection to the server following the
messaging interface as outlined in: http://grid.ncsa.uiuc.edu/myproxy/protocol/

The code is based on an original program myproxy_logon by Tom Uram of ANL.

Examples
========
These show how to retrieve a certificate bootstrapping trust in remote service:

API
---

```
>>> from myproxy.client import MyProxyClient
>>> myproxy_clnt = MyProxyClient(hostname="myproxy.somewhere.ac.uk")
>>> cert, private_key = myproxy_clnt.logon(username, password, bootstrap=True)
```

Command line interface
----------------------
```
$ myproxyclient logon -s myproxy.somewhere.ac.uk -l <username> -o creds.pem -b
```

Releases
========
2.0.1
-----
 * Updated hashing algorithm to sha256 after reported errors interacting with
   some servers

2.0.0
-----
 * Ported to Python 3.  This version is dual compatible with Python 2 and 3.
 * Minor fix to script to improve error reporting
 * Added Vagrantfile to enable provisioning of test myproxy-server for use with
   the tests.

Tested on CentOS 6.8 and OSX El Capitan

1.4.4
-----
 * Minor changes for ready for inclusion in conda-forge.  Thanks to Alex Goodman.

1.4.3
-----
 * Fix for SSL to use TLS instead of SSLv3 to address POODLE vulnerability
 * Fix for SSL verification for PyOpenSSL version 0.14 - v1.3.1 was broken
   because it passed the call back method to OpenSSL using verification classes'
   `__call__` method.

Tested on CentOS 6.4

1.3.1
-----
 * Fix to `MyProxyClient.writeProxyFile` and
   `MyProxyClient.readProxyFile` to correctly pick-up overridden file
   setting.  Thanks to Nicolas Carenton, IPSL.

Tests
=====
Unit test module with test files is in test/.  See the README in that directory.

Documentation
=============
Sphinx generated documentation is available in documentation/.  run the
Makefile to regenerate if required.

Thanks
======
 * to OMII-UK (Now Software Sustainability Institute) for funding development of NDG Security (2007-2008)
 * Tom Uram who wrote the `myproxy_logon` program on which this package is based.
