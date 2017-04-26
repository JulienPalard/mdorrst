=====================
Django IP Restriction
=====================

Department of International Trade Django IP Whitelist.  A Django middleware to restrict incoming IPs to a Django project to a list of allowed IPs or IP ranges.  Access to the admin login screen, and access to authenticated users are configurable, so it can be set such that users can authenticate, and bypass the IP restriction for the site.

Requirements
------------

* Python >= 3.3
* Django >= 1.9


===========
Quick start
===========

#. Install the package::

    $ pip install django-ip-restriction

#. Add the middleware to your settings (Note: the minimum necessary other middleware components are Django's `SessionMiddleware` and `AuthenticationMiddleware`, these are added by default to your settings)::

    # Django 1.9
    MIDDLEWARE_CLASSES = [
        ...
        'ip_restriction.IpWhitelister',
        ...
    ]

    # Django 1.10+
    MIDDLEWARE = [
        ...
        'ip_restriction.IpWhitelister',
        ...
    ]


=============
Configuration
=============

Turning on or off, and configuring the IP whitelist is done either via variables in your Django settings, or via environment variables.  Values in Django settings take preference over values in the environment.

Turning on/off the middleware is done via ``RESTRICT_IPS``, and the default value is False.  Either set this variable to True in Django settings, or set a truthy value (e.g. 'true', '1') in your environment.  

Individual IPs can be whitelisted via ``ALLOWED_IPS``, which is either a list of IP strings in Django settings, or a comma-separated list of IPs in the environment, e.g the following 2 are equivalent::

    # in bash (spaces are disregarded, trailing commas are OK)
    export ALLOWED_IPS='192.168.0.1, 192.168.0.2,192.168.0.3,'
    
    # in settings.py (will override the above environment variable)
    ALLOWED_IPS = ['192.168.0.1', '192.168.0.2', '192.168.0.3']

IP ranges can be whitelisted via ``ALLOWED_IP_RANGES``, which is either a list of IP range strings (CIDR notation) in Django settings, or a comma-separated list of IP ranges in the environment, e.g.::
    
    # in bash
    export ALLOWED_IP_RANGES='192.168.0.0/8, 127.0.0.0/2'
    
    # in settings.py
    ALLOWED_IPS = ['192.168.0.0/8', '127.0.0.0/2']

Regardless of the IP addresses/rages that are in the whitelist, access for all authenticated users can be allowed with ``ALLOW_AUTHENTICATED``.  If true, this will allow any valid sessions past the IP restriction.

Regardless of the IP addresses/rages that are in the whitelist, access to the admin URLs is also allowed past the IP restriction if ``ALLOW_ADMIN`` is true.

Setting both ``ALLOW_ADMIN`` *and* ``ALLOW_AUTHENTICATED`` to true is recommended, and will allow any user that can log in, to first access only the admin interface in order to authenitcate, and from then have access to all URLs for the project.


============
Contributing
============

Contributions are welcome. Please follow the guidelines below to make life easier:

* Fork the repo, branch off release, make changes, then make a pull request (PR) to release on the main repo
* Include documentation for any new features
* Please limit changes for a PR to a single feature, or a single bugfix
    - Make multiple PRs for multiple discrete changes
* Please squash commits - ideally a single commit, but at least to a sensible minimum
    - If a PR reasonably should have multiple commits, consider if it should *actually* be separate PRs


=======
License
=======

MIT licensed. See the bundled `LICENSE  <https://github.com/uktrade/dit-ip/blob/master/LICENSE>`_ file for more
details.


====
TODO
====

* Allow the IP restriction to work in a blacklisting mode, rather than just a whitelisting mode
* Get continuous integration to run on multiple python versions from 3.0+ 
    - Currently only running on 3.5.0
    - Utilise parallelism
* Run tests on multiple Django versions
    - Currently only running against Django 1.9
    - Utilise parallelism
