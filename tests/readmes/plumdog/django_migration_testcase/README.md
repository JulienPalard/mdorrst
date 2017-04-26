# django_migration_testcase
[![Build Status](https://travis-ci.org/plumdog/django_migration_testcase.svg?branch=master)](https://travis-ci.org/plumdog/django_migration_testcase)

For testing migrations in Django >= 1.4 (both South and Django migrations)

Because migrations are important. And if they go wrong, people get
angry. How better to be sure that they won't go wrong than to run
tests.

I found [this article](https://micknelson.wordpress.com/2013/03/01/testing-django-migrations/)
on writing tests around South migrations, which I had used, but as of
Django 1.7, I was out of luck. So I wrote this. It also supports
Django 1.4, 1.5 and 1.6.

This project is very much in its infancy, and I'd be really interested
to know how others get on. Also, if there's a better strategy or
existing library, I'd love to know about it.

If there's anything not made clear in this README, please open an
issue.

Quickstart
----------

```python

from django_migration_testcase import MigrationTest


class MyMigrationTest(MigrationTest):

    # At present, we can only run migrations for one app at a time.
    app_name = 'my_app'
    # Or just the numbers, if you prefer brevity.
    before = '0001_initial'
    after = '0002_change_fields'

    # Can have any name, is just a test method. MigrationTest
    # subclasses django.test.TransactionTestCase
    def test_migration(self):
        # Load some data. Don't directly import models. At this point,
        # the database is at self.before, and the models have fields
        # set accordingly. Can get models from other apps with
        # self.get_model_before('otherapp.OtherModel')

        MyModel = self.get_model_before('MyModel')

        # ... save some models

        # Trigger the migration
        self.run_migration()

        # Now run some assertions based on what the data should now
        # look like. The database will now be at self.after. To run
        # queries via the models, reload the model.

        MyModel = self.get_model_after('MyModel')
```


Migrating Multiple Apps
-----------------------

If you want to test that two apps in different apps play nicely
together, you can set `self.before` and `self.after` as a list of
two-tuples, each of which should be `([[app-name]],
[[migration]])`. (This is done this way rather than as a dict because
order may matter - migrations are run in the order they are listed.)

Eg
```python
class MigrateBothMigrationTest(MigrationTest):
    # Don't set app_name on the class, because there isn't one.
    before = [('test_app', '0001'), ('test_second_app', '0001')]
    after = [('test_app', '0002'), ('test_second_app', '0002')]
```

Then, in your `test_*` methods, when you need to get a model, you must
specify the app name (if you're only testing one app, then it can look
at `self.app_name`). So you can't do
`self.get_model_before('MyModel')`, you have to do
`self.get_model_before('test_app.MyModel')`.

Migration Versions
------------------

By setting the migration version as `'zero'`, this sets the target
migration as before the first migration.

In cases where two migrations have the same number-prefix, you can
specify the full version to resolve this. Or you can use the full
version anyway in the name of explicitness.

Relationships between models in different apps
----------------------------------------------

This works in with Django's migrations. But (at present) doesn't with
South. There's an additional problem with South, as the metadata for a
migration doesn't contain the state of all models, just those that
were frozen. So how does your test work out what a model should look
like for a migration, if the migration itself doesn't know? Answers in
a PR please, or just any suggestions.

How it works
------------

In Django's migrations, when writing data migrations, rather than
directly importing models, you load them using `apps.get_model()` --
see
[here](https://docs.djangoproject.com/en/1.7/topics/migrations/#data-migrations).
I've tried to unravel the migrations framework to do the same thing
here, so that we load models dynamically.

The `migrate` and `migrate_kwargs` methods
------------------------------------------

The test method has a `migrate` method that takes an app name, a
version and an optional `fake` boolean. By default, this just calls:
```python
call_command('migrate', app_name, version,
             fake=fake, verbosity=0, no_initial_data=True)
```

If you need to alter your migrate command, you can either override
this method, or you might just override `migrate_kwargs`, which by
default sets `verbosity=0` and `no_initial_data=True`. Extend this to
pass more options/different options. Note that if you try to set a
`fake` kwarg from this method, it will be ignored.

Tests
-----

There's a test app that has four migrations. It is linked to different
projects within the test directory, one that uses postgres, and one
that uses sqlite3, and one for each but with South. To run the tests,
`pip install django psycopg2 [south] -e .` then `./run_tests.sh`. Or,
to cover all supported Django and Python versions: `pip install tox`
then `tox`.