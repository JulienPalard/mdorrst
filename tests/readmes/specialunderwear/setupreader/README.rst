retrieve package specification from setup,py
============================================

setup.py contains a function named setup.

When writing software that works with python packages it is very
inconvenient to retrieve the package metadata from setup.py. This package
makes it easy, just point it at setup.py and get a dict::

    >>> import setupreader, json
    >>> foo = setupreader.load('setup.py')
    >>> print json.dumps(foo, indent=4)
    {
        "description": "retrieve package specification from setup,py", 
        "install_requires": [
            "setuptools", 
            "mock"
        ], 
        "zip_safe": false, 
        "keywords": "", 
        "packages": [], 
        "classifiers": [], 
        "entry_points": {
            "console_scripts": [
                "setupreader = setupreader:main"
            ]
        }, 
        "name": "setupreader", 
        "license": "", 
        "author": "Lars van de Kerkhof", 
        "url": "", 
        "include_package_data": true, 
        "py_modules": [
            "setupreader"
        ], 
        "long_description": "", 
        "author_email": "lars@permanentmarkers.nl", 
        "version": "0.0.1"
    }
