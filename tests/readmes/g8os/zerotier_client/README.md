# zerotier_client
client to zerotier network generated by [go-raml](https://github.com/Jumpscale/go-raml)

## Guides

### spec.json
Is zerotier API specification from https://my.zerotier.com/api/spec with some fixes:
- GET /network/{id}/member response type
- add POST /network to creates new network

### api.raml

RAML file converted from spec.json using https://app.stoplight.io

## example.py

An example on how to use the library. It does these things:

- print network status
- get array of networks and print the name of first network in the array
- reverse the name of the first network above
- get the first network above by it's ID and print it's name
- creates new network with name = 'my new network'

## generates.sh

Script to generate this client library
