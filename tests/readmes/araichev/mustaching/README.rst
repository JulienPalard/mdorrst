Mustaching
***********

.. image:: http://mybinder.org/badge.svg 
    :target: http://mybinder.org:/repo/araichev/mustaching

.. image:: https://travis-ci.org/araichev/mustaching.svg?branch=master
    :target: https://travis-ci.org/araichev/mustaching

A Python 3.4+ package inspired by Mr. Money Mustache to summarize and plot personal finance data given in a CSV file.
Uses Pandas and Python-Highcharts to do most of the work.


Usage
=========
Play with the IPython notebook ``ipynb/examples.ipynb``.
You can do so online by clicking the Binder badge above.
You can even upload your own transaction data into the notebook, but consider first `Binder's warning about private data <http://docs.mybinder.org/faq>`_.

Your CSV of transactions should contain at least the following columns

- ``'date'``: string; something consistent and recognizable by Pandas, e.g 2016-11-26
- ``'amount'``: float; amount of transaction; positive or negative, indicating a credit or debit, respectively
- ``'description'`` (optional): string; description of transaction, e.g. 'dandelion and burdock tea'
- ``'category'`` (optional): string; categorization of description, e.g. 'healthcare' 
- ``'comment'`` (optional): string; comment on transaction, e.g. 'a gram of prevention is worth 16 grams of cure'

The business logic can be found in ``budgeting/main.py``


Documentation
==============
In docs and `on RawGit <https://rawgit.com/araichev/mustaching/master/docs/_build/singlehtml/index.html>`_.


Notes
========
- Development status: Alpha
- This project uses semantic versioning (major.minor.micro), where each breaking feature or API change is considered a major change


Authors
========
- Alex Raichev, 2016-11


History
========

2.0.1, 2017-04-26
-------------------
- Fixed the bug where ``setup.py`` could not find the license file.


2.0.0, 2017-04-25
-----------------
- Removed ``budget_and_freq`` option, because i don't need that extra complexity
- Calculated spending rate
- Added ``insert_repeating()`` to avoid having to record repeating transactions in my personal spendings
- Prepared for PyPi


1.2.1, 2017-03-01
-----------------
- Fixed README and ``ipynb/examples.ipynb``


1.2.0, 2017-03-01
------------------
- Lowercased category names and values when reading transactions
- Added percentages to bar chart stacks when splitting by categories
- Sorted categories from highest to lowest values in bar chart stacks
- Changed name to 'mustaching' and restructured directories
- Wrote automated tests


1.1.0, 2016-12-13
------------------
- Made ``read_ransactions()`` infer column names a little
- Made ``summarize()`` always create ``'period_budget'`` column and fill it with NaNs if no budget given


1.0.0, 2016-12-10
------------------
- Changed summary columns to ``'credit'``, ``'debit'``, and ``'balance'``
- Plotted balance as a cumulative sum line series


0.1.1, 2016-11-21
------------------
Fixed date labels and off-by-1-day error in time grouping


0.1.0, 2016-11-18
------------------
First release
