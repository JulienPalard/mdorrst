=================================================
spigot - rate-limited feed aggregation to pump.io
=================================================

About Spigot
============

Spigot takes syndicated content feeds and posts them to pump.io
accounts at a limited rate. This way you can syndicate content to a
pump.io account without worrying about flooding the account when
updates to the feed are frequent.

First you add RSS or Atom feeds, specifying which account to post to,
the maximum post frequency, and the format of the posted
message. Spigot will verify and authorize the account once, after
which it can be reused for additional feeds. Each time spigot runs, it
checks the feeds for new posts, and determines whether or not a new
item should be posted based on the specified interval. Spigot can be
run in a cron job (or manually) to make regular posts.

Spigot is inspired by Tricklepost and Brdcst.it. 


Requirements
============

spigot depends on Python 2.6 or higher and the following non-standard libraries

- pypump = 0.6 https://pypi.python.org/pypi/PyPump
- Universal Feed Parser >= 5.0 http://www.feedparser.org/
- argparse >= 1.0 (required for Python 2.6) 

Git Repo
========

Spigot's code is hosted on GitHub: https://github.com/nathans/spigot

  
Installation
============

You can install spigot via pip:

    $ sudo pip install spigot

Or you can clone the git repo and install manually:

    $ sudo python setup.py install

If you are using a virtualenv, you can omit the sudo.


Configuration
=============
To configure spigot for first use, run it from the command-line:
    $ spigot.py

You will be prompted to configure one feed and its account.

To add a new feed:
    $ spigot.py --add-feed


Running
=======

After initial configuration, running spigot will poll your feeds and
post to the configured accounts if the intervals allow. Running
without specifying any options will result in no console output unless
there are warnings or errors.  This is optimal for running spigot as a
cron job. To view more verbose logging, you can specify
the --log-level option.


Cron
====

Spigot can be run as a cron job to make sure that the flow of posts is
regular.  Here is an example crontab entry to run every at the 10th
minute of each hour:

    10 * * * * cd ~/spigot; spigot.py

Remember, spigot looks for its database and configuration file in the
current working directory.


FAQ
===

How can I upgrade an existing install of spigot?
------------------------------------------------

There are two basic steps. First upgrade the code version, then update
your configuration file and database to be compatible with the latest
version of spigot.

If you installed via pip, simply run:

    $ pip install spigot --upgrade

If you installed manually, be sure to update PyPump to version 0.6.

The source code includes a script in the utils folder called
convert.py. Run that in the same folder as your configuration file and
database, and the script will modify your database and configuration
file to work with the newest release of spigot.

After obtaining the source:

    $ python utils/convert.py

The upgrade script creates a backup of both files in case anything
goes wrong.

Where does Spigot store its configuration files and database?
-------------------------------------------------------------

Spigot stores its configuration (spigot.json) and database (spigot.db)
in the working directory from which it is invoked. If you are running
Spigot from a cron job, you'll want to first cd into the directory
containing these.

Starting with version 2.3.0, spigot delegates the storage of
credentials to PyPump. These are stored by default in
~/.config/PyPump/credentials.json

How often should I run Spigot?
------------------------------

There are a couple factors which weigh on this. First, you want to run
it often enough so that catches all of the posts in the feeds it is
polling. For example, if you are polling a feed which lists 10 items
and is updated about 5 times per hour, you need to run Spigot at least
every 2 hours to catch all of those posts in its database.

Second, you'll want to run Spigot more often than the shortest
interval in your configuration. If you run spigot less often than the
shortest interval, posts will effectively happen only as often as
Spigot runs.

In brief, Spigot should run more often than you want to actually post.


Credits
=======

(c) 2011-2015 Nathan D. Smith <nathan@smithfam.info>
(c) 2014 Craig Maloney <craig@decafbad.net>

License
=======

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.
