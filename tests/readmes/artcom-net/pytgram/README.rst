=======
PyTGram
=======

PyTGram is python library to create Telegram Bot based on Twisted.

----------
Installing
----------

~~~~~~~~~~~~~~
Prerequisites:
~~~~~~~~~~~~~~

- Python 3.x

You may need to install additional packages, depending on your operating system:

- Debian/Ubuntu:

.. code::

        $ sudo apt-get install python3-dev libffi-dev libssl-dev

- RHEL/CentOS (for python 3.6):

.. code::

        $ sudo yum install python36u-devel openssl-devel
        $ sudo yum group install "Development Tools"

- FreeBSD:

.. code::

        $ pkg install ca_root_nss

- Windows:

    - `VS Build Tools <http://landinghub.visualstudio.com/visual-cpp-build-tools>`_

    - `Windows Extension for Python <https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/>`_

You can install pytgram using pip:

.. code::

    $ pip install pytgram

-----
Usage
-----

~~~~~~~~~~~~~
Webhook setup
~~~~~~~~~~~~~

.. code-block:: python

    from pytgram import set_webhook

    set_webhook('bot_token', 'https://example.com')

If you use self-signed certificate - the pass path to it:

.. code-block:: python

    from pytgram import set_webhook

    set_webhook('bot_token', 'https://example.com', 'path/to/cert.pem')

~~~~~~~~~~~~~~~~~~~~~
Creating a simple bot
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import sys

    from twisted.python import log
    from twisted.internet import reactor, ssl
    from twisted.internet.defer import inlineCallbacks

    from pytgram import TelegramBot, MessageHandler, web_hook

    bot = TelegramBot('bot_token')


    @MessageHandler(content=['text'])
    @inlineCallbacks
    def text_handler(message):
        result = yield bot.send_message(chat_id=message.chat.id,
                                        text=message.text[::-1])
        print(result)


    @MessageHandler(command=['start'])
    @inlineCallbacks
    def start_handler(message):
        result = yield bot.send_message(chat_id=message.chat.id,
                                        text='Received command "start"')
        print(result)


    def main():
        log.startLogging(sys.stdout)
        ssl_context = ssl.DefaultOpenSSLContextFactory('ssl/secret.key',
                                                       'ssl/cert.pem')
        # If want use reverse proxy, then replace listenSSL on listenTCP.
        reactor.listenSSL(443, web_hook(bot.token), ssl_context)
        reactor.run


    if __name__ == '__main__':
        main()

If you want to use polling mode, you can do it like that:

.. code-block:: python

    import sys

    from twisted.python import log
    from twisted.web.server import Site
    from twisted.web.resource import Resource
    from twisted.internet import reactor
    from twisted.internet.defer import inlineCallbacks

    from pytgram import TelegramBot, MessageHandler, polling

    bot = TelegramBot('bot_token')


    @MessageHandler(content=['text'])
    @inlineCallbacks
    def text_handler(message):
        result = yield bot.send_message(chat_id=message.chat.id,
                                        text=message.text[::-1])
        print(result)


    @MessageHandler(command=['start'])
    @inlineCallbacks
    def start_handler(message):
        result = yield bot.send_message(chat_id=message.chat.id,
                                        text='Received command "start"')
        print(result)


    def main():
        log.startLogging(sys.stdout)
        reactor.listenTCP(8080,  Site(Resource()))
        polling(bot, interval=10)
        reactor.run


    if __name__ == '__main__':
        main()

