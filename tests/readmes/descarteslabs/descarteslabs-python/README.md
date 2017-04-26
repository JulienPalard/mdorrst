[![Build Status](https://travis-ci.org/descarteslabs/descarteslabs-python.svg?branch=master)](https://travis-ci.org/descarteslabs/descarteslabs-python)

Descarteslabs
=============

Services
--------

This package includes service wrappers for Descartes Labs application services that 
do require additional dependencies (included in requirements.txt) and are thus not 
implicitly included in the root package (see above). Service wrappers include, 
primarily, Metadata (image metadata) and Places (named shapes and statistics). 
These services are authenticated and in order to setup authentication there is a 
convenience script to help you log in.

```bash
$ python setup.py install
$ pip install -r requirements.txt
$ descarteslabs login
```

For non-interactive environments, one needs to set the CLIENT_ID and CLIENT_SECRET 
environment variables. These can be retrieved from the ~/.descarteslabs/token_info.json
created from the login process or generated fresh through through [IAM](https://iam.descarteslabs.com).

```bash
$ export CLIENT_ID=...
$ export CLIENT_SECRET=...
```

The latest build of the documentation can be found on [readthedocs](http://descartes-labs-python.readthedocs.io/en/latest/)

FAQ
---

If you are on older versions of Python 2.7, you may encounter warnings about
SSL such as:

  InsecurePlatformWarning: A true SSLContext object is not
  available. This prevents urllib3 from configuring SSL appropriately and 
  may cause certain SSL connections to fail. For more information, see 
  https://urllib3.readthedocs.org/en/latest  
  /security.html#insecureplatformwarning.

Please follow the instructions from
[stackoverflow](http://stackoverflow.com/questions/29099404/ssl-insecureplatform-error-when-using-requests-package)
and install the `"requests[security]"` package with, e.g. `pip install
"requests[security]"`.

