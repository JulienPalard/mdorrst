# geo_code

[![Build Status](https://travis-ci.org/jwilber/geo-code.svg?branch=master)](https://travis-ci.org/jwilber/geo-code)

Lightweight Python package for geocoding addresses using the Google Geocoding API.

There are multiple geocoding modules in Python. What makes **geo_code** different from the others is that if offers the following functionalities:

- ***Batch-geocoding***: Given an input csv file name (and column to geocode), `Geocoder.geocode_csv()` will return a csv file of the geocoded locations.

- ***String Removal***: Address columns are often dirty, so **geo_code** allows you to input a string (or Python list of strings) to remove from a given query.

- **Delayed Geocoding**: The Google Geocoding API free tier service has a request limit of ___. **geo_code** allows you to use the free tier service and will automatically wait 30 minutes when a query limit is reached. It also provides functionality to save intermediate progress.


For an input string address, `Geocoder` will return the longitude, latitude, postcode, formatted_address, and query status; e.g.: 

`{'status': u'OK', 'postcode': u'55441', 'latitude': 44.9850985, 'longitude': -93.4207907 'formatted_address': u'11100-11298 Sunset Trail, Plymouth, MN 55441, USA'}`

***

# Getting Started: Using the Geocoder Class

The core functionality provided by **geo_code**, geocoding, is provided by the `geocode` method of the `Geocoder` class. 
The `Geocoder` class can be initialized with an API-key (provided at [here](https://console.developers.google.com/apis/)), or without an argument (for free-tier service/rates).

```Python
from geo_code import Geocoder

# init with free tier service
g = Geocoder()

# init with API-key
g = Geocoder('thisIsNotARealAPIKey')
```

To geocode an Address, simply input the address as a string into the `Geocoder.geocode` method.

```Python
# input string as argument
address = '190 Doe Library, Berkeley CA'
g.geocode(address)

# another example: input raw string
g.geocode('1600 Pennsylvania Ave NW, Washington, DC 20500')
```