=====
Emtex Common Utils
=====

This contains utility like permissions, audit log etc.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "emtex_common_utils" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'emtex_common_utils',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^emtex-common-utils/', include('emtex-common-utils.urls')),

3. Run `python manage.py migrate` to create the emtex_common_utils models.
