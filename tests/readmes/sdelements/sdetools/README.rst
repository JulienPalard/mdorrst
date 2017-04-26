.. image:: https://codeclimate.com/github/sdelements/sdetools/badges/gpa.svg
   :target: https://codeclimate.com/github/sdelements/sdetools

.. image:: https://travis-ci.org/sdelements/sdetools.svg?branch=master
    :target: https://travis-ci.org/sdelements/sdetools

.. image:: https://ci.appveyor.com/api/projects/status/wwjae8ser722tte0/branch/master?svg=true&passingText=master%20-%20OK&failingText=master%20-%20failing
    :target: https://ci.appveyor.com/project/sdelements/sdetools/branch/master

Requirements
============

- Python 2.6 or 2.7

This project is intended to be ultra lightweight, and portable.
The only requirement is to have Python 2.6 or 2.7 installed.

The console usage
-----------------

**sde.py**

The command line tool to run SD Elements integration modules. Use ``python
sde.py help`` to see usage and ``python sde.py help <cmd>`` to see usage for
specific module.

For example, to run command ``sync_tfs`` - which syncs a TFS server with an SDE server:

``python sde.py sync_tfs -c tfs.conf`` 

where ``tfs.conf`` is a file containing the settings associated with both services.

Additional command-line options:

 - Enable verbose output ``-v``
 - Enable debugging ``-d``
 - Specify which module to debug ``--debugmods=MODULENAME``

For example, to enable verbose output and debug information for ``sdetools.sdelib.restclient``,

``python sde.py sync_tfs -v --debugmods=sdetools.sdelib.restclient -d -c tfs.txt``
 

The package usage
-----------------

.. code-block:: python

	import sdetools

	sdetools.call('api_proxy', {'api_func': 'get_applications'})


SDE Library (sdelib/)
---------------------

A light weight library that provides an interface to SD Elements RESTful API.

- **apiclient**: The base API provider for calls to SD Elements.
- **interactive_plugin**: This module provides the interactive experience 
  needed for the SDE Lint tool and other similar usecases. This includes:
    - Password collection and retry
    - Application selection
    - Project selection
	
- **conf_mgr**: Configuration Manager provides support for parsing command
  line arguments, reading variables from config file, and allows for extended
  options to be defined for each usecase.

Testing
-------

Tests can be invoked using ``nosetests``:
``nosetests <flags> <testsFile>`` 

Simply running ``nosetests`` will run all tests in the current directory and its subdirectories. The flag ``-e live`` is useful for excluding the live tests.

Live tests should be run individually:
``nosetests --tests=$TESTS_FILE_PATH --tc=sdetools.config_path:$CONFIG_TESTS``
where $CONFIG_TESTS is the path to the file containing the appropriate configuration settings for running the life tests

**Writing new tests**

Modules typically have two types of tests, mock and live. Both inherit from 
``alm_integration.tests.alm_plugin_test_base.AlmPluginTestBase``
and  
``alm_integration.tests.alm_plugin_live_test_base.AlmPluginLiveTestBase``
respectively.

New test classes should be stored in a test folder of the module which they test and should extend these two classes. New tests may not neccesarily need to be extended further than simply initializing the base classes with the corresponding module connectors, generators and settings.

Response Generators are used in generating the api call return values when running mock tests. As such, each module test suite requires a new response generator that extends the base class 
``sdetools.sdelib.testlib.response_generator.ResponseGenerator``
The response generator class must declare rest_api_targets (if dealing with a REST API). Mocking an API endpoint consists of adding a regex matching the url, and mapping it to a new function to handle the response. Each function must return objects, consisting of the headers and the response returned by the API call.

JSON templates can also be created and loaded by the response generator to create mock responses. These are typically stored in the response directory of the test directory.
