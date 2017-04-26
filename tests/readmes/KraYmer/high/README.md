[![nopypi travis](https://travis-ci.org/Kraymer/high.svg?branch=master)](https://travis-ci.org/Kraymer/high)
[![pypi](http://img.shields.io/pypi/v/high.svg)](https://pypi.python.org/pypi/high)
[![nopypi rss](https://img.shields.io/badge/rss-subscribe-orange.svg)](https://github.com/Kraymer/hiGH/releases.atom)

# hiGH

*Hi GitHubers!* Extract mail addresses of a repo stargazers/collaborators, etc

<img src="https://raw.githubusercontent.com/Kraymer/high/master/docs/_static/supportcat.png" width="400">

## Usage

~~~
Usage: high.py [OPTIONS] REPO_NAME

  Extract mails from stargazers, collaborators and people involved with issues of given repository.

Options:
  -l, --login TEXT    Github.com login.
  -b, --with-blog     When user has no email, print blog instead when
                      available.
  --as-list           Print addresses as a comma separated list, as used in
                      emails 'To:'' field.
  -r, --role [s|c|i]  Classes of users to consider: s (stargazers), c
                      (collaborators), i (issues participants). DEFAULT: all.
  --version           Show the version and exit.
  -h, --help          Show this message and exit.
~~~

## Install

`high` is written for [Python 3](https://www.python.org/downloads/).

Install with [pip](https://pip.pypa.io/en/stable/) via
`pip3 install high` command.

If you're on Windows and don't have pip yet, follow [this
guide](https://pip.pypa.io/en/latest/installing/) to install it.
