# Requestests

This is an testing/validation extension on top of the ever-so-popular [requests library](https://github.com/kennethreitz/requests). The library relies on duck typing to add testability of a response object. Given that, leveraging the validation mechanism in `requestests` is both lightweight and simple!

## Installation

The library can be installed via:

	pip install requestests
	
## Usage

Using the built-in validations in `requestests` is intended to be an extremely intuitive extension of using `requests`:

	>>> import requestestests
	>>> r = requestests.get('https://api.github.com/user', auth=('user', 'pass'))
	>>> r.validate_code(requests.code.ok)
	>>> r.validate_header_like('Content-Type', 'application/json')
	>>> r.encoding
	'utf-8'
	>>> r.text
	u'{"type":"User"...'
	>>> r.json()
	{u'disk_usage': 368627, u'private_gists': 484, ...}
	
What is happening is that the assertion operation is being abstracted out. The traditional method of asserting on the response:

	r = requests.get('https://api.github.com/user')
	assert r.status_code == requests.codes.ok, "Expecting a 200 response code"
	
can be simplified to this:
	
	r = requestests.get('https://api.github.com.user')
	r.validate_code(requests.code.ok)
	
	## Or even to this
	r = requestests.get('https://api.github.com.user').validate_code(requests.code.ok)
	
Validations follow the builder paradigm, so operations can be chained together:

	entity = requestests.get('https://api.github.com.user') \
				.validate_code(requests.code.ok) \
				.validate_header_like('Content-Type', 'application/json') \
				.json()

What happens in this scenario is that if any of the validations fails, an `AssertionError` is raised; otherwise, at the end of this requests, you would have:

1. Validated that the request was successful
2. Validated the 'Content-Type' is 'application/json'
3. and deserialized the response.text


## Documentation

The projects homepage can be found [here](https://github.com/jauntvrpeter/requestests).

## Supported Operations on a Response

### json\_decode(self, serializable\_class):

Provides a convenience method to Response to deserialize directly into a specific Object type of choice. Behind the scenes, this is using jsonstruct for decoding.

    :param serializable_class
    :return instance of serializable_class


### validate\_code(self, code):

Validates response code

    :param code: The expected response code
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    :raises: AssertionError, if the response.code != code
    
### validate\_not\_code(self, code):

Validates response code

    :param code: The not expected response code
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    :raises: AssertionError, if the response.code == code

### validate\_codes(self, codes=[]):

Validates response codes

    :param codes: A list of expected response codes
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    :raises: AssertionError, if none of the response.code were returned. At least 1 must match

### validate\_not\_codes(self, codes=[]):

Validates response codes not returned

    :param codes: A list of unexpected response codes
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    :raises: AssertionError, if one of the response.code were returned.

### validate\_header\_eq(self, header, value):

Validates header equals

    :param header: The header to check
    :param value: The value that you expect the header to be
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    :raises: AssertionError, if header does not match

### validate\_header\_like(self, header, value):

Validates header using regular expression

    :param header: The header to check
    :param value: The value that you expect the header to be
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    :raises: AssertionError, if header does not match

### validate\_content(self, value):

Validates content body using regular expression

    :param value: The value that you expect the body to be/have
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    :raises: AssertionError, if body does not match

### validate\_entity\_eq(self, value):

Validates content body

    :param value: The value that you expect the body to be. This should be an instance of a deserializable entity
                    (a.k.a. representational entity)
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    :raises: AssertionError, if objects do not match
    
### ttlb(self, ttlb=None):
 
    :param ttlb: The time-to-last-byte for the given request. If you don't specify anything, it simply returns the value
    :return: Returns the value of time-to-last-byte

_Example:_

	> response = requestests.get("http://www.google.com") \
	    .validate_code(requestests.codes.ok)
	> print response.ttlb
	0.426213979721
	> print response.request_url
	http://www.google.com

### request\_url(self, url=None):

    :param url: The request URL. If you don't specify anything, it simply returns the value
    :return: Returns the value of the request URL

_Example:_

	> response = requestests.get("http://www.google.com") \
	    .validate_code(requestests.codes.ok)
	> print response.ttlb
	0.426213979721
	> print response.request_url
	http://www.google.com

# Contributing to Requestests
 
* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet.
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it.
* Fork the project.
* Start a feature/bugfix branch.
* Commit and push until you are happy with your contribution.
* Make sure to add tests for it. This is important so I don't break it in a future version unintentionally.
* Please try not to mess with the version or history. If you want to have your own version, or is otherwise necessary, that is fine, but please isolate to its own commit so that I can cherry-pick around it.

## Testing and Releasing

### 1. Uprev the version in requestests/__init__.py

You'll need to uprev the `__version__` attribute in `requestests/__init__.py`:

	...
	
	__title__ = 'requestests'
	__version__ = '1.0.0'
	__build__ = 0x021000
	__author__ = 'Peter Salas'
	__license__ = 'Apache 2.0'
	
	...
	
Commit and push your changes to Github!

### 2. Upload your package to PyPI Test

Run:

	make publish.test
	
You should get no errors, and should also now be able to see your library in the test PyPI repository.

### 3. Upload to PyPI Live

Once you've successfully uploaded to PyPI Test, publish your changes to Live:

	make publish

# References

A huge shoutout to Peter Downs for his very easy-to-follow instructions for submitting a Python package to the community. See [first time with pypi](http://peterdowns.com/posts/first-time-with-pypi.html) for his instructions.

## Package Dependencies:

* [requests](https://github.com/kennethreitz/requests) - Requests is the only Non-GMO HTTP library for Python, safe for human consumption
* [jsonstruct](https://github.com/initialxy/jsonstruct) - jsonstruct is a library for two way conversion of typed Python object and JSON

# Copyright

Copyright (c) 2016 Peter Salas. See LICENSE for
further details.
