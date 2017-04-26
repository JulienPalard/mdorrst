Improved logging for Bottle.

Use
===
In order to catch exceptions from other plugins the LoggingPlugin should be
the first plugin you install to the application.

.. code-block:: python

    import bottle
    from bottle_log import LoggingPlugin

    app = bottle.Bottle()
    app.install(LoggingPlugin(app.config))

    @app.get('/test')
    def test(logger):
        logger.warning('This is only a test')
        return {}

Configuration
=============
The plugin uses the following configuration keys:

**logging.level**

The logging level. Possible values: `debug`, `info`, `warning`, `error`, `critical`.
Defaults to `warning`.

**logging.format**

The logging format. See the python logging documentation for the format.
Defaults to "`[%(asctime)s] %(levelname)s: %(name)s: %(message)s`"

**logging.utc**

If `True`, the default, time stamps are in UTC.

Logging
=======
The standard logger, used by the `logger` keyword, prints to stderr by default.

Exception logging
=================
This plugin also provides an exception logger ('bottle.exception'). By default
this logger does nothing, since bottle prints all exceptions to stderr, but it can be
useful if you want to log exceptions to somewhere else.
For example, logging to Logentries:

.. code-block:: python

    import bottle
    from logentries import LogentriesHandler
    from bottle_log import LoggingPlugin

    app = bottle.Bottle()
    app.install(LoggingPlugin(app.config))
    le_handler = LogentriesHandler('logentries-api-token')
    logging.getLogger('bottle.exception').addHandler(le_handler)
