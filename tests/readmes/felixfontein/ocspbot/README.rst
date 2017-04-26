OCSP Bot
========

The OCSP Bot's job is to make sure up-to-date OCSP responses are kept
for a set of certificates.

The bot should be run as a cronjob regularly (like, once per hour) and
will attempt to obtain OCSP responses for certificates for which

- no valid OCSP response is currently stored, and
- the existing OCSP response is expiring soon enough.

The criteria for “expiring soon enough” can be defined in the
configuration.

To install, use ``pip install ocspbot``. If you want a one-file version,
please rename ``ocspbot/__main__.py`` to ``ocspbot.py`` and use that one.


Requirements
------------

OCSP Bot needs `pyyaml <http://pyyaml.org/>`__ and `OpenSSL <https://www.openssl.org/>`__.
It has been tested with OpenSSL 1.0.x, but not yet with OpenSSL 0.9.x and 1.1.x.


Command Line Interface
----------------------

The OCSP Bot can be invoked as follows::

  ocspbot.py [ <config file> ] [ -h | -help | --help ] [ -v | -version | --version ]

In case ``-h``, ``-help`` or ``--help`` is specified, a short help text
will be printed. In case ``-v``, ``-version`` or ``--version`` is specified,
the program's version will be printed.

If no configuration file name is specified, it will use ``ocspbot.yaml``.
The configuration file will be parsed and the certificates specified
therein will be processed.

OCSP Bot returns 0 for success (without changes), a positive return value
for the number of OCSP responses renewed, and negative return values for
errors:
  
+-------------+--------------------------------------------------------------------------------+
| Return Code | Meaning                                                                        |
+=============+================================================================================+
|          -1 | An error occured while retrieving OCSP responses                               |
+-------------+--------------------------------------------------------------------------------+
|          -2 | An error occured while parsing the configuration (parsing YAML, start logging) |
+-------------+--------------------------------------------------------------------------------+
|          -3 | An error occured while parsing the configuration (interpreting configuration)  |
+-------------+--------------------------------------------------------------------------------+
|          -4 | Invalid command line arguments                                                 |
+-------------+--------------------------------------------------------------------------------+

Non-zero return values can be used to reload services which deliver the OCSP
responses. In case of negative return values, manual user invention might be
needed.


Configuration File Format
-------------------------

Configuration files must be in `YAML format <https://en.wikipedia.org/wiki/YAML>`__.
They can contain the following keys:

- ``ocsp_folder``: ``<string>``

  The folder in which the OCSP responses are stored. All OCSP response paths
  will be interpreted relatively to this path.

  Default value is the empty string, i.e. the current directory.

- ``minimum_validity``: ``<string>``

  If an OCSP response is newer than the described time interval, the program
  will try to renew it. The string is interpreted as a list of space separated
  tokens of the form::

      ? s, ? sec, ? second, ? seconds
      ? m, ? min, ? minute, ? minutes
      ? h, ? hour, ? hours
      ? d, ? day, ? days
      ? w, ? week, ? weeks

  Examples:

  - 2 hours 5 minutes 10 seconds
  - 1w 3d 5h

- ``minimum_validity_percentage``: ``<number>``

  Specifies a percentage (between ``0`` and ``100``). If this percentage of the
  OCSP response's lifespan has elapsed, the response is renewed.

- ``parallel_threads``: ``<number>``

  An integer specifying how many threads should be run in parallel.
  Default value is ``1``.

- ``stop_on_error``: ``<boolean>``

  Specifies whether to stop on the first error found when processing OCSP
  responses, or whether to try to renew all.

- ``make_backups``: ``<boolean>``

  If set to True, new OCSP responses are also copied in the ``ocsp_folder``
  directory to ``<filename>-<timestamp>`` as a backup (to keep track which
  OCSP response was used when). Default value is ``False``.

- ``openssl_executable``: ``<string>``

  The OpenSSL executable to use. Default is ``openssl``.

