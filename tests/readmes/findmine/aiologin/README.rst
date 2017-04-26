========
Aiologin
========

This module provides extension to the `aiohttp_session <http://aiohttp-session.
readthedocs.io/en/latest>`_ and `aiohttp.web <https://aiohttp.readthedocs.io/en/
latest/web.html>`_ projects by extending their functionality with this login
management tool. The style of this login management module was greatly inspired
by the flask-login module.

Disclaimer
----------
This module expects that you have a working understanding of the aiohttp and
aiohttp_session modules. Links to the tutorials for those are:
http://aiohttp.readthedocs.io/en/stable/ . Additionally, this module uses
aiohttp.test_utils which is currently only available in the latest version of
aiohttp.

Installation
------------
To install this module just use pip3 with the following command

.. code:: Python

    sudo pip3 install aiologin

Getting Started
---------------
The first thing you are going to want to do is create your user class which is
needed to store your user session's information. The User class should
minimally look like this:

.. code:: Python

    import aiologin

    class User(aiologin.AbstractUser):
        def __init__(self, email, password):
            print("user class made")
            self.email = email
            self.password = password

        @property
        def authenticated(self):
            return True

        @property
        def forbidden(self):
            return False

*Note:* The User class should inherit from aiologin.AbstractUser
and define its authenticated and forbidden properties inside the user class. If
these conditions are not met the module with throw Exceptions.

Further Setup, Creating Your Handlers and Authentication Methods 
----------------------------------------------------------------
Once your User class has been created you should construct the authentication
methods that your server will use to handle the routes you will add later. See
the sample below for some examples of authentication methods. At the very least
you should create two handlers one for a Login route and one for a Logout route.

.. code:: Python

    from aiohttp import web

    @aiologin.secured
    async def handler(request):
        return web.Response(text="OK")

    async def login(request):
        # remember is false you should add your own functionality
        await request.aiologin.authenticate(remember=False)
        return web.Response(text="logged in")


    async def logout(request):
        await request.aiologin.logout()
        return web.Response(text="logged out")

Additionally, you should define the auth_by_form, auth_by_header, and
auth_by_session methods, that will be passed into the aiologin class. These
methods should return a User object as a sign of success or None as failure.

.. code:: Python

    from urllib.parse import parse_qs

    async def auth_by_header(request, key):
        if key == '1234567890':
            return User('user@sample.com', 'blueberry')
        return None


    async def auth_by_session(request, profile):
        email, password = profile.get('email', None), profile.get('password', None)
        if email == 'user@sample.com' and password == 'blueberry':
            return User(profile['email'], profile['password'])
        return None


    async def auth_by_form(request):
        args = parse_qs(request.query_string)
        email, password = args.get('email', [''])[0], args.get('password', [''])[0]
        if email == 'user@sample.com' and password == 'blueberry':
            return User(email, password)
        return None

Furthermore, whatever handlers you want to be secured should have the
`@aiologin.secured` decorator before it. This will create a wrapper for your
handler which will be responsible for protecting the handle from unauthenticated
access.

More Setup, Creating Your Web App and Adding Routes To It
---------------------------------------------------------
Now you need to create your web app that will contain your routes as well as
your middleware that you can add at your own discretion. What you will
definitely need to add is the session_middleware with the SimpleCookieStorage
class passed in. See the example below

.. code:: Python

        from aiohttp_session import session_middleware, SimpleCookieStorage

        app = web.Application(middlewares=[
            session_middleware(SimpleCookieStorage())
        ])
        
Once you defined your web app, add it to the aiologin class via it's setup
method, as well as pointers to your auth_by_header and auth_by_session methods.
See the example below

.. code:: Python

        aiologin.setup(
            app=app,
            auth_by_form=auth_by_form,
            auth_by_header=auth_by_header,
            auth_by_session=auth_by_session
        )

One last step before starting your server is to add your routes. For that all
you need to do is manually add your routes with their respective handler
methods.
        

Last Steps, Creating and Starting Your Event Loop
-------------------------------------------------
Once everything is set up, we create our async server via an async method that
will create and run our server for as long as we need. the code for that looks
as follows:

.. code:: Python

    import asyncio

    app.router.add_route('GET', '/', handler)
    app.router.add_route('GET', '/login', login)
    app.router.add_route('GET', '/logout', logout)

    async def init(loop,app):
        return await loop.create_server(app.make_handler(), '0.0.0.0', 8080)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop,app))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

Signals
-------
For logging purposes or any kind of event driven automation a convenient signals
interface is provided. In order to register callback functions with the events
follow the code sample below. Begin by defining some callback functions.

.. code:: Python

    @asyncio.coroutine
    def func1(request):
        print("login")


    @asyncio.coroutine
    def func2(request):
        print("handler")


    @asyncio.coroutine
    def func3(request):
        print("authenticated")


    @asyncio.coroutine
    def func4(request):
        print("forbidden")


    @asyncio.coroutine
    def func5(request):
        print("unauthorized")

Once the functions have been defined, you may register these functions during
the aiologin setup initialization as follows

.. code:: Python

    aiologin.setup(
        app=app,
        auth_by_form=auth_by_form,
        auth_by_header=auth_by_header,
        auth_by_session=auth_by_session,
        signals=[
            (aiologin.ON_LOGIN, func1),
            (aiologin.ON_LOGOUT, func2),
            (aiologin.ON_AUTHENTICATED, func3),
            (aiologin.ON_FORBIDDEN, func4),
            (aiologin.ON_UNAUTHORIZED, func5)
        ]
    )


License
-------

MIT License
