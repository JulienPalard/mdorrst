# Fleaker

Fleaker makes Flask devlopment easier by including glue and customizations for
popular support libraries such as:

* Marshmallow
* PeeWee

In addition to implementing improved Flask apps with more powerful:

* Configuration
* Components
* Exceptions

All in all, Fleaker makes developing for Flask more like developing for Python:
it's batteries included and you'll always be surprised with what's already
built.

## Usage

The main way to begin using Fleaker is simply to import: `fleaker.App` and
then call `create_app`, like so:

```python
import os

from fleaker import App


def create_app():
    app = App.create_app(__name__)

    # configure from settings module, and then the OS environment
    app.configure('settings', os.environ)

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
```

Run the above code and you can access your Flask app on: `localhost:5000`!


## Development

To lint, run this:

```sh
tox -e lint
```

And it will run both `flake8` and `pylint` for you.

@TODO: Probably move to CONTRIBUTING.md.

## Fixing an issue

See an issue or bug you wanna tackle? Awesome! Here's how you do it, using
a classic test-driven approach:

+ First you're going to want to clone the repository: `git clone
  git@github.com:croscon/fleaker.git` 
+ Write a test that produces the failure seen in the issue
  + Run all tests with this command (`py27` denotes a python 2 run environment):
    `tox -e py27`
  + Run a specific test by passing in the location like so **(note the
    space)**: `tox -e py27 -- tests/path-to-test-file`
+ Write various similar tests to see how they respond
	+ If they fail, you can try to address them in the fix for the original issue
	+ If they pass, no problem.
+ Use `tox` to run the tests and utilize the stack trace to locate the source
+ Once the source is located, go forth and fix it
+ Run tests to ensure all is well
  + Make sure to run `tox` without flags to ensure all environments are tested
    and passing


## The Ultimate Goal

Right now, setting up a Flask app can be a bit more time consuming and tedious
than it should be. You need to create factories, register blueprints, integrate
a host of extensions, and then you always seem to forget something simple, but
important, like properly configuring `logging`.

There are existing libraries that try to package `Flask` up into a nicer, more
abstract interface, but they're always too heavy handed or just not maintained.
Fleaker aims to solve that by building most of it's functionality in App Mixins
that can be chained together at will and configured as desired. Additionally,
Fleaker powers all projects at [Croscon](http://www.croscon.com), meaning it
gets a fair amount of usage and attention.

Fleaker still has a bit more work to go before it hits it's ideal API, but in
the long run this is what setting up a `Flask` app should look like:

```python
from os import env

from fleaker import App

from my_application.components import SessionComponent


# app factories are always a best practice
def create_app():
    # make your App and set the SessionComponent as the primary means of
    # interfacing with Flask-Login, who will extract methods based on names
    app = App.create_app(__name__, login_component=SessionComponent,
                         enable_logging=True)

    # configure from a settings_common.py, a settings_secret.py, and then the
    # environment.
    app.configure('.settings_common', '.settings_secret', env)

    # register all blueprints automatically in the `blueprints` module in this
    # package. Blueprints are registered with a generically named registration
    # function in each top level module
    app.register_blueprints('.blueprints')

    # there is one ELB in front of the app, so apply the standard proxy fix
    app.proxy_fix(1)
    return app
```

## Releases

The release process is fully automated via the `scripts/make_release.py`
script. All you need to have in order to run it is a `~/.pypirc` file with your
proper credentials and two sections: `pypi` and `pypitest`. It should resemble:

```cfg
[distutils]
index-servers=
  pypi
  pypitest

[pypi]
repository=https://pypi.python.org/pypi
username=yourusername
password=yourpassword

[pypitest]
repository=https://testpypi.python.org/pypi
username=yourusername
password=yourpassword
```

From there, the release process is as simple as creating the new entry in the
`CHANGES` file with the appropriate version number as the header, the date it
was released, and a summary of the changes. Like so:

```
Version 0.2.0
-------------

Released on March 31st 2017, codename Erlenmeyer.

The rise of the documentation and the opening of source...

- Added Sphinx integration for generating the documentation. Right now, it's
  mostly focued around generating the API Documentation.
- Fleaker is now open source!
```

The format of the date is very important. For most cases, just look at what's
already done and follow suit.

After running the script it will update version numbers, download URL's in
`setup.py`, commit, create a tag, and publish to PyPI. When the script is done,
it will leave one uncommitted change for the new `-dev` version. Commit that,
and push it up along with all the new tags.

Now go home and enjoy your new release of Fleaker!
