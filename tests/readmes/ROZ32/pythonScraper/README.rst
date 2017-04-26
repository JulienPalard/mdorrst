Python Scraper
==============

A simple web scraper made in python with love:

Install with pip:
-----------------

.. code:: sh

    pip install simplescraper


Usage:
-----------------

Make a simple call to a web page, lets call 'www.test.com'

.. code:: python

    from simplescraper import SimpleScraper

    test = SimpleScraper()
    result = test.get_scraped_data('www.test.com')
    print result

output:
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: javascript

    {
        url: 'http://www.test.com', 
        source: 'www.test.com', 
        image: 'http://www.test.com/some/random/image.png',
        title: 'Just a test page'
    }

You can also call it without using the 'www' as 'test.com' if the web page has a redirection. If the web page needs the usage of the https protocol to be accessed you can call it as: 'https://www.test.com', this is not mandatory since the scraper checks if the protocol is needed.

Get iframe:
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    result = test.get_scraped_data('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
output:
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: javascript

    {
        description: 'Rick Astley - Never Gonna Give You Up (Official Music Video) - Listen On Spotify: http://smarturl.it/AstleySpotify Download Rick\'s Number 1 album "50" - http...', 
        title: 'Rick Astley - Never Gonna Give You Up', 
        url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 
        image: 'https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg', 
        source: 'www.youtube.com', 
        iframe: '<iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" height="720" width="1280"></iframe>'
    }
This is on `GitHub <https://github.com/ROZ32/pythonScraper>`__ so let me
know if I've broked it somewhere.

Stuff used to make this:
~~~~~~~~~~~~~~~~~~~~~~~~

-  `beautifulsoup4 <https://github.com/getanewsletter/BeautifulSoup4>`__
   for Markdown language parsing
-  `html5lib <https://github.com/html5lib/html5lib-python>`__ for the
   awesome html5 parser
