StrictYAML
==========

StrictYAML is a `type-safe <https://en.wikipedia.org/wiki/Type_safety>`_ YAML parser
built atop `ruamel.yaml <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-is-strictyaml-built-on-ruamelyaml>`_ that parses a
`restricted subset <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#what-features-does-strictyaml-remove>`_
of the YAML specificaton.

Priorities:

* Readability of YAML.
* Ease of use of API.
* Secure by default.
* Strict validation of markup and straightforward type casting.
* Clear, human readable exceptions with line numbers.
* Acting as a drop in replacement for pyyaml, ruamel.yaml or poyo.
* Roundtripping.
* Letting you worry about more interesting things than parsing config files.

Simple example:

.. code-block:: yaml

  # All about the character
  name: Ford Prefect
  age: 42
  possessions:
    - Towel

Default parse result:

.. code-block:: python

   >>> strictyaml.load(yaml)
   YAML({'possessions': ['Towel'], 'age': '42', 'name': 'Ford Prefect'})

   >>> strictyaml.load(yaml).data
   {"name": "Ford Prefect", "age": "42", "possessions": ["Towel", ]}   # All data is str, list or dict

Using a schema:

.. code-block:: python

   >>> from strictyaml import load, Map, Str, Int, Seq
   >>> person = load(yaml, Map({"name": Str(), "age": Int(), "possessions": Seq(Str())})) \
   >>> person.data == {"name": "Ford Prefect", "age": 42, "possessions": ["Towel", ]}     # 42 is now an int


Once parsed you can change values and roundtrip the whole YAML, with comments preserved:

.. code-block:: python

   >>> person['age'] = 43
   >>> print(person.as_yaml())
   # All about the character
   name: Ford Prefect
   age: 43
   possessions:
     - Towel

As well as look up line numbers:

.. code-block:: python

   >>> person['possessions'][0].start_line
   5


Install It
----------

.. code-block:: sh

  $ pip install strictyaml



FAQ
---

From learning programmers:

* `What is YAML? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#what-is-yaml>`_
* `Why should I care about YAML? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-should-i-care-about-yaml>`_
* `When should I use a validator and when should I not? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#when-should-i-use-a-validator-and-when-should-i-not>`_

If you're looking at this and thinking "why not do/use X instead?" that's a healthy response, and you deserve answers. These are probably the questions you're asking:


* `Why should I use strictyaml instead of ordinary YAML? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-should-i-use-strictyaml-instead-of-ordinary-YAML>`_
* `What features does StrictYAML remove? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#what-features-does-strictyaml-remove>`_
* `Why not use JSON for configuration or DSLs? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-not-use-json-for-configuration-or-dsls>`_
* `Why not use INI files for configuration or DSLs? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-not-use-ini-files-for-configuration-or-dsls>`_
* `Why shouldn't I just use python for configuration? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-shouldnt-i-just-use-python-for-configuration>`_
* `Why not use XML for configuration or DSLs? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-not-use-xml-for-configuration-or-dsls>`_
* `Why not use TOML? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-not-use-toml>`_
* `Why not use HJSON? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-not-use-hjson>`_
* `Why not use JSON5? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-not-use-json5>`_
* `Why not use pykwalify to validate YAML instead? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#why-not-use-pykwalify-to-validate-yaml-instead>`_
* `What if I still disagree with everything you wrote here? <https://github.com/crdoconnor/strictyaml/blob/master/FAQ.rst#what-if-i-still-disagree-with-everything-you-wrote-here>`_


Map Patterns
------------

If you're not sure what the key name is going to be in a map but you know what type the keys and values will be, use "MapPattern".

.. code-block:: yaml

  emails:
    arthur: arthur@earth.gov
    zaphod: zaphod@beeblebrox.com
    ford: ford@megadodo-publications.com

