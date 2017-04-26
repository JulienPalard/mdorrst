kotti_controlpanel
*******************

Add a settings configuration to your Kotti site. |build status|_

.. |build status| image:: https://img.shields.io/travis/b4oshany/kotti_controlpanel/production.svg?style=flat-square
.. _build status: http://travis-ci.org/b4oshany/kotti_controlpanel

`Find out more about Kotti`_


You have a full example e.g. in the addon kotti_google_analytics_.

Setup
=====

To activate the ``kotti_controlpanel`` add-on in your Kotti site, you need to
add an entry to the ``kotti.configurators`` setting in your Paste
Deploy config.  If you don't have a ``kotti.configurators`` option,
add one.  The line in your ``[app:main]`` (or ``[app:kotti]``, depending on how
you setup Fanstatic) section could then look like this::

    kotti.configurators = kotti_controlpanel.kotti_configure

The add-on adds a new configuration page to save settings for your module or
across different modules. It adds a new submenupoint named "Settings" to the
menupoint "Site Setup". Every setting collection is presented in one tab. It
is intended to use one tab for a module, but it is also possible to use
multiple tabs if you have the need for a more extended structure.

You can choose between two modes to set up your settings. With the "dict mode"
you have a very easy and straightforward option to set up the settings. If you
need more advanced forms you can set up an own schema.

A setting tab is set up with with a dictionary. Here you define a name and a
title for your tab, what are required. Optional arguments are success_message,
either settings or schema, schema_factory and use_csrf_token.

Define your settings in a dictionary::

    TestSettings = {
        'name': 'test_settings',
        'title': "Testsettings",
        'icon': 'myaddon:static/icon.png',
        'description': "Some description for my settings",
        'success_message': u"Successfully saved test settings.",
        'settings': [
            {'type': 'String',
             'name': 'testsetting_1',
             'title': 'Test 1',
             'description': 'a test setting',
             'default': '', },
            {'type': 'Integer',
             'name': 'testsetting_2',
             'title': 'Test 2',
             'description': 'again a test setting',
             'default': 23, }]}

Define your settings with a schema::

    class StringSchemaNode(colander.SchemaNode):
        name = 'a_string'
        title = 'hello'
        default = 'hello world'

    class RangedIntSchemaNode(colander.SchemaNode):
        name = 'range_int'
        validator = colander.Range(0, 10)
        default = 5
        title = 'Ranged Int'

    class TestSchema(colander.MappingSchema):
        string = StringSchemaNode(colander.String())
        ranged_int = RangedIntSchemaNode(colander.Int())

    TestSettings = {
        'name': 'test_settings',
        'title': "Testsettings",
        'description': "Some description for my settings",
        'success_message': u"Successfully saved test settings.",
        'schema_factory': TestSchema
    }


To get your configuration registered within ``kotti_controlpanel`` add the
settings in a populator in your add-on. Have a look to the Kotti documentation
to get more informations for populators_ and to see an example_.


Add your settings configuration within a populator, e.g. in a file named populate.py::

    def populate():
        from kotti_controlpanel.util import add_settings
        add_settings(TestSettings)

and add this to your configuration::

    def kotti_configure(settings):
        settings['kotti.populators'] += ' my_addon.populate.populate'

or directly to your ini file::

    kotti.populators = my_addon.populate.populate


To get your setting back into your code you use the following::

    from kotti_controlpanel.util import get_setting

    first_test_setting = get_setting('test_setting_1')


You can also add useful links to the main Control panel view by::

    from kotti.util import Link
    from kotti_controlpanel import CONTROL_PANEL_LINKS

    def kotti_configure(settings):
        CONTROL_PANEL_LINKS.append(Link('setup-users', title='User Management'))


Events
------

Before and after the settings are saved events for handling the changes are fired. To subscribe
to the events use something like::

    from pyramid.events import subscriber
    from kotti_controlpanel.events import SettingsAfterSave

    @subscriber(SettingsAfterSave)
    def do_something_when_settings_saved(event):
        # Check if the settings for this module was saved.
        if not event.module == __package__:
            return
        my_fancy_thing()

Default schemas
---------------

``kotti_controlpanel`` provides some default schemas that you can use directly in your code and for
example purposes. Currently there are two schemas implemented, one to choose in what slot the
widget should be shown and another one to set the visibility of the widget. To use it in your
addon place something like the following in your populator::

    from kotti.views.slots import assign_slot
    from kotti_controlpanel.config import SlotSchemaNode
    from kotti_controlpanel.config import ShowInContextSchemaNode
    from kotti_controlpanel.util import add_settings
    from kotti_controlpanel.util import get_setting
    from kotti_myaddon import _

    class MyWidgetSchema(colander.MappingSchema):
        slot = SlotSchemaNode(colander.String())
        show_in_context = ShowInContextSchemaNode(colander.String())

    MyAddonSettings = {
        'name': 'myaddon_settings',
        'title': _(u'My Addon Settings'),
        'description': _(u"Settings for my addon"),
        'success_message': _(u"Successfully saved my addon settings."),
        'schema_factory': MyAddonSchema,
    }

    def populate():
        add_settings(MyAddonSettings)

Note
-----

This package was insipred by `kotti_settings`_ package

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _populators: http://kotti.readthedocs.org/en/latest/developing/configuration.html#kotti-populators
.. _example: http://kotti.readthedocs.org/en/latest/developing/frontpage-different-template.html
.. _kotti_google_analytics: https://pypi.python.org/pypi/kotti_google_analytics
.. _kotti_settings: https://pypi.python.org/pypi/kotti_settings
