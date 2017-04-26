==========================
Django Autometrics Non-Rel
==========================

This package installs models and middleware used to simplify user tracking across sessions and correlate access to resources to the user requesting such access.

Some of the tools in this project assume you are running in a non-relational environment (so far only Google App Engine is supported) for your views of interest. As such, the project depends on the `djangae` package. Some day perhaps I will split this into relational and non-relational sub-packages.


Quick start
-----------

The easiest way to use `django-autometrics-nonrel` is to use the `RestFrameworkGenericViewSetAutoMetricsMixin` to provide built-in recording of user retrieval of entities:

Add the project to your `INSTALLED_APPS`:

    INSTALLED_APPS = [
        ...
        'autometrics_nonrel',
        ...
    ]

Add the middleware to `MIDDLEWARE_CLASSES` anywhere *after* `SessionMiddleware`:

    MIDDLEWARE_CLASSES = (
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'autometrics_nonrel.middleware.UserSessionTrackingMiddleware',
        ...
    )

Use the mixin on your Django REST Framework `GenericViewSet` (or any viewset derived from `GenericViewSet`) to automatically log user access to items:

    from rest_framework import viewsets
    from autometrics_nonrel import mixins
    from myapp.models import MyModel
    class MyViewSet(
            viewsets.ReadOnlyModelViewSet,
            RestFrameworkGenericViewSetAutoMetricsMixin
    ):
        model = MyModel
        queryset = MyModel.objects.all()
        ...
