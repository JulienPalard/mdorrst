=============================================
Python minimalist SDK to use Isogeo REST API
=============================================

.. image:: https://badge.fury.io/py/isogeo-pysdk.svg
    :target: https://badge.fury.io/py/isogeo-pysdk
.. image:: https://img.shields.io/badge/python-2.7-blue.svg
    :target: https://badge.fury.io/py/isogeo-pysdk
.. image:: https://img.shields.io/badge/python-3.5-blue.svg
    :target: https://badge.fury.io/py/isogeo-pysdk
.. image:: https://travis-ci.org/Guts/isogeo-api-py-minsdk.svg?branch=master
    :target: https://travis-ci.org/Guts/isogeo-api-py-minsdk
    :alt: Travis build status

Unofficial lib.
API keys are required to use it.

Getting API keys
================

`Send us your request by email <mailto:projects+api@isogeo.com>`_.

Getting Help
============

There is a basic documentation about the  `Isogeo API <https://docs.google.com/document/d/11dayY1FH1NETn6mn9Pt2y3n8ywVUD0DoKbCi9ct9ZRo/edit?usp=sharing>`_.

Installing
==========

To use:

.. code-block:: shell

    pip install --user isogeo-pysdk

For developers:

.. code-block:: shell

    git clone git@github.com:Guts/isogeo-api-py-minsdk.git
    cd isogeo-api-py-minsdk
    python setup.py install

Quickstart
==========

.. code-block:: python

    from isogeo_pysdk import Isogeo

    # authentify the application
    isogeo = Isogeo(client_id=app_id,
                    client_secret=app_secret)

    # get available subresources
    print(isogeo.SUBRESOURCES)

    # get the token
    token = isogeo.connect()

    # search within catalogs shared to the application
    search = isogeo.search(token)

    print("Search __dict__ keys: ", search.keys())
    print("Search query parameters: ", search.get('query'))
    print("Total count of metadatas shared: ", search.get("total"))
    print("Count of resources got by request: {}\n".format(len(search.get("results"))))

Others samples are available in `the source repository <https://github.com/Guts/isogeo-api-py-minsdk/tree/master/isogeo_pysdk/samples>`_.


Isogeo API coverage
===================

Authentication
---------------

- [X] group application (oAuth2 Credentials Grant)
- [ ] user confidential application (oAuth2 Authorization Code Grant)
- [ ] user public application (oAuth2 Implicit Grant)
- [X] token auto refresh

Resources search ( GET /resources/search )
-------------------------------------------

Resources search parameters:

- [X] q (query)
- [X] ob (order by)
- [X] od (order direction)
- [X] _id (filter on specific resources id list)
- [X] _include (subresources management)
- [X] _lang (French or English with complete translation)
- [X] _limit (results length)
- [X] _offset (pagination)
- [X] box (filter on WGS84 boundging box)
- [X] geo (filter on WKT polygon)
- [X] rel (geometric operation to apply on 2 previous filters)
- [X] s share segregation


Resource details ( GET /resources/{rid} )
----------------------------------------

Resource detailed parameters:

- [X] id (metadata UUID)
- [X] _include (subresources management)

Others:

- [X] download resource in XML ISO-1939 version
- [ ] resource with contacts subresource included ( GET /resources/{rid}/contacts )
- [ ] resource with events subresource included ( GET /resources/{rid}/events )
- [ ] resource with keywords subresource included ( GET /resources/{rid}/keywords )
- [ ] resource with operations subresource included ( GET /resources/{rid}/operationds - only for services)

Keyword details ( GET /keyword/{kid} )
---------------------------------------

- [X] kid (keyword UUID)
- [X] _include (subresources management)
- [X] searches for keywords in a specific workgroup ( GET /groups/{gid}/keywords/search  )

These requests are not publicly available.

Thesaurus ( GET /thesauri )
----------------------------------

- [X] list of available thesauri
- [X] specific thesaurus ( GET /thesauri/tid )
- [X] searches for keywords in a specific thesaurus ( GET /thesauri/{tid}/keywords/search )

Shares  ( GET /shares )
----------------------------------------------

- [X] list accessible shares
- [X] specific share ( GET /shares/sid )

Miscellaneous & bonus
----------------------

- [X] check API version
- [X] check database version
- [X] pick between different Isogeo API platform (PROD, QA, [INT])
- [X] set protocol requests to HTTPS (default) or HTTP (only for GET requests not for authentication)
- [X] get every API label automatically translated (not only INSPIRE themes)
- [X] additional search parameter to automatically get full results without have to iterate with _limit and _offset
- [X] option (`ALL`) to quickly get every subresources through _include parameter
- [X] method to easily download Isogeo hosted data
- [-] handle proxies setting (only for basic auth - not PAC nor NTLM)