.. code-block:: python

   >>> from strictyaml import load, Map, MapPattern, Str
   >>> load(yaml, Map({"emails": MapPattern({Str(), Str()})}) \
     == {"emails": {"arthur": "arthur@earth.gov", "zaphod": "zaphod@beeblebrox.com", "ford": "ford@megadodo-publications.com"}}


Optional values
---------------

If you want to use a mapping with a number of *required* keys and a number of *optional* keys use "Optional":

.. code-block:: yaml

  arthur:
    email: arthur@earth.gov
  zaphod:
    email: zaphod@beeblebrox.com
    job: President of the Galaxy
  ford:
    email: ford@ursa-minor.com
    job: Freelance "journalist"


This would be parsed like so:

.. code-block:: python

   >>> from strictyaml import load, MapPattern, Map, Str, Optional
   >>> load(yaml, MapPattern(Str(), Map({"email": Str(), Optional("job"): Str()}))) \
     == {
            "arthur": {'email': 'arthur@earth.gov',},
            "zaphod": {'email': 'zaphod@beeblebrox.com', 'job': 'President of the Galaxy'},
            "ford": {'email': 'ford@ursa-minor.com', 'job': 'Freelance "journalist"'},
        }


Either/Or
---------

If, for example, you want to parse something as a list of strings *or* an individual string, you can
use a pipe operator to distinguish between them - like so: |

.. code-block:: yaml

  zaphod:
    email: zaphod@beeblebrox.com
    victims: Good taste
  ford:
    email: ford@ursa-minor.com
    victims: Journalistic integrity
  arthur:
    email: arthur@earth.gov
    victims:
      - A bowl of petunias
      - Agrajag
      - A sperm whale

This would be parsed like so:

.. code-block:: python

   >>> from strictyaml import load, Seq, Map, Str, Optional
   >>> load(yaml, MapPattern(Str(), Map({"email": Str(), "victims": Str() | Seq(Str())}))) \
     == {
            "zaphod": {'email': 'zaphod@beeblebrox.com', 'victims': 'President of the Galaxy'},
            "arthur": {'email': 'arthur@earth.gov', 'victims': 'Journalistic integrity'},
            "ford": {'email': 'ford@ursa-minor.com', 'victims': ['A bowl of petunias', 'Agrajag', 'A sperm whale', ]},
        }

Numbers
-------

StrictYAML will parse a string into integers, floating point or decimal (non-floating point) numbers if you specify it:

.. code-block:: python

  >>> import from strictyaml import load, Map
  >>> load("int: 42", Map({"int": strictyaml.Int()})) == {"int": 42}
  >>> load("float: 42.3333", Map({"float": strictyaml.Float()})) == {"float": 42.3333}
  >>> load("price: 35.42811", Map({"price": strictyaml.Decimal()})) == {"price": decimal.Decimal('35.42811')}

Booleans
--------

Upper case or lower case - it doesn't matter. Yes, on and true are treated as True and no, off and false are treated as False.

.. code-block:: python

  >>> load("booltrue: yes", Map({"booltrue": strictyaml.Bool()})) == {"booltrue": True}
  >>> load("boolfalse: no", Map({"boolfalse": strictyaml.Bool()})) == {"booltrue": True}
  >>> load("booltrue: true", Map({"booltrue": strictyaml.Bool()})) == {"booltrue": True}
  >>> load("boolfalse: False", Map({"boolfalse": strictyaml.Bool()})) == {"booltrue": False}

Empty values
------------

Empty values can be be validated and returned as None, {} and []:

.. code-block:: python

  >>> load("empty: ", Map({"empty": strictyaml.EmptyNone()})) == {"empty": None}
  >>> load("empty: ", Map({"empty": strictyaml.EmptyDict()})) == {"empty": {}}
  >>> load("empty: ", Map({"empty": strictyaml.EmptyList()})) == {"empty": []}

Enums
-----

.. code-block:: python

  >>> load("day: monday", Map({"day": strictyaml.Enum(["monday", "tuesday", "wednesday"])})) == {"day": "monday"}



Datetimes
---------

This datetime parser uses dateutil's datetime parser, which is used, among others, by arrow, delorean and pendulum.


.. code-block:: python

  >>> load("date: 2016-10-22T14:23:12+00:00", Map({"date": strictyaml.Datetime()})) == {"date": datetime(2016, 10, 22, 14, 23, 12)}


Comma Separated Values
----------------------

Scalar strings can be parsed a second time into comma separated values.

.. code-block:: python

  >>> load("a: 1, 2, 3", Map({"a": strictyaml.CommaSepaeated(strictyaml.Int())})) == {"a": [1, 2, 3, ]}


Custom scalar types
-------------------

COMING SOON


Kwalify Validation
------------------

COMING SOON


Changelog
---------

0.5: Data is now parsed by default as a YAML object instead of directly to dict/list. To get dict/list as before, get yaml_object.data.


Contributors
------------

* @gvx
* @AlexandreDecan
* @lots0logs
