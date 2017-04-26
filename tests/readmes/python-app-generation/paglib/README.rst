paglib
======

General utility modules.

paglib.log
==========

No-frills logging library for Python 3.

This logging library is based on the following concepts (partially inspired by the `twelve-factor app`_):

- All output is written unbuffered to stdout. (There are no handlers.)
- The application controls the output in a print()-style syntax. (There are no formatters.)
- Output lines are tagged and the actual output can be filtered by tags. (There are no log levels.)
- All configuration is taken from environment variables. (There are no configuration files.)
- All logging to the standard logging library is redirected to this library. (We are greedy.)

Tagging mechanism
-----------------
- Every log output is tagged with a set of implicitly assigned or explicitly specified tags.
- Explicit tags are specified in a list as first parameter of log methods e.g. log.info(['tag'], ...)
- Implicit tags are:
    - The name of the module that contains the log statement.
    - The name used as log method e.g. log.warning(). Note: There are no pre-defined log methods. Any valid method name if possible e.g. log.whatever() or log.this_too().
    - In case of redirected logging:
        - The standard log level name in lowercase.
        - The name of the logger e.g. 'root' for the root logger.

Filtering
---------
The actual log output is filtered by a list of included or excluded tags.
If an include list is specified, only those log lines are printed of which at least one tag is part of the include list.
If an exclude list is specified, only those log lines are printed of which no tag is part of the exclude list.
If no list is specified, all log lines are printed. If both lists are specified, the exclude list has priority.

To omit all log output, specify an include list with an unused tag e.g. LOG_INCLUDE=_nothing

Usage
-----

.. code-block:: bash

    $ LOG_INCLUDE = debug;some_tag

.. code-block:: python

    from paglib import log

    log.debug('How many fingers:', 10)
    log.something(['some_tag'], 'Output something with additional tag.')

Configuration / environment variables
-------------------------------------
LOG_FTIME = "%x %X.%f" (default) | <strftime-style format for the time>

LOG_OUTPUT = native (default) | json
The JSON-formatted output line is a dict with the following fields:
- time: a float value of the timestamp (see datetime.timestamp())
- tags: a list of the log tags
- args: a list of the positional arguments
- kwargs: a dict of the keyword arguments

LOG_INCLUDE = <;-separated list of tags to be included in output>

LOG_EXCLUDE = <;-separated list of tags to be excluded from output>

LOG_LOGGING_LEVEL = DEBUG (default) | <level name from standard logging>

LOG_THREADED = false (default) | true
When threaded log is enabled, log output is done as a daemon thread.

.. _twelve-factor app: https://12factor.net

