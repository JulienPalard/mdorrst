GTFSTK
********
.. image:: https://travis-ci.org/araichev/gtfstk.svg?branch=master
    :target: https://travis-ci.org/araichev/gtfstk
    
GTFSTK is a Python 3.4+ tool kit that analyzes `General Transit Feed Specification (GTFS) <https://en.wikipedia.org/wiki/GTFS>`_ data in memory without a database.
It uses Pandas and Shapely to do the heavy lifting.


Installation
=============
Create a Python 3.4+ virtual environment and ``pip install gtfstk``.


Examples
========
You can play with ``ipynb/examples.ipynb`` in a Jupyter notebook


Documentation
=============
Documentation is in ``docs/`` and also on RawGit `here <https://rawgit.com/araichev/gtfstk/master/docs/_build/singlehtml/index.html>`_.


Notes
=====
- Development status is Alpha
- This project uses `semantic versioning <http://semver.org/>`_
- Thanks to `MRCagney <http://www.mrcagney.com/>`_ for partially funding this project
- Constructive feedback and code contributions welcome


Authors
=========
- Alex Raichev (2014-05)


History
=========

8.0.1, 2017-04-26
-------------------
- Fixed the bug where ``setup.py`` could not find the license file.


8.0.0, 2017-04-21
-----------------
- Finally knuckled down and wrote a GTFS validator: ``validators.py``.  It's basic, easy to read, and, thanks to Pandas, fast.  It checks `this 31 MB Southeast Queensland feed <http://transitfeeds.com/p/translink/21/20170310>`_ in 22 seconds on my 2.8-GHz-processor-16-GB-memory computer.  With the same computer and feed and in fast mode (``--memory_db``), `Google's GTFS validator <https://github.com/google/transitfeed>`_ takes 420 seconds. That's about 19 times slower. Part of the latter validator's slowness is its many checks beyond the GTFS, such as checks for too fast travel between every pair of stop times.
- Moved all but the most basic ``Feed`` methods into other modules grouped by theme, ``routes.py``, ``stops.py``, etc.  Eases reading and additionally exposes the methods as functions on feeds, like in the GTFSTK versions before 7.0.0.
- Speeded up ``miscellany.py::asssess_quality``
- Refactored ``constants.py``
- Renamed some functions


7.0.0, 2017-04-07
-----------------
- Rewrote most feed functions as ``Feed`` methods
- Rewrote tests for pytest
- Removed some miscellaneous functions, such as plotting functions


6.1.0, 2016-11-24
-----------------
- Changed ``feed.read_gtfs`` to unzip to temporary directory
- Enabled ``feed.write_gtfs`` to write to a directory


6.0.0, 2016-10-17
-----------------
- Improved function names, e.g. ``compute_trips_stats`` -> ``compute_trip_stats``
- Added functions to ``cleaner.py`` and changed cleaning function outputs to feed instances
- Made ``feed.copy`` a method
- Simplified Feed objects and added auto-updates to private attributes
- Changed the signatures of a few functions, e.g. ``calculator.append_dist_to_shapes`` now returns a feed instead of a shapes data frame
- Fixed formatting of properties field in ``calculator.trip_to_geojson`` and ``calculator.route_to_geojson``


5.1.1, 2016-09-01
-----------------
- Bugfix: Added ``'from_stop_id'`` and ``'to_stop_id'`` to list of string data types in ``constants.py``. Previously, they were sometimes getting interpreted as floats, which stripped leading zeros from the IDs, which then did not match the IDs in the stops data frame


5.1.0, 2016-08-31
-----------------
- Added trip ID parameter to ``calculator.get_stops``
- Created ``calculator.trip_to_geojson``
- Added whitespace stripping to ``cleaner.clean_route_short_names``


5.0.0, 2016-07-08
-----------------
- Renamed the function ``calculator.get_feed_intersecting_polygon`` to ``calculator.restrict_by_polygon``
- Added the function ``calculator.restrict_by_routes``


4.3.0, 2016-07-04
-----------------
- Added the function ``calculator.get_start_and_end_times``


4.2.0, 2016-07-04
-----------------
- Added the functions ``calculator.compute_center``, ``calculator. compute_bounds``, ``calculator.route_to_geojson``
- Extended the function ``calculator.get_stops`` to accept an optional route ID
- Extended the function ``calculator.build_geometry_by_shape`` to accept and optional set of shape IDs
- Extended the function ``calculator.build_geometry_by_stop`` to accept and optional set of stop IDs


4.1.2, 2016-07-01
------------------
- Improved distance sanity checks in ``calculator.compute_trip_stats`` and ``calculator.append_dist_to_stop_times``


