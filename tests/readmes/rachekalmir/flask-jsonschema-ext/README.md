# Flask-JSONSchema-Ext
Flask JSONSchema Extended Library

This library can be used to apply a JSONSchema (http://json-schema.org/) to a Flask API end-point that is generated on the fly from your database entities.

Currently supported drivers are:

* SQLAlchemy

## Installation

Use pip or easy_install:

`pip install flask-jsonschema-ext`

Flask-JSONSchema-Ext follows [semantic versioning](http://semver.org/).

## Testing

The tests are in the tests/ and examples/ folders.
To run the tests use the `py.test` testing tool:

`pytest`

## Basic Usage

First create some SQLAlchemy models:

```python
# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    post_value = Column(String)
    author_name = Column(String)
```

Next create a basic Flask app and annotate the flask endpoint with the `@jsonschema_generate` decorator:

```python
# app.py

from flask import Flask

from flask_jsonschema_ext import FlaskJsonSchemaExt, jsonschema_generate
from flask_jsonschema_ext.drivers import SqlAlchemyDriver

from .models import Post

app = Flask(__name__)
jsonschema = FlaskJsonSchemaExt(app, SqlAlchemyDriver)

@app.route('/post', methods=['POST', 'PUT'])
@jsonschema_generate(Post)
def post_root():
    return ""

if __name__ == '__main__':
    app.run()
```

Now, all posts and puts to `/post` will only accept json that matches the schema defined by the `Post` class. 

## Including and Excluding fields (and relationships)

Including and excluding fields can be done at a global level by specifying `__jsonschema_include__` or `__jsonschema_exclude__` on the SQLAlchemy class:

```python
class Post(Base):
    __tablename__ = 'post'
    __jsonschema_exclude__ = ['author_name']
    post_id = Column(Integer, primary_key=True)
    post_value = Column(String)
    author_name = Column(String)
```

This exclude definition will remove `author_name` from the resulting schema and thus any incoming requests containing it will be rejected by the flask endpoint.

Include can be specified in a similar fashion; just remember that include will run before exclude as it is more explicit and it is therefore incorrect to specify both of them on the same class.  I.e. specifying include will already have limited the class to only those included fields thereby making any exclude definition meaningless.

## Customising the schema per endpoint

You can also customise the schema at a local level by specifying a custom parse tree on an endpoint:

```python
@app.route('/post', methods=['POST', 'PUT'])
@jsonschema_generate(Post, parse_tree={__jsonschema_include__: ['post_value', 'author_name']})
def post_root():
    return ""
```

This will override the definition as specified on the class itself as the schema generator will now first check the specified definition and then check the class definition. 

## Development

We would love to hear what you think about flask-jsonschema-ext on our [issues](https://github.com/rachekalmir/flask-jsonschema-ext/issues) page.

## Changelog

#### Version 0.2.0

Released on 

- Added Local File Driver

#### Version 0.1.2

Released on 2017-04-12

- Migrated jsonschema decorator to support non-generated schemas
- Added colanderalchemy example

#### Version 0.1.1

Released on 2017-03-04

- Created CHANGELOG
- Added caching options to decorator
