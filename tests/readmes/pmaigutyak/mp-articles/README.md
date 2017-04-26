# MP-Articles

Django articles app.

### Installation

Install with pip:

```sh
$ pip install django-mp-articles
```

Add articles to urls.py:

```
urlpatterns += i18n_patterns(
    url(r'^articles/', include('articles.urls', namespace='articles')),
)
```

Add articles to settings.py:
```
INSTALLED_APPS = [
    'articles',
]

# Default: ('news', _('News')),
ARTICLE_TYPE_CHOICES = (
    ('example', _('Example')),
    ('example2', _('Example 2')),
)

# Default: None
DEFAULT_ARTICLE_TYPE = 'example'
```

Run migrations:
```
$ python manage.py migrate
```

### Template tags

To get latest articles in template you should load 'articles' tags and add 'get_latest_articles' template tag into your template. 
Examples:

```
{% load articles %}

{% get_latest_articles article_type='example' %}

{% get_latest_articles article_type='example' count=3 %}

{% get_latest_articles article_type='example' as latest_articles %}
```

### Requirements

App require this packages:

* django-modeltranslation
* django-pure-pagination
* django-ckeditor