4.1.1, 2016-07-01
------------------
- Bugfixed ``feed.copy`` so that the ``dist_units_in`` of the copy equals ``dist_units_out`` of the original
- Added some more distance sanity checks to ``calculator.compute_trip_stats`` and ``calculator.append_dist_to_stop_times``


4.1.0, 2016-05-23
------------------
- Improved ``cleaner.clean_route_short_names``
- Removed ``utilities.clean_series``
- Improved ``cleaner.aggregate_routes``
- Removed some unnecessary print statements


4.0.0, 2016-05-11
------------------
- Deleted an extraneous print statement in ``calculator.create_shapes``
- Added ``utilities.is_not_null``
- Changed ``calculator.shapes_to_geojson`` to return a dictionary instead of a string
- Upgraded to Pandas 0.18.1 and fixed ``calculator.downsample`` accordingly
- Added ``cleaner.aggregate_routes``


3.0.1, 2015-12-16 
------------------
- Bugfix: formatted ``parent_station`` as a string in ``constants.DTYPE``


3.0.0, 2015-12-15
------------------
- Changed signature and behavior of ``create_shapes``
- Added duplicate route short name count to ``assess``
- Changed the behavior of ``clean_route_short_names``
- Changed ``INT_COLS`` to ``INT_COLUMNS``
- Moved some functions
- Added some functions, such as a function to copy feeds


2.1, 2015-12-08
------------------
- Added more functions to ``calculator.py``, some of which are optional and depend on GeoPandas
- Documented more
- Made ``read_gtfs`` raise a more helpful error when an input path does not exist


2.0.1, 2015-11-19
--------------------
- Made Matplotlib import optional
- Updated plotter function chart colors


2.0.0, 2015-11-06
----------------
- Moved the ``Feed`` class into a separate file
- Fixed a fatal bug in ``plot_routes_time_series`` and renamed it ``plot_feed_time_series``
- Added ``route_type`` to trips stats and routes stats
- Added more functions to the ``cleaner`` module


1.0.0, 2015-11-04
--------------------
- Modularized more
- Refactored the Feed class, exporting most methods to functions
- Changed function names, favoring a ``compute_`` prefix over a ``get_`` prefix for complex functions
- Bug fix: in ``INT_COLUMNS`` changed ``'dropoff_type'`` to ``'drop_off_type'``.


0.12.3, 2015-07-18
--------------------
- Changed to return empty data frames instead of ``None`` where appropriate
- Added ``Feed.clean_route_short_names``
- Changed the inputs and outputs of ``get_stops_stats`` and ``get_stops_time_series``
- Replaced ``assert`` statements with exceptions


0.12.2, 2015-07-06
--------------------
- Changed name to ``gtfstk``


0.12.1, 2015-06-24
--------------------
- Added ``route_short_name`` and ``min_headway`` to trips stats and routes stats
- Changed the default handling of distance units in ``Feed``


0.12.0, 2015-04-21
--------------------
- Assembled ``feed.py`` and ``utils.py`` into a unified top-level package by tweaking ``__init__.py``
- Renamed ``get_linestring_by_shape`` and ``get_point_by_stop`` to ``get_geometry_by_shape`` and ``get_geometry_by_stop``, respectively


0.11.16, 2015-04-20
---------------------
- Added ``min_transfer_time`` to ``INT_COLUMNS``


0.11.15, 2015-04-14
---------------------
- Fixed ``get_route_timetable`` sort order


0.11.14, 2015-04-14
---------------------
- Added data frame empty checks to ``Feed.__init__``, because i was getting errors on feeds with empty ``calendar.txt`` files


0.11.13, 2015-04-14
---------------------
- Removed ``parent_station`` from ``INT_COLUMNS``, which should have never been there in the first place


0.11.12, 2015-04-13
---------------------
- Now you can specify the output distance units


0.11.11, 2015-04-08
---------------------
- Changed most functions to return an empty data frame instead of ``None``
- Fixed ``export`` so that integer columns, such as 'bike_allowed', that have at least on NaN value no longer get formatted as floats in the output CSVs


0.11.10, 2015-04-03
---------------------
- Reduced columns in ``get_trips_activity``
- Added ``clean_series``


0.11.9, 2015-04-03
---------------------
- Fixed a bug/typo in the computation of the ``service_distance`` and ``service_duration`` columns of feed stats


0.11.8, 2015-03-27
---------------------
- Fixed a bug in the computation of the ``peak_start_time`` and ``peak_end_time`` columns of routes stats and feed stats


0.11.7, 2015-03-27
---------------------
- Added more columns to ``get_routes_stats``
- Added ``get_feed_stats`` and ``get_feed_time_series`` and removed the similar ``agg_routes_stats`` and ``agg_routes_time_series`` 
- Removed ``dump_all_stats``, because it wasn't very useful
- Replaced ``get_busiest_date_of_first_week`` with ``get_busiest_date``


