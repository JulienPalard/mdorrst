Cloudmesh Rest
==============

Prerequistis
-------------

* mongo instalation
* eve instalation
* cloudmesh cmd5
* cloudmesh rest

Install Mongo on OSX
^^^^^^^^^^^^^^^^^^^^

::

   brew update
   brew install mongodb

   # brew install mongodb --with-openssl

Install Mongo on OSX
^^^^^^^^^^^^^^^^^^^^

ASSIGNMET TO STUDENTS, PROVIDE PULL REQUEST WITH INSTRUCTIONS

Introduction
------------

With the cloudmesh REST framework it is easy to create REST services while defining the resources in
the service easily with examples. The service is based on eve and the examples are defined in yml to be
converted to json and from json with evegenie into a valid eve settings file.

Thus oyou can eother wite your examples in yaml or in json. The resources are individually specified in a
directory. The directory can contain multiple resource files. We recomment that for each resource you
define your own file. Conversion of the specifications can be achieved with the `schema` command.


Yaml Specification
------------------

Let us first introduce you to a yaml specification. Let us assume that your yaml file is called
`profile.yaml` and located in a directory called `example`::

  profile:
    description: The Profile of a user
    email: laszewski@gmail.com
    firstname: Gregor
    lastname: von Laszewski
    username: gregor

As eve takes json objects as default we need to convert it first to json.
This is achieved wih::

  cd example
  cms schema convert profile.yml profile.json

This will provide the json file `profile.json` as Listed in the next section

Json Specification
------------------

A valid json resource specification looks like this::

  {
    "profile": {
      "description": "The Profile of a user",
      "email": "laszewski@gmail.com",
      "firstname": "Gregor",
      "lastname": "von Laszewski",
      "username": "gregor"
    }
  }


Conversion to Eve Settings
--------------------------

The json files in the ~/sample directory need now to be converted
to a valid eve schema. This is achieved with tow commands. First,
we must concatenate all json specified resource examples into a
single json file. We do this with::

  cms schema cat . all.json

As we assume you are in the samples directory, we use a . for the current
location of the directory that containes the samples. Next, we need to convert it
to the settings file. THis can be achieved with the convert program when you
specify a json file::

  cms schema convert all.json

THe result will be a eve configuration file that you can use to start an
eve service. The file is called all.settings.py


Managing Mongo
^^^^^^^^^^^^^^

Next you need to start the mongo service with

::

    cms admin mongo start

You can look at the status and information about the service with ::

    cms admin mongo info
    cms admin mongo status

If you need to stop the service you can use::

    cms admin mongo stop

Manageing Eve
^^^^^^^^^^^^^

Now it is time to start the REST service. THis is done in a separate window with the following commands::

  cms admin settings all.settings.json
  cms admin rest start

The first command coppies the settings file to

  ~/cloudmesh/eve/settings.py

This file is than used by the start action to start the eve service.
Please make sure that you execute this command in a separate window, as
for debugging purposses you will be able to monitor this way interactions
with this service

Testing - OLD
^^^^^^^
::

  make setup    # install mongo and eve
  make install  # installs the code and integrates it into cmd5
  make deploy
  make test

