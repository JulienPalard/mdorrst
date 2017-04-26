# Django CBTP e-mail #

[![Travis CI Badge](https://api.travis-ci.org/illagrenan/django-cbtp-email.png)](https://travis-ci.org/illagrenan/django-cbtp-email)
&nbsp;
[![Coverage Status](https://coveralls.io/repos/illagrenan/django-cbtp-email/badge.svg?branch=master&service=github)](https://coveralls.io/github/illagrenan/django-cbtp-email?branch=master)
&nbsp;
[![Requirements Status](https://requires.io/github/illagrenan/django-cbtp-email/requirements.svg?branch=master)](https://requires.io/github/illagrenan/django-cbtp-email/requirements/?branch=master)

```bash
CBTP
│ │└──Premailer (CSSs ares inlined)
│ └───Template
└─────Class-based (optional)
```

## Installation ##

**Install this package using pip:**

```bash
pip install --upgrade django-cbtp-email
```

Supported Python versions are: `2.7`, `3.4`, `3.5` and `3.6`.


**Add `django_cbtp_email` to `INSTALLED_APPS`:**
```python
INSTALLED_APPS = (
    'django_cbtp_email',
)
```

## Usage ##

Create custom mailer (e.g. in `your_app/mailers.py`):

```python
from django_cbtp_email.mailer import Mailer

class TestMailer(Mailer):
    template = "test_mail" # .html is added by default
    subject = "Subject of test mail"
    to = ["nobody@localhost"] # or override method get_recipients()
    context = {
        "title": "Hello world"
    }

test_mailer = TestMailer()
text_mailer.attach_file("path/to/file_to_attach.PDF")
text_mailer.to.append("john@localhost")
test_mailer.send_message()
```

Create e-mail template (e.g. in `your_app/templates/mail/test_email.html`):

```html+django
{% extends "email_base.html" %}

{% block content %}
    <h1>{{ title }}</h1>

    <p class="first">
        Lorem ipsum...
    </p>

    <footer>
        &copy; 2015 ACME
    </footer>
{% endblock %}
```

Content of `email_base.html`:

```html+django
{% load mailing_tags %}

<!doctype html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Test mail</title>

    <style>
		/* This will be inlined */
        h1 {
            color: red;
        }
    </style>

    {# This will be also inlined #}
	{% css_direct "css/my_css.css" %}
</head>
<body>
{% block content %}{% endblock %}
</body>
</html>
```

You can specify type of rendered template by:

```python
DEFAULT_TEMPLATE_TYPE = "html" # or "txt"
```


## License ##

The MIT License (MIT)

Copyright (c) 2015–2017 Vašek Dohnal (@illagrenan)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