0.11.6, 2015-03-16
---------------------
- Cleaned code slightly
- Added 'speed' column in trips stats
- Added 'is_loop' column in trips stats and routes stats
- Added more tests


0.11.5, 2015-03-13
---------------------
- Added route and stop timetable methods
- Improved tests slightly
- Tidied code slightly
- Change occurrences of 'vehicle' to 'trips', because that's clearer
- Updated some packages


0.11.4, 2015-03-12
---------------------
- Changed name to gtfs-tk


0.11.3, 2015-03-02
----------------------
- Add ``get_shapes_geojson``
- Renamed ``get_active_trips`` and ``get_active_stops`` to ``get_trips`` and ``get_stops``
- Upgraded to Pandas 0.15.2


0.11.2, 2014-12-10
----------------------
- Scooped out main logic from ``Feed.get_stops_stats`` and ``Feed.get_stops_time_series`` and put it into top level functions
  for the sake of greater flexibility.  Similar to what i did for 
  ``Feed.get_routes_stats`` and ``Feed.get_routes_time_series``
- Fixed a bug in computing the last stop of each trip in ``get_trips_stats``
- Improved the accuracy of trip distances in ``get_trips_stats``
- Upgraded to Pandas 0.15.1


0.11.1, 2014-11-12
----------------------
- Added ``fill_nan_route_short_names``
- Switched back to version numbering in the style of major.minor.micro, because that seems more useful


0.11, 2014-11-10
----------------------
- Fixed a bug in ``Feed.get_routes_stats`` that modified the input data frame and therefore affected the same data frame outside of the function (dumb Pandas gotcha). Changed it to operate on a copy of the data frame instead.


0.10, 2014-11-06
----------------------
- Speeded up time series computations by at least a factor of 10
- Switched from representing dates as ``datetime.date`` objects to '%Y%m%d' strings (the GTFS way of representing dates), because that's simpler and faster. Added an export method to feed objects
- Minor tweaks to ``append_dist_to_stop_times``.


0.9, 2014-10-29
----------------------
- Scooped out main logic from ``Feed.get_routes_stats`` and ``Feed.get_routes_time_series`` and put it into top level functions for the sake of greater flexibility.  I at least need that flexibility to plug into another project. 


0.8, 2014-10-24
----------------------
- Simplified methods to accept a single date instead of a list of dates.


0.7, 2014-10-08
----------------------
- Whoops, lost track of the changes for this version.


0.6, 2014-10-08
----------------------
- Changed ``seconds_to_time`` to ``timestr_to_seconds.``.  Added ``get_busiest_date_of_first_week``. 


0.5, 2014-10-02
----------------------
- Converted headways to minutes
- Added option to change headway start and end time cutoffs in ``get_stops_stats`` and ``get_stations_stats``

0.4, 2014-10-02
---------------------
- Fixed a bug in get_trips_stats that caused a failure when a trip was missing a shape ID


0.3, 2014-09-29
----------------------
- Switched from major.minor.micro version numbering to major.minor numbering
- Added ``get_vehicle_locations``.


0.2.3, 2014-08-22
----------------------
- Added ``append_dist_to_stop_times`` and ``append_dist_to_shapes``


0.2.2, 2014-08-17
----------------------
- Changed ``get_xy_by_stop`` name and output type


0.2.1, 2014-07-22
----------------------
- Changed from period indices to timestamp indices for time series, because the latter are better supported in Pandas. 
- Upgraded to Pandas 0.14.1.


0.2.0, 2014-07-22
----------------------
- Restructured modules 


0.1.12, 2014-07-21
----------------------
- Created stats and time series aggregating functions


0.1.11, 2014-07-17
----------------------
- Added ``get_dist_from_shapes`` keyword to ``get_trips_stats`` 


0.1.10, 2014-07-17
----------------------
- Fixed some typos and cleaned up the directory


0.1.9, 2014-07-17
----------------------
- Changed ``get_routes_stats`` headway calculation
- Fixed inconsistent outputs in time series functions.


0.1.8, 2014-07-16
----------------------
- Minor tweak to ``downsample``


0.1.7, 2014-07-16
----------------------
- Improved ``get_trips_stats`` and cleaned up code


0.1.6, 2014-07-04
----------------------
- Changed time series format


0.1.5, 2014-06-23
----------------------
- Added documentation


0.1.4, 2014-06-20
----------------------
- Upgraded to Python 3.4


0.1.3, 2014-06-01
----------------------
- Created ``utils.py`` and updated Pandas to 0.14.0


0.1.2, 2014-05-26
----------------------
-Minor refactoring and tweaks to packaging


0.1.1, 2014-05-26
----------------------
- Minor tweaks to packaging


0.1.0, 2014-05-26
----------------------
- Initial version
