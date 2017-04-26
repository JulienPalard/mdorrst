# Welcome to Fcmd
[![Version][version-badge]][version-link] ![Supported-python-version][python27-badge] [![Build Status][travis-badge]][travis-link]  [![Coverage][coverage-badge]][coverage-link] ![Star][stars] ![Fork][forks] [![MIT License][license-badge]](LICENSE.md)

## Introduction

Freg is a pure Python library designed to show the information about what you specify on [FREESWITCH](https://freeswitch.org/).
In [/scripts](https://github.com/sudaning/Freg/tree/master/scripts) , there are some scripts written by me for daily use.

## Installation
1. Via **pip**  
```pip install Fcmd```  
2. Via **easy_install**  
```easy_install pyFcmd```  
3. From **source**(recommend)   
```python setup.py install```  

## upgrading
1. Via **pip**  
```pip install --upgrade pyFcmd```

## Examples
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from fcmd import RegUser

if __name__ == '__main__':

	from optparse import OptionParser
	usage = "usage: \n\tpython %prog [options]" + \
		"\nFor example: " + \
		"\n\tpython %prog -s 192.168.0.2 -u root -p root -n 075536384596"
	parser = OptionParser(usage=usage, version="%prog V1.0")
	parser.add_option('-s', '--host', dest='host', default='114.119.11.59',help="SSH IP. default:'%default'")
	parser.add_option('-u', '--user', dest='user', default='root', help="SSH port. default:'%default'")
	parser.add_option('-p', '--password', dest='password', default='root', help="SSH password. default:'%default'")

	parser.add_option('-f', '--profile', dest='profile', default="sipp", help="profile. default:'%default'")
	parser.add_option('-n', '--num', dest='num', default='', help="number. default:'%default'")
	parser.add_option('-c', '--cmd', dest='cmd', default='', help="command. default:'%default'")

	(options, args) = parser.parse_args() 

	if options.cmd:
		with Cmd(debug=True) as c:
			c.login(host=options.host, user=options.user, password=options.password)
			c.run(cmd=options.cmd)
			c.show()
	else:
		with RegUser(debug=True) as reguser:
			reguser.login(host=options.host, user=options.user, password=options.password)
			reguser.run(profile=options.profile, number=options.num)
			reguser.show()
```

## From the author
**Welcome to use Fcmd (●'◡'●)ﾉ♥**  
If you find any bug, please report it to me by opening a issue.
Fcmd needs to be improved, your contribution will be welcomed.


[version-badge]:   https://img.shields.io/pypi/v/pyFcmd.svg?label=pypi
[version-link]:    https://pypi.python.org/pypi/pyFcmd/
[python27-badge]:  https://img.shields.io/badge/python-2.7-green.svg
[stars]:           https://img.shields.io/github/stars/sudaning/Fcmd.svg
[forks]:           https://img.shields.io/github/forks/sudaning/Fcmd.svg
[travis-badge]:    https://img.shields.io/travis/sudaning/Fcmd.svg
[travis-link]:     https://travis-ci.org/sudaning/Fcmd
[coverage-badge]:  https://img.shields.io/coveralls/sudaning/Fcmd.svg
[coverage-link]:   https://coveralls.io/github/sudaning/Fcmd
[license-badge]:   https://img.shields.io/badge/license-MIT-007EC7.svg

