Sprockets
=========
A loosely coupled framework built on top of Tornado. Take what you need to build
awesome applications.

The core `sprockets` packages offers only the command line application for
invoking Sprockets controllers such as the HTTP and AMQP controllers.

|Version| |Downloads| |Status| |Coverage| |License|

CLI Usage
---------

    usage: sprockets [-h] [-l] [-d] [-s] [-v] [--version]
                     {http,amqp} ... application
    
    positional arguments:
      {http,amqp}      Available sprockets application controllers
        http           HTTP Application Controller
        amqp           RabbitMQ Worker Controller
      application      The sprockets app to run
    
    optional arguments:
      -h, --help       show this help message and exit
      -l, --list       List installed sprockets apps
      -s, --syslog     Log to syslog
      -v, --verbose  Verbose logging output, use -vv for DEBUG level logging
      --version      show program's version number and exit



.. |Version| image:: https://badge.fury.io/py/sprockets.svg?
   :target: http://badge.fury.io/py/sprockets

.. |Status| image:: https://travis-ci.org/sprockets/sprockets.svg?branch=master
   :target: https://travis-ci.org/sprockets/sprockets

.. |Coverage| image:: https://coveralls.io/repos/sprockets/sprockets/badge.png
   :target: https://coveralls.io/r/sprockets/sprockets
  
.. |Downloads| image:: https://pypip.in/d/sprockets/badge.svg?
   :target: https://pypi.python.org/pypi/sprockets
   
.. |License| image:: https://pypip.in/license/sprockets/badge.svg?
   :target: https://sprockets.readthedocs.org
