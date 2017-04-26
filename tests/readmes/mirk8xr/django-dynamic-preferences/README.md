# What is dynamic-preferences-plus ?

Dynamic-preferences-plus is a Django app designed to manage your project settings. While most of the time,
a `settings.py` file is sufficient, there are some situations where you need something more flexible,
such as per-user settings and per-site settings.

For per-user settings, you could actually store them in `UserProfile`. However, it means that every time you want to add a new setting, you need to add a new column to the `UserProfile` DB table. Not very efficient.

Dynamic-preferences-plus allow you to register settings (a.k.a. preferences) in a declarative way, for users,
sites and your whole project. Preferences values are serialized before storage in database,
and automatically deserialized when you want to access them.

With dynamic-preferences-plus, you can update settings on the fly, through django's admin or custom forms, without restarting your application.

Links:

- [Project page](https://github.com/mirk8xr/django-dynamic-preferences)
- [PyPi package](https://pypi.python.org/pypi/django-dynamic-preferences-plus)

# License

The project is licensed under BSD license.