
## Jawaf ##

[![Build Status](https://travis-ci.org/danpozmanter/jawaf.svg?branch=master)](https://travis-ci.org/danpozmanter/jawaf)
[![Documentation](https://readthedocs.org/projects/jawaf/badge/?version=latest)](http://jawaf.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/jawaf.svg)](https://pypi.python.org/pypi/jawaf/)
[![PyPI Version](https://img.shields.io/pypi/pyversions/jawaf.svg)](https://pypi.python.org/pypi/jawaf/)

**Jawaf asynchronous web application framework**

A fast asynchronous web application framework.

Read the [documentation](http://jawaf.readthedocs.io) to get started.

Inspired by (and using some code/concepts from) [Django](https://www.djangoproject.com/) and the promise of [Sanic](https://github.com/channelcat/sanic).

The goal of this project is to provide much of what Django provides (convenience, smart scaffolding, ease of development) on top an async python 3 core.

**Built Using**

***Core***

[Python 3](https://www.python.org/) (Version 3.6+ Required)

[Sanic](https://github.com/channelcat/sanic)

***Data***

[SQLAlchemy Core](http://docs.sqlalchemy.org/en/latest/core/)

[PostgreSQL](https://www.postgresql.org/)

[asyncpg](https://github.com/MagicStack/asyncpg)

[ascynpgsa](https://github.com/CanopyTax/asyncpgsa)

***Session***

[sanic_session](https://github.com/subyraman/sanic_session)

[asyncio_redis](https://github.com/jonathanslenders/asyncio-redis)

[Redis](https://redis.io/)

***Tests***

[py.test](http://doc.pytest.org/en/latest/)

**Features**

* Built on an async stack (Sanic) to run fast and scale.
* Database interaction via SQLAlchemy Core
* Sessions via sanic_session and Redis
* Unit testing via py.test
* Django style management commands
* Django style project/app scaffolding
* Extensible using structured python packages as apps
* CSRF protection baked in
* Interactive shell (using ipython or bpython if either are detected)
* User Authentication, Groups & Permissions built in
* Optional Admin API

Note: Many of the software requirements are in beta, alpha, or even pre-alpha status.
You'd be well advised to have a long hard think about using this in production.

Given the early status of this project it is subject to potential backwards-incompatible changes.

Jawaf is provided "at your own risk".
