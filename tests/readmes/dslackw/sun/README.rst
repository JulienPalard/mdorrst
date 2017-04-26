.. image:: https://img.shields.io/github/release/dslackw/sun.svg
    :target: https://github.com/dslackw/sun/releases
.. image:: https://travis-ci.org/dslackw/sun.svg?branch=master
    :target: https://travis-ci.org/dslackw/sun
.. image:: https://landscape.io/github/dslackw/sun/master/landscape.png
    :target: https://landscape.io/github/dslackw/sun/master
.. image:: https://img.shields.io/codacy/ea3c2619e1124874a7d53079092dc956.svg
    :target: https://www.codacy.com/public/dzlatanidis/sun/dashboard
.. image:: https://img.shields.io/pypi/dm/sun.svg
    :target: https://pypi.python.org/pypi/sun
.. image:: https://img.shields.io/badge/license-GPLv3-blue.svg
    :target: https://github.com/dslackw/sun
.. image:: https://img.shields.io/github/stars/dslackw/sun.svg
    :target: https://github.com/dslackw/sun
.. image:: https://img.shields.io/github/forks/dslackw/sun.svg
    :target: https://github.com/dslackw/sun
.. image:: https://img.shields.io/github/issues/dslackw/sun.svg
    :target: https://github.com/dslackw/sun/issues

.. contents:: Table of Contents:

About
-----

Let's SUN:sunny:(shine)!!!


SUN (Slackware Update Notifier) is a tray notification applet for informing about
package updates in Slackware and CLI tool for monitoring upgraded packages.

.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/sun.png
    :target: https://github.com/dslackw/sun

How works
---------

Actually read the two dates of ChangeLog.txt files one the server and a local by counting
how many packages have been upgraded, rebuilt or added.
SUN works with `slackpkg <http://www.slackpkg.org/>`_ as well with `slpkg <https://github.com/dslackw/slpkg>`_
 

Installing
----------

.. code-block:: bash

    Required root privileges

    $ tar xvf sun-1.2.1.tar.gz
    $ cd sun-1.2.1
    $ ./install.sh

    Installed as Slackware package

    or

    $ pip install sun --upgrade


Usage
-----

Choose ONE mirror from '/etc/slackpkg/mirrors' file.


Gtk menu icon
-------------

Add sun in your windows manager session startup.

As for xfce:
Settings Manager --> Session and Startup --> Application Autostart --> +Add

.. code-block:: bash
    
    [Add application]

    Name: sun
    Description: Slackware Update Notifier
    Command: /usr/bin/sun_gtk &
    
    Click [Ok]

    Click Menu --> System --> SUN (Slackware Update Notifier)
    An icon will appear in the panel, right click in SUN icon to show menu.

    Thats it.
    
CLI
---

.. code-block:: bash

    $ sun help
    SUN (Slackware Update Notifier) - Version: 1.2.1

    Usage: sun [OPTION]

    Optional arguments:
      help     display this help and exit
      start    start sun daemon
      stop     stop sun daemon
      restart  restart sun daemon
      check    check for software updates
      status   sun daemon status
      info     os information

    $ sun start
    Starting SUN daemon:  /usr/bin/sun_daemon &

    $ sun stop
    Stopping SUN daemon:  /usr/bin/sun_daemon

    $ sun status
    SUN is not running
    
    $ sun check
    3 software updates are available

    samba-4.1.17-x86_64-1_slack14.1.txz:  Upgraded.
    mozilla-firefox-31.5.0esr-x86_64-1_slack14.1.txz:  Upgraded.
    mozilla-thunderbird-31.5.0-x86_64-1_slack14.1.txz:  Upgraded.


Configuration files
-------------------

.. code-block:: bash

    /etc/sun/sun.conf
        General configuration of sun

    /etc/rc.d/rc.sun
        Runtime configuration file

    
Screenshots
-----------

.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/gtk_daemon.png
    :target: https://github.com/dslackw/sun


.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/xfce_screenshot.png
    :target: https://github.com/dslackw/sun


.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/kde_screenshot.png
    :target: https://github.com/dslackw/sun


.. image:: https://raw.githubusercontent.com/dslackw/images/master/sun/check_updates.png
    :target: https://github.com/dslackw/sun

 
Donate
------
If you feel satisfied with this project and want to thank me go
to `Slackware <https://store.slackware.com/cgi-bin/store/slackdonation>`_ and make a donation 
or visit the `store <https://store.slackware.com/cgi-bin/store>`_.


Copyright 
---------

- Copyright © Dimitris Zlatanidis
- Slackware® is a Registered Trademark of Patrick Volkerding.
- Linux is a Registered Trademark of Linus Torvalds.
