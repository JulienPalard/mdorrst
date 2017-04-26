# django-makeconf

Make config files from Django settings variables and templates.

## Installation

From your Django app, install the module from pip:

	pip install django-makeconf
	
Then make sure it's included in your `INSTALLED_APPS` section:

	INSTALLED_APPS = (
		...
	    'makeconf',
	)

## Templates

Create templates in the `templates/` directory of your app. For example, if you create `myapp/templates/makeconf/Dockerfile.tmpl`, you can generate `Dockerfile` in the root of your app by configuring `MAKECONF_MAP` in your settings file:

	MAKECONF_MAP = {
		'Dockerfile': 'makeconf/Dockerfile.tmpl',
	}
	
This relies on Django's template finder, which is pretty flexible. It will scan all your apps for a template with the same path name. The `Dockerfile` will be generated using the `Dockerfile.tmpl`, and it will have access to the `settings` variable. 

## Elastic Beanstalk Modules

Elastic Beanstalk configuration files can be declared using `MAKECONF_EB_MODULES`. Templates named `<module_name>.tmpl` can be referenced in a list by the module name. If you had a `newrelic` module and a `postgres` module that each configure your server with packages, files, etc., you can automatically turn the following format:

    MAKECONF_EB_MODULES = ['postgres', 'newrelic']

Into additional `MAKECONF_MAP` entries like so:

    MAKECONF_MAP = {
        ...
        '.ebextensions/01_postgres.config': 'postgres.tmpl',
        '.ebextensions/02_newrelic.config': 'newrelic.tmpl',
    }

If `MAKECONF_EB_MODULES` is set, `.ebextensions` will be erased with each build.

## Options

Currently, there is one option which can be set using `MAKECONF_OPTIONS`:

* `executable_extensions` - Files with extensions in this list will be created executable. Defaults to `['.sh']`.

## Usage

Assuming you have a `TIER` variable defined as `'qa'` in your settings file and the following template,

	FROM amazon/aws-eb-python:3.4.2-onbuild-3.5.1
	
	ADD uwsgi-start.sh /
	
	ENV DJANGO_SETTINGS_MODULE config.settings.{{ settings.TIER }}
	
	EXPOSE 8080

you could run

	python manage.py makeconf
	
and `{{ settings.TIER }}` would be replaced with `qa` in the output file.

## Template Tags

* `environ` - The `environ` tag is used to get required variables from the shell environment:
 	* To use it, first, load the `makeconf` template tags in your template:

	    	{% load makeconf %}

	* Then, use the tag in that template:

			{{'MY_ENVIRONMENT_VARIABLE'|environ}}

## Shared Templates

If people use this, I could see shareable formats published for different services and needs. I'm currently using it to build Elastic Beanstalk and Docker configurations based on my Django settings, so I may end up publishing Django apps with names like `django-makeconf-elasticbeanstalk-configure-proxy`, or `django-makeconf-eb-docker-settings-module`, which would simply contain templates in their `templates/` directories (plus a `setup.py` and a `MANIFEST.in` that included the template files). You'd be able to pip install those templates and use them directly in your `MAKECONF_MAP`.

Also, I'm totally open to contributions in that vein or pull requests / issues on this project.
