[![PyPI version](https://badge.fury.io/py/ios-build-versions.svg)](https://badge.fury.io/py/ios-build-versions)[![Build Status](https://travis-ci.org/SecretObsession/ios-build-versions-python.svg?branch=master)](https://travis-ci.org/SecretObsession/ios-build-versions-python)[![Code Climate](https://codeclimate.com/github/SecretObsession/ios-build-versions-python/badges/gpa.svg)](https://codeclimate.com/github/SecretObsession/ios-build-versions-python)[![Test Coverage](https://codeclimate.com/github/SecretObsession/ios-build-versions-python/badges/coverage.svg)](https://codeclimate.com/github/SecretObsession/ios-build-versions-python/coverage)[![Issue Count](https://codeclimate.com/github/SecretObsession/ios-build-versions-python/badges/issue_count.svg)](https://codeclimate.com/github/SecretObsession/ios-build-versions-python)

# iosbuildversions
A library which can used to look up more information, using the iOS build number.

Build numbers last updated: 2017/04/17

```
>>> import iosbuildversions
>>> print iosbuildversions.lookup_by_build("5A240d")
{'beta': True, 'build': '5A240d', 'name': 'iPhone OS 2.0 Beta 3', 'final': False}

>>> print iosbuildversions.lookup_by_build("foobar")
False
```