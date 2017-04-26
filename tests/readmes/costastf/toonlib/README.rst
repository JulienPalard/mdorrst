=======
toonlib
=======

A library to interact with Eneco's toon.

Main information is cached for 5 minutes before reaching out to the api for
freshness. Assigning values to either the thermostat or the thermostat state effectively changing the temperature clears the cache so the next call will get fresh info about the
settings.

Most returned information is currently modeled as a named tuple
since they need no intelligence. The smartplugs and lights are proper objects
since they need to call the api and refresh their values. Everything else will evolve according to it's needs.

The library exposes the data that toon uses to graph its consumption both as
flow data (hourly consumption for the day) and graph data (yearly, monthly,
weekly, daily, hourly) consumption.


* Documentation: http://toonlib.readthedocs.io/en/latest/

Features
--------

* Reads values for gas, electric, temperature.
* Identifies connected hue lights and fibaro smartplugs
* Can read and set temperature and thermostat state
* Can turn lights or plugs on, off or toggle their state
* Can get consumption values from fibaro plugs
* More ...

TODO
____

* Change the caching library to a name spaced one.
* Fine tune the caching sanely across all required objects
* Properly implement caching for flow and graph data information