- ``domains``: ``<dict>``

  The dictionary maps a domain identifier to a dictionary with the
  following entries:

  - ``cert``: ``<string>``
  - ``chain``: ``<string>``
  - ``rootchain``: ``<string>``
  - ``ocsp``: ``<string>``

  The domain identifier will be used in the output messages.

  The strings in the inner dictionaries must be paths specifying:

  - The certificate;
  - The certificate's chain (excluding the certificate itself and
    the root);
  - The certificate's root chain (i.e. the chain excluding the
    certificate itself, but including the root);
  - The OCSP response.

  The paths are relative to the current working directory, except
  for the OCSP response, where the paths are relative to ``ocsp_folder``.

- ``scan_keys``: ``<list>``

  Every list entry must be a dictionary with the following entries:

  - ``folder``: ``<string>``

    Default: (empty string, i.e. current working directory)

  - ``recursive``: ``<boolean>``

    Default: ``True``

  - ``cert_mask``: ``<string>``

    Default: ``{domain}.pem``

  - ``chain_mask``: ``<string>``

    Default: ``{domain}-chain.pem``

  - ``rootchain_mask``: ``<string>``

    Default: ``{domain}-rootchain.pem``

  - ``ocsp_mask``: ``<string>``

    Default: ``{domain}.ocsp-resp``

  For each dictionary, the program searches for all triples of files
  (cert, chain, rootchain) in the specified folders (and its subfolders
  if ``recursive`` is ``True``) which match the masks for the domain
  identifier ``{domain}``; the corresponding OCSP response filename is
  chosen.

  When scanning recursively, and triples are found in subfolders, the
  relative path of the triple's files to the folder to scan is prepended
  to the OCSP response filename.

- ``includes``: ``<list>``

  A list of folders which will be searched for YAML files with extensions
  ``.yml`` and ``.yaml``. All found YAML files will be parsed and
  ``domains`` and ``scan_keys`` entries processed as in the main
  configuration file.

- ``output_log``: ``<string>``

  ``error_log``: ``<string>``

  Writes output respectively error output into log files and not to
  ``stdout`` resp. ``stderr``. The filenames will be formatted with
  the following replacements:
  
  - ``{year}``: the current year (four digits)
  - ``{month}``:  the current month, 1 to 12 (two digits)
  - ``{day}``: the current day per month, 1 to 31 (two digits)
  - ``{hour}``: the current hour, 0 to 23 (two digits)
  - ``{minute}``: the current minute, 0 to 59 (two digits)
  - ``{second}``: the current second, 0 to 59 (two digits)


Example Configuration File
--------------------------

The following configuration file updates OCSP responses for ``example.com``
and ``example.org`` so that the responses are valid at least for three days
or 42.8% of their validity period. Backups will be created, and ``stdout``
output will be logged. The certificates are taken from
``/var/www/tls/certs/``, and the responses will be written to
``/var/www/ocsp/responses`` with backups.

The minimum validity parameters are tuned for
`Let's Encrypt <https://letsencrypt.org/>`__. When running the CERT Bot
once per hour for some time, ``/var/www/ocsp/responses`` might have the
following files::

    example.com.ocsp-resp
    example.com.ocsp-resp-20170415-060000
    example.com.ocsp-resp-20170418-060000
    example.com.ocsp-resp-20170421-060000
    example.org.ocsp-resp
    example.org.ocsp-resp-20170415-060000
    example.org.ocsp-resp-20170418-060000
    example.org.ocsp-resp-20170421-060000

The current valid OCSP responses will be ``example.com.ocsp-resp`` and
``example.org.ocsp-resp``, with the last update having been on
April 21, 2017 at 06:00 am.

The configuration file:

.. code:: yaml

    ---
    openssl_executable: openssl

    minimum_validity: 3d
    minimum_validity_percentage: 42.8

    ocsp_folder: /var/www/ocsp/responses

    parallel_threads: 1

    output_log: /var/www/ocsp/logs/example-{year}{month}{day}-{hour}{minute}{second}.log

    make_backups: True

    domains:
      example.com:
        cert: /var/www/tls/certs/example.com.pem
        chain: /var/www/tls/certs/example.com-chain.pem
        rootchain: /var/www/tls/certs/example.com-rootchain.pem
        ocsp: example.com.ocsp-resp
      example.org:
        cert: /var/www/tls/certs/example.org.pem
        chain: /var/www/tls/certs/example.org-chain.pem
        rootchain: /var/www/tls/certs/example.org-rootchain.pem
        ocsp: example.org.ocsp-resp
