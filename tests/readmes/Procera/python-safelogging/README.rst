safelogging: Extensions to the standard python logging framework
================================================================

A simple python library that adds some additional logging functionality on top
of the standard python logging library that could be useful for python
applications running as background services in a UNIX system.

One of the main functionalities it provides is a ``ResilientSysLogHandler``
class that is a drop-in replacement of ``logging.handlers.SysLogHandler`` and
is able to gracefully handle any connection issues to the syslog server while
falling back to file stream logging to avoid any loss of messages.
