python-alkivi-logger
==========================

[![Build Status](https://travis-ci.org/alkivi-sas/python-alkivi-logger.svg?branch=master)](https://travis-ci.org/alkivi-sas/python-alkivi-logger)
[![Requirements Status](https://requires.io/github/alkivi-sas/python-alkivi-logger/requirements.svg?branch=master)](https://requires.io/github/alkivi-sas/python-alkivi-logger/requirements/?branch=master)

Python logger used at Alkivi

## Package

Example

```python
import logging

from alkivi.logger import Logger

#
# Define Logger
#
logger = Logger(min_log_level_to_mail=None,
                min_log_level_to_save=logging.DEBUG,
                min_log_level_to_print=logging.DEBUG,
                min_log_level_to_syslog=None,
                emails=['youremail@example.org'],
                use_root_logger=False) # If set to True will use root_logger

#
# All log level, from bottom to top
#
logger.debug('This is a debug comment')
logger.info('This is an info comment')
logger.warning('This is a warning comment')
logger.error('This is an error comment')
logger.critical('This is a critical comment')

try:
    1/0
except Exception as e:
    logger.exception('This is an exception comment')
    pass

#
# You can adjust log level on the fly
#
logger.set_min_level_to_mail(logging.WARNING)
logger.set_min_level_to_save(logging.WARNING)

#
# You can use loops
#
logger.new_loop_logger()
for i in range(0, 11):
    logger.new_iteration(prefix='i=%i' % (i))
    logger.debug("We are now prefixing all logger")
    if i == 9:
        logger.debug("Lets do another loop")
        logger.new_loop_logger()
        for j in range(0, 5):
            logger.new_iteration(prefix='j=%i' % (j))
            logger.debug("Alkivi pow@")

        # Dont forget to close logger or shit will happen
        logger.del_loop_logger()
    # Bonus point : if emailing is set, only send email for the loop we have
    # error
    if i == 10:
        logger.critical("We shall receive only mail for last loop")

logger.del_loop_logger()
logger.debug('We now remove an loop, thus a prefix')
```

## Parameters


## Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled
with the pytest-cov plugin.

Run your tests with ```py.test``` in the root directory.

Coverage is ran by default and is set in the ```pytest.ini``` file.
To see an html output of coverage open ```htmlcov/index.html``` after running the tests.

TODO

## Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.2, should you choose to use it.

TODO
