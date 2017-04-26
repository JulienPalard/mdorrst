MongoNorm
=========

`中文文档 <README_cn.rst>`_

**MongoNorm** is Not a Object Relational Mapping library for mongodb.


MongoNorm just packages document Mongo's as an object. you can add custom
methods and properties for it, And you can still use it as dict.

MongoNorm based on pymongo. The class and methos which is not be mentioned
is same as pymongo's, please refer to pymongo's documentation first.

installation
------------
Use pip to install::
    
    pip install MongoNorm

use guide
---------

1. MongoClient and Database

Use these just like you use in pymongo::

    from mongonorm import MongoClient
    client = MongoClient()
    # Or: client = MongoClient('mongodb://localhost:27017/')
    db = client.test_database

2. Define your own Model

MongoNorm changed the way collections and documents were used,
first you need to define your own Model::

    @db.collection('articles')
    Class Article(object):
        """Article
        
        documents struct: {
            "title": "article title",
            "author": "author",
            "content": ""
        }
        """
        def __init__(self, title, author, content):
            self.insert({
                'title': title,
                'author': author,
                'content': content})
        
        def html_content(self):
            parse_html(self['content'])

*!Warning about __init__():*
    Don't add attribute in :``__init__``. You can defind property in Model if
    you need.

    You must call ``insert(document)`` in or after ``__init__`` to upload
    document to Mongodb.


All the pymongo on the collection of operations,
have become the Model of the classmethod,
If the pymongo's return is the document, will be monogonorm package
for your definition of the class, such as::
    
    Article.find_one ({'title': 'Hello'}) # return an object of Article or None
    cur = Article.find ({})
    # Return a cursor, you can get Article object from this cusor

    for article in cur:
        print(article['title'])  # use as dict
        print(article.html_content())  # use method of model class

3. some useful methods:

* shortcut for set a single field as a dict::

    article['title'] = 'MongoNorm'
    # it will auto update to mongodb

* shortcut for update self::

    article.update({'$set': {'title', 'MongoNorm', 'author': 'Crows'}})
