Simple log monitor for PostgreSQL CSV logs.

To enable CSV logs, please refer to the PostgreSQL docs.

This monitor takes into account that some queries might contain newlines, and
properly parses the records.


Installation::

    pip install --user git+https://github.com/exhuma/postgresql-logmon.git


After running as user installation like above, run it like this::

    ~/.local/bin/pglogmon --help

Or start monitoring right away::

    ~/.local/bin/pglogmon /psth/to/postgresql.csv
