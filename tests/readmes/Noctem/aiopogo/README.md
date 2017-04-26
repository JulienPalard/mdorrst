[![Build Status](https://travis-ci.org/Noctem/aiopogo.svg)](https://travis-ci.org/Noctem/aiopogo)

# aiopogo - a Pokémon API in Python
It allows automatic parsing of requests/responses by finding the correct protobuf objects over a naming convention and will return the response in a parsed Python dictionary format.

 * This is unofficial, use at your own risk!
 * No bot/farming code included!

## Feature Support
 * Python 3
 * Google/PTC auth
 * Address parsing for GPS coordinates
 * Chaining of RPC calls
 * Re-auth if ticket expired
 * Check for server side-throttling
 * Asynchronous IO
 * Advanced logging/debugging
 * Uses [POGOProtos](https://github.com/Noctem/POGOProtos)
 * All available RPC calls (see [API reference](https://docs.pogodev.org) on the wiki)

## Documentation
Documentation is available at the [pgoapi wiki](https://wiki.pogodev.org).

## Requirements
 * Python ≥3.5
 * aiohttp
 * protobuf (≥3)
 * gpsoauth
 * pycrypt
 * cyrandom

## Contribution
Contributions are very welcome, feel free to submit a pull request.

## Credits
[Mila432](https://github.com/Mila432/Pokemon_Go_API) for the login secrets  
[elliottcarlson](https://github.com/elliottcarlson) for the Google Auth PR  
[AeonLucid](https://github.com/AeonLucid/POGOProtos) for improved protos  
[tejado](https://github.com/tejado/pgoapi) for the original project
[pogodev](https://github.com/pogodevorg/pgoapi) for keeping it alive
