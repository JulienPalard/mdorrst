# MP-Config

This app helps to save custom site settings in admin and use them in views or templates.
Supported field types:

* CharField
* TextField
* IntegerField
* FloatField
* BooleanField
* UrlField
* EmailField
* FileField
* ImageField

### Installation

Install with pip:

```sh
$ pip install django-mp-config
```

Add config to settings.py:
```
INSTALLED_APPS = [
    'site_config',
]
```

Run migrations:
```
$ python manage.py migrate
```

### Usage
```
>>> from site_config import config
>>> print config.my_var
```

### Template tags

To get config in template you should load 'site_config' tags and add 'get_site_config' template tag into your template. 
Examples:

```
{% load site_config %}

{% get_site_config as config %}

{{ config.my_var }}
```

### Requirements

App require this packages:

* django-modeltranslation
