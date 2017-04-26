=========================
YD Technology Common libs
=========================

.. image:: https://travis-ci.org/ArabellaTech/ydcommon.png?branch=master
   :target: http://travis-ci.org/ArabellaTech/ydcommon

.. image:: https://coveralls.io/repos/ArabellaTech/ydcommon/badge.png?branch=master
   :target: https://coveralls.io/r/ArabellaTech/ydcommon/
   
.. image:: https://requires.io/github/ArabellaTech/ydcommon/requirements.svg?branch=master
     :target: https://requires.io/github/ArabellaTech/ydcommon/requirements/?branch=master
     :alt: Requirements Status


System Requirements
===================
- Python 2.7+

Settings
========
- ``IGNORE_QUNIT_HTML_FILES`` ignore HTML qunits files
- ``JSHINT_FILES_FIND`` JS Hint search files grep. Default ``-name "*.js" | xargs grep -l '/\*jslint' | grep -v libs``

Views
=====

``QunitTestsView`` Qunit tests (stuff permission required), example entry in urls.py:

::

    url(r"^js-tests/(?P<path>.*)", 'ydcommon.views.qunit_view', name='quinit'),

Commands
========

Checking requirement for tests:

::

    ./manage.py check_test_requirements

Running Qunit tests

::

    ./manage.py run_qunit

Running JS Hint

::

    ./manage.py jshint


Running JS Hint with custom directory

::

    ./manage.py jshint --dir=my/custom/dir


Clear database - drop all tables

::

    ./manage.py clear_database

Dump database

::

    ./manage.py dump_database
