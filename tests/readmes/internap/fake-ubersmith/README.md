[![Build Status](https://travis-ci.org/internap/fake-ubersmith.svg?branch=master)](https://travis-ci.org/internap/fake-ubersmith)

Fake-ubersmith
=============
This library is a web server representing a fake Übersmith where you can register api calls and response that can be used
for integration test purposes.

# Command line usage
```
pip install fake-ubersmith
fake-ubersmith
```

# Docker usage
```
docker pull internap/fake-ubersmith:latest
docker run -d -p 8000:9131 internap/fake-ubersmith
```

# License

fake-ubersmith is distributed under [Apache License Version 2.0](LICENSE).

# Contributing

Feel free to raise issues and send some pull request, we'll be happy to look at them!
