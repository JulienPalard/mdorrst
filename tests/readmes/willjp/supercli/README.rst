supercli
========

``supercli`` is a tiny Toolkit to quickly create readable, user-friendly 
CLI interfaces *(+autocomplete)*. 

(built on top of builtin argparse/logging modules)

|
|

This project has been built around tasks that I find myself repeating
every time that I create a CLI interface. Aside from autocompletion-script 
generation, this project is less about providing features that are unavailable elsewhere
than gluing together several existing options to quickly get you up and running.


**__warning__** : this is still very much in alpha, and some arguments **will** change.



|
|

.. image:: images/coloured_argparse.png
   :align: center



.. image:: images/coloured_logging.png
   :align: center



______________________________________________________________________________

|
|

.. contents:: Table Of Contents

|
|

______________________________________________________________________________



Features
--------

argparse tweaks
................
* Automatically generate ZSH autocompletion scripts (supports subarsers)
* ReStructuredText syntax-highlighting within helplines
* newlines, and ANSI colours can be used in helplines (on windows too)
* enables logging (streamhandler) by default (reused if already exists)
* builtin arguments (``--help(-h), --verbose(-v), --very-verbose(-vv), --fullhelp``)
* builtin hidden arguments (``--pdb,--devlog,--gen-autocomp,--default-parser``)
* extended set of logging-options can be enabled if needed (``--logfile,--log-longfmt,--silent``)
* 1x metavar when multiple flags available for one command 
  (``-f, --file [METAVAR]``  **instead of** ``-f [METAVAR] --file [METAVAR]``)
* argument flags are coloured `white` to standout from their descriptions.

logging tweaks
...............

* colour-coded logging (on windows too) (borrowed from `unutbu` and `sorin` on stackoverflow)
* some useful logfilters (borrowed from `unutbu` and `sorin` on stackoverflow)
* reuse existing loghandlers if already built in interactive python shells.
* short string-based argument to quickly modify log-verbosity/logformat



Usage
------

QuickStart
..............

This is all you need to do to create a CLI interface that matches
the format above:

.. code-block:: python

   import supercli.argparse

   parser = supercli.argparse.ArgumentParser(
               autocomp_cmd = 'myprogram',     ## name of command autocompletions are generated for
               description  = 'This descriptions can have `ReStructuredText` in it.',
               )


.. code-block:: bash

   myprogram --gen-autocomp   ## create ZSH autocompletion script in current dir



argparse
........

This is just a collection of subclasses of the real `argparse` module,
and the usage is mostly the same.


.. code-block:: python

   import supercli.argparse
   from pygments.lexers      import HtmlLexer
   from pygments.formatters  import Terminal256Formatter

   parser = supercli.argparse.ArgumentParser(
               autocomp_cmd = 'myprogram',                ## name of command autocompletions are generated for
               description  = 'This descriptions can have `ReStructuredText` in it.',

               helpline_lexer     = HtmlLexer,            ## use a different lexer or formatter
               helpline_formatter = Terminal256Formatter, #  if you'd like

               extended_logopts   = True,                 ## enable flags for log options related to 
                                                          #  logging to files

               developer_opts     = True,                 ## make `invisible` dev commands visible in 
                                                          #  help menu for users

               loghandlers        = None,                 ## if logformat or loghandlers don't suit your needs
                                                          #  you can manage and pass your own formatted 
                                                          #  loghandlers.
                                                          #  (-v|-vv) flags will stil work
           )



logging
.......

If you'd like, you can also use the logging module independently of
the argparse module. Once again, nothing really new or mindblowing here, 
this is purely convenience.


loglevel/logformat
``````````````````
The first argument, ``str_arg`` is a shorthand way of changing the loglevel
and logformat.

.. code-block:: python

   import supercli.logging
   import logging

   logger = logging.getLogger(__name__)

   ## loglevel
   supercli.logging.SetLog( )                                        ## log to stderr (using loglevel==logging.INFO by default)
                                                                     #  each logrecord is prefixed by the datetime
   supercli.logging.SetLog(lv=10, logfmt='dev')                      ## print method names
   supercli.logging.SetLog(lv=10, logfmt='long')                     ## print module import-path, method name, etc. uses 2x lines
   supercli.logging.SetLog(lv=10, logfmt='stack')                    ## prints 5x levels of the stacktrace for each logrecord
   supercli.logging.SetLog(lv=10, logfmt='stack', stack_logging=10 ) ## prints 10x levels of the stacktrace for each logrecord

   supercli.logging.SetLog('i')                  ## loglevel==logging.INFO
   supercli.logging.SetLog('w')                  ## loglevel==logging.WARNING
   supercli.logging.SetLog('v')                  ## loglevel==logging.DEBUG
   supercli.logging.SetLog('vv')                 ## loglevel==logging.DEBUG and disable all logfilters

   ## the long way
   supercli.logging.SetLog( lv='INFO' )


   ## logformat
   supercli.logging.SetLog('d')   ## (developer) instead of datetime, display __name__ and line-number
   supercli.logging.SetLog('l')   ## each log-entry takes 2x lines (full import-path & func, time, lineno, etc)

   ## these can be combined
   supercli.logging.SetLog('dv') ## (developer) and (verbose) flags are both active


logfile
```````
99.9% of the time when I want to log to a file, I want to use a ``RotatingLogHandler``.
I'm guessing this is the case for most people, so it is the default behaviour.


.. code-block:: python

   import supercli.logging
   import logging

   logger = logging.getLogger(__name__)

   supercli.logging.SetLog( 
      lv           = 'INFO',
      logfile      = '/path/to/myfile.log',
      logstream    = False  ,               ## optionally, disable logging to STDERR
      logfile_size = 1000000,               ## =~8mb
      debug_mode   = False,                 ## this module is peppered with print() statements
                                            #  to assist in debugging. This displays them.
   )


logfilters
``````````

LogFilters let you filter out logrecords based on some information.
There are two logfilters in ``supercli.logging``, but any ``logging.Filter``
subclass will work.

By default ``SetLog()`` is set up to use ``supercli.logging.BlackList`` as it's filter.
Each record is matched against the calling function's **import-path + function-name**.

ex:

.. code-block:: python

   fnmatch.fnmatch( filter_value, '*{import_path}.{function_name}*' )


.. code-block:: python

   from   supercli.logging import SetLog, Blacklist
   import logging

   logger = logging.getLogger(__name__)

   SetLog(
      lv             = 'INFO'               ,
      logfile        = '/path/to/myfile.log',
      logstream      = True                 ,
      filter_matches = ['sqliface.','chatty.module.func'],   ## filters records matching  
                                                             #   '*sqliface.*', 
                                                             #   '*chatty.module.func*' 

      filter_type    = Blacklist,                            ## BlackList is the default
   )






Todo
----

* tests
* bash autocompletion scripts
* (zsh) completion types (_file,_netwkiface,...)
* needs more flexible handling of ackward environments like maya.
  (I'm assuming all autodesk products have their own loghandlers for
  script-editors and the like)
* make logging.WhiteList work like Blacklist works.
* WhiteList and BlackList need to be able to be used together
* Show a more generic use of command in picture.. 


Thanks
-------

* `colorama` authors for filling cmd.exe with colourful text, instead of the room with colourful language.
* stackoverflow users `unutbu` and `sorin` for windows-colour/logfilter solutions.



