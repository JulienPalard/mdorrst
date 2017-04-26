=====
Template Preview
=====

Template Preview is a simple Django app to preview Django-rendered templates within a browser.
For example, if you send emails from Django, this is a quick and easy way to see your changes,
without needing to constantly be sending yourself emails.

Quick start
-----------

1. Add "template_preview" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'template_preview',
    ]

2. Include the template_preview URLconf in your project urls.py like this::

    url(r'^template_preview/', include('template_preview.urls')),

    Note: you might to only register this app/urls when DEBUG is set to True

3. Start the development server and visit http://127.0.0.1:8000/template_preview/
    to view a list of your registered templates

4. Click on a template name to view a form containing all of your template variables

5. Provide any values you'd like to see in the rendered template.

6. Click "Render" and your rendered template will appear in a modal.
