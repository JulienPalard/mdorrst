Picks - View, pick and tag pictures
===================================

Despite there are lot's and lot's of file viewers out there *none* of them
satisfied a couple of (simple) requirements which are important for me:

- Support for 'interesting file separation' (by **copying/linking a file**
  to a special folder while viewing) (Gwenview has this, but it's broken)
- **File tagging** without a proprietary database (best would be using the
  filename to store tags because this is intuitive and platform/tool
  independent)
- Sexy **slide show** mode (e.g. with Ken Burns effect (pan/zoom))
- Support at least for **Linux**

This is why `picks` (play on the words *picture* and *pick*) emerged. Among
the features already mentioned the project goals are:

- **Easy deployment/usage** on at least Linux/MacOS/Windows
- **Easy interaction** (e.g. without the need to use a mouse)
- Support for reading from attached **smart phones** (MTP support)
- Tools for deciding whether to **keep or delete** a file (focus peaking, etc.)


Installation / Usage
--------------------

Recommended way to install picks is via **pip**::

    pip3 install picks

If you want to have the latest bugs::

    git clone https://github.com/frans-fuerst/picks
    cd picks
    ./setup.py install

Run ``picks`` like this::

    picks [<DIR>]

.. Note:: you have to run picks inside the directory containing the pictures
          you want to view or provide it on command line - there's no
          navigation inside the application yet.

There is also a command line mode but very few commands right now. E.g. you
can *initialize* the filenames of all pictures inside a directory::

    picks --initialize <DIR>
