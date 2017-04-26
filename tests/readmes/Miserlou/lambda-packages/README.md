![Logo](http://i.imgur.com/AlmKP2q.png)

# lambda-packages
[![Build Status](https://travis-ci.org/Miserlou/lambda-packages.svg)](https://travis-ci.org/Miserlou/lambda-packages)
[![PyPI](https://img.shields.io/pypi/v/lambda-packages.svg)](https://pypi.python.org/pypi/lambda-packages)
[![Slack](https://img.shields.io/badge/chat-slack-ff69b4.svg)](https://slack.zappa.io)

Various popular libraries, pre-compiled to be compatible with AWS Lambda.

Currently includes support for:

* bcrypt
* cffi
* cryptography
* datrie_extended 
* LXML
* misaka
* MySQL-Python
* numpy
* OpenCV
* Pillow (PIL)
* psycopg2
* PyCrypto
* PyNaCl
* pyproj
* python-ldap
* python-Levenshtein
* regex

This project is intended for use by [Zappa](https://github.com/Miserlou/Zappa), but could also be used by any Python/Lambda project.

## Installation

    pip install lambda-packages

## Usage

The best way to use these packages is with [Zappa](https://github.com/Miserlou/Zappa), which will automatically install the right packages during deployment, and do a million other useful things. Whatever you're currently trying to do on Lambda, it'll be way easier for you if you just use Zappa right now. Trust me. It's awesome. As a bonus, Zappa now also provides support for [manylinux wheels](https://blog.zappa.io/posts/zappa-adds-support-for-manylinux-wheels), which adds support for hundreds of other packages.

But, if you want to use this project the other (wrong) way, just put the contents of the .tar.gz archive into your lambda .zip.

**lambda-packages** also includes a manifest with information about the included packages and the paths to their binaries.

```python
from lambda_packages import lambda_packages

print lambda_packages['psycopg2']['version']
# 2.6.1
print lambda_packages['psycopg2']['path']
# /home/YourUsername/.venvs/lambda_packages/psycopg2/psycopg2-2.6.1.tar.gz
```

## Contributing

To add support for more packages, send a pull request containing a gzipped tarball of the package (build on Amazon Linux and tested on AWS Lambda) in the appropriate directory, an updated manifest, and deterministic build instructions for creating the archive.

You may find the [build.sh script](https://github.com/Miserlou/lambda-packages/blob/master/lambda_packages/cryptography/build.sh) useful as a starting point.

Useful targets include:

* MongoEngine
* pandas
* scipy
* [scikit-learn](https://serverlesscode.com/post/deploy-scikitlearn-on-lamba/)

## Support / Development / Training / Consulting

Do you need help with..

  * Porting existing Python applications to AWS Lambda?
  * Building new applications and services that scale infinitely?
  * Reducing your operations and hosting costs?
  * Training your team to use AWS and other server-less paradigms?

Good news! We're currently available for remote and on-site consulting for small, large and enterprise teams. Please contact <miserlou@gmail.com> with your needs and let's work together!

<br />
<p align="center">
  <a href="https://gun.io"><img src="http://i.imgur.com/M7wJipR.png" alt="Made by Gun.io"/></a>
</p>
