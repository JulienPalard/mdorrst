# pyLoggingExtras
Extra logging functionality for Python

####NoneLogger

NoneLogger is a logger class that implements logging.Logger interface
 but provides no functionality (Null object design pattern), allowing you 
 to use that as a default logger and forgo the need to check if logger is 
 an actual instance before using it to log things.
 
**Example:**
*without NoneLogger*
```python
def method_that_logs_if_possible(arg1, arg2, logger=None)
    #TODO code here
    if logger: 
        logger.info("ran code up to here")
    #TODO more code here
    if logger: 
        logger.debug("values here are so and so")

```

*with NoneLogger*
```python
from loggingextras import NoneLogger

def method_that_logs_if_possible(arg1, arg2, logger=NoneLogger())
    #TODO code here
    logger.info("ran code up to here")
    #TODO more code here
    logger.debug("values here are so and so")

```

####API Logging

apilog is a set of logging decorators that will log entry and exit events
 in and out of methods.
 
apilog decorators will log entry events and input arguments to methods, as
 well as exit values and exceptions raised within methods
 
apilog decorators are availale for different logging levels

apilog decorators take advantage of a class's logger property if one
exists and follows logging.Logger interface. otherwise uses stdout prints

apilog decorators are available for the following logging levels:
```python
apilog_finest
apilog_finer
apilog_fine
apilog_debug
apilog_info
apilog_warning
apilog_error
apilog_critical
```

**Example usage module level methods:**
```python
from loggingextras.apilog import apilog_debug, apilog_info

@apilog_debug
def method_debug_output(param_a=None):
    print 'params:', param_a
    return param_a


if __name__ == "__main__":
    method_debug_output(dict(k1=1, k2=2))
```

*Sample output:*
```
DEBUG:apilog:entering method_debug_output with wargs=[{"k2": 2, "k1": 1}], kwargs={}
params: {'k2': 2, 'k1': 1}
DEBUG:apilog:exiting method_debug_output with {"k2": 2, "k1": 1} in [0:00:00.000107]
```

**Example usage using class methods with a class logger availble:**
```python
from loggingextras.apilog import apilog_debug

class decorated_class_with_logger(object):

    def __init__(self):
        basicConfig(level=1, stream=sys.stdout)
        self.logger = getLogger('decorated_class')

    @apilog_debug
    def method_a(self, param_a=None, param_b=None, param_c=None):
        self.logger.info('params:', param_a, param_b, param_c)
        assert param_b != "exception", 'failed something'


if __name__ == "__main__":
    obj = decorated_class_with_logger()
    obj.method_a(param_b='something')

```

*Sample output:*
```
DEBUG: decorated_class: entering method_a with wargs=[], kwargs={"param_b": "something"}
INFO : decorated_class: params: None something None
DEBUG: decorated_class: exiting method_a with null in [0:00:00.000090]

```