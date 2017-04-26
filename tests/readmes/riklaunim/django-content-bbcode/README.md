django-content-bbcode
=====================

BBCode alike parser for Django applications.

This application is based on tag parser I use on my rk.edu.pl sites. It's very similar to BBCode although it's designed
to support more advanced tags giving more complex output. My usage examples:

* put a link to article by given slug (depending if the article is a category or a page different styles may apply)
* highlight code block in articles
* insert a thumbnail of image given by relative path from media (with optional alt text, size, headline etc.)

```
[rk:syntax lang="bash"]
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
[/rk:syntax]
```

Or:

```
[rk:art slug="some-article-slug"]
```

So it's BBCode that calls some Python code, Django ORM even and returns dynamic output.


How to use it
-------------
* You can install it from pypi:
```
pip install django-content-bbcode
```

* Add 'content_bbcode' to INSTALLED_APPS
* You will get 'parse_content_bbcode' templatetag you can use in your templates on text which should have tags parsed:
```
{% load parse_content_bbcode %}
{{ article.text|parse_content_bbcode|safe }}
```

In code usage
-------------

You can also manually parse tags:
```
parser = cbcparser.ContentBBCodeParser()
result = parser.parse_tags(some_text)
```

Setup and usage
-------------
You will have to define parsers for tags you will want to use. The application will look for **tags.py** files in every
application from INSTALLED_APPS. In that file it will look for **registered_tags** dictionary.

Example: https://github.com/riklaunim/django-content-bbcode/blob/master/content_bbcode_demo/demo_application/tags.py

* Dictionary key is the tag *name* like *rk:art* would have *art* as name.
* Dictionary value would be a callable, usually a function taking two arguments: list of dictionaries and text

* The text is the text in which we replace the tags
* The list of dictionaries is a list of all occurrences of given tag


The dictionary from the occurrences list has few keys:
* tag: the tag we need to replace
* attributes: all key-value attributes given to the tag
* code: will be only for double tags (those with opening and closing tag)

```
[rk:mytag]code[/rk:mytag]
```


In general you would iter over the list and replace every tag with something.

In the the end the callable should return modified text.

If you want to place tags.py in different location, then you can define ``CONTENT_BBCODE_SCAN_MODULES`` as a dictionary of 'app_name': 'module_location'.

To change the default tag prefix from ``rk`` set ``CONTENT_BBCODE_PREFIX`` in your settings.py


Running tests
-------------
Tests are in the content_bbcode_demo.demo_application. Clone the repo and run:

```
pip install -r demo_requirements.txt
```

Direct test run:

```
python manage.py test content_bbcode_demo
```

Testing on Python 2.7 and 3.6 with tox:

```
tox
```

Project status
--------------
At the moment the code is just after pulling it out of my site code. It still needs some refactors/cleanups and quite likely regexp improvements,
but it works, at least it should :)

I'll try to post, commit somewhere some real tags, like the pygments syntax highlighting and so on.

You can check the issues page for current ToDo list. I'm also interested in your feedback, suggestions and pull requests :)


Credits
-------
* tags loader was inspired by https://github.com/pozytywnie/django-javascript-settings configuration loader
