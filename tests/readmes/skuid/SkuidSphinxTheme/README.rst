Skuid Sphinx Theme
##################

This repository contains Skuid's Sphinx theme.

Install
=======

To install, run the following command and input your bitbucket credentials::

    pip install skuidsphinxtheme


If you plan on editing this and want to dynamically update this theme for use
in another project, clone this repo down and then run::

    pip install -e .

Use
===

To use in another project, add this project to the ``setup.py`` file's
``install_requires``  directive::

    setup(
        ...
        install_requires=[
            'SkuidSphinxTheme>=1.0.0',
        ]
    )

or add it to the project's ``requirements.txt`` file

Then add in the ``conf.py`` of your sphinx project::

    html_theme = 'skuidsphinx'

    # TODO: We'd like this rolled into the theme, hopefully we can remove this later
    html_sidebars = {'**': ['localtoc.html']}

Theme Options
=============
To configure the theme for your project, you'll need to configure the
``html_theme_options`` in your project's ``conf.py`` file. See the variables
section below for a full list of options.
::

    html_theme_options = {
        'logo': 'skuid.png',
        'logo_alt': 'Skuid Documentation',
    }


Variables
---------

* ``logo``: Relative path (from $PROJECT/_static/) to a logo image, which will appear in the upper left corner above the name of the project.

    * See the note below about image paths.
* ``logo_alt``: The alt text for the logo
* ``visit_link``: The link for the visit button in the footer
* ``visit_link_text``: The text for the visit button in the footer
* ``copyright_year``: The year for the copyright.

    * To make things easier, add the following to your ``conf.py``::

        # At the top
        from datetime import datetime

        # in the ``html_theme_options``
        html_theme_options = {
            'copyright_year': datetime.utcnow().year
        }
* ``analytics_id``: Set to your Google Analytics ID (e.g. UA-#######-##) to enable tracking.

Images
------

If you're using a custom logo, you'll also want to tell Sphinx where to get
your images from. If so, add a line like this (changing the path if necessary;
see the Sphinx docs for 'html_static_path')::

    html_static_path = ['_static']


TODO
====

* Document all configurable ``html_theme`` options (from the ``theme.conf``)
* Figure out how to make ``html_sidebars`` option default for projects using this theme
* Clean up search results page

    * Add search box
    * Add some padding on the left of results

Authors
=======

`Shannon Hale`_

.. _`Shannon Hale`: shannon@skuid.com

`Cody Taylor`_

.. _`Cody Taylor`: cody@skuid.com