============
Health Check
============

:Version: 3.1.0
:Status: Production/Stable
:Author: José Antonio Perdiguero López

Health Check is an application that provides an API to check the health status of some parts and some utilities like
ping requests. This application can works as standalone or included in a Django project.

Quick start
===========

#. Install this package using pip::

    pip install health-check


#. Add *PROJECT_PATH* to your django settings module.
#. Add *health_check* to your **INSTALLED_APPS** settings like this::

    INSTALLED_APPS = (
        ...
        'health_check',
    )

#. Add **Health Check** urls to your project urls::

    urlpatterns = [
        ...
        url(r'^health/', include('health_check.urls')),
    ]

Check Providers
===============
Health Check provides a mechanism to add new custom check functions through **check providers**. Each check provider
will generate a new API method with an URL that uses the name of the provider. These functions must accept \*args and
\*\*kwargs and will return a JSON-serializable object through json.dumps() method, for example a ping function::

    def ping(*args, **kwargs):
        return {'pong': True}

By default **Health Check** provides the follow checks:

Ping
    A ping to application.
    URL: /api/health/ping

Databases
    Check if databases are running.
    URL: /api/health/databases

Caches
    Check if caches are running.
    URL: /api/health/caches

Celery
    Check if celery workers defined in settings are running.
    URL: /api/health/celery

Databases stats
    Show stats for all databases.
    URL: /api/stats/databases

Celery stats
    Show celery worker stats.
    URL: /api/stats/celery

Code
    Source code stats such as current active branch, last commit, if debug is active...
    URL: /api/stats/code

Health Check website
=====================
A website that shows Health Check data is available in this application. It's possible access to follow URLs to get a
detailed view of your system health status. Those three pages will show results of providers configured (as explained in
settings section)::

    http://www.website.com/health/
    http://www.website.com/health/health/
    http://www.website.com/health/stats/

Health Check API
=================
Health Check API can be used as a standalone application including only their urls::

    urlpatterns = [
        ...
        url(r'^health/', include('health.api.urls')),
    ]

This API have a single url for each provider, that are grouped by resources.
Each provider can be queried alone, returning his current health status::

    http://your_domain/health/api/health/ping

Also there is a resource view that will return the health status of all providers::

    http://your_domain/health/api/health

For last, there is a root view that will return the health status of all providers from all resources::

    http://your_domain/health/api

Django management commands
==========================
Health Check provides a django management command to query current health of a resource. This command can be call as::

    python manage.py health_check <resource> [options]

To get current status of health checks, and exit with an error if some check is failing::

    python manage.py health_check health -e

Each resource has its own set of options that can be displayed through command help::

    python manage.py health_check -h

Command
=======
Previous Django command can be used in standalone mode as::

    health_check <resource> [options]

Settings
========
Health check settings can be added directly to Django settings module or create an specific module for them. If a
custom module (or class) is used, you must specify it through **DJANGO_STATUS_SETTINGS** environment variable.

To use a custom module for settings is necessary to specify the full path: *project.package.settings*. The same applies
to objects: *project.package.settings:SettingsObject*.

health_check_providers
----------------------
List of additional check providers. Each provider consists in a tuple of name, function complete path, args and kwargs.
Example::

    health_check_providers = {
        'resource': (
            ('test', 'application.module.test_function', [1, 2], {'foo': 'bar'}),
        )
    }

Default::

    providers = getattr(settings, 'health_check_providers', {
        'health': (
            ('ping', 'health_check.providers.health.ping', None, None),
            ('databases', 'health_check.providers.django.health.databases', None, None),
            ('caches', 'health_check.providers.django.health.caches', None, None),
        ),
        'stats': (
            ('databases', 'health_check.providers.django.stats.databases', None, None),
            ('code', 'health_check.providers.stats.code', None, None),
        )
    }

health_check_celery_workers
---------------------
List of hostname from celery workers to be checked. If any worker is defined, two additional providers listed previously
will be added to default set.
Default::

    health_check_celery_workers = ()

