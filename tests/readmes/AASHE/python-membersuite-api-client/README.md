[![Build Status](https://travis-ci.org/AASHE/python-membersuite-api-client.svg?branch=master)](https://travis-ci.org/AASHE/python-membersuite-api-client) [![Coverage Status](https://coveralls.io/repos/github/AASHE/python-membersuite-api-client/badge.svg?branch=master)](https://coveralls.io/github/AASHE/python-membersuite-api-client?branch=master) [![Issue Count](https://codeclimate.com/github/AASHE/python-membersuite-api-client/badges/issue_count.svg)](https://codeclimate.com/github/AASHE/python-membersuite-api-client/issues) [![Requirements Status](https://requires.io/github/AASHE/python-membersuite-api-client/requirements.svg?branch=master)](https://requires.io/github/AASHE/python-membersuite-api-client/requirements/?branch=master)

# python-membersuite-api-client
A python interface to the MemberSuite API

## Installation

Install as you would any other package. Add to your requirements.txt:

    https://github.com/AASHE/python-membersuite-api-client/archive/master.zip

(to be updated when this package is added to PyPi)

## MemberSuite Configuration

In your MemberSuite account, you will need to create a dedicated API console
user. Ensure that API access is enabled for your MemberSuite account, and
also check the box for "API User" for this new user account.

Create a keypair for this user via the console and save the credentials
generated somewhere secure (they cannot be retrieved later if lost)


## Usage

    from membersuite_api_client.client import ConciergeClient

    client = ConciergeClient(
        access_key=MS_ACCESS_KEY,
        secret_key=MS_SECRET_KEY,
        association_id=MS_ASSOCIATION_ID)

To authenticate and receive a session ID:

    client.request_session()
    print client.session_id

To take advantage of a service, for example `subscriptions`:

    ORG_ID = #####
    service = SubscriptionService(self.client)
    subscription_list = service.get_subscriptions(org_id=ORG_ID)

## Running tests

To run all tests:

    $ nosetests

To run specific tests, load them by module. For example:

    $ python -m membersuite_api_client.tests.test_subscriptions

## Contributing and Extending

Looking to contribute? The best place to start is in the code base. Notice how
we created modules for each MemberSuite object, like `organizations`.

Each module contains `services.py` and `models.py` files.

Your "models" are simply python representations of the MemberSuite objects.

Your "services" provide interfaces to those models in MemberSuite. This is
where objects are retrieved from MemberSuite and converted to your models for
use in a python app. It is recommended that the services be classes and if
you define `result_to_models` and `ms_object_to_model` methods on the class
you can use the ChunkQueryMixin to make large queries.

### Nuance

This can now be used to make additional calls using the methods included in
the WSDL from MemberSuite. For documentation on available methods and their
usage, see http://api.docs.membersuite.com/

Use request_session() as a model for constructing the headers for
your own functions in your app that follow this method:

    1) Call client.construct_concierge_header(url) to generate a new header element, using your method's URL as an argument.
    2) Call client.service.method_name(_soapheaders=[concierge_request_header], method arguments)
    3) Return any relevant data out of the response object

***IMPORTANT NOTE: In constructing headers, SessionId must appear first.***
