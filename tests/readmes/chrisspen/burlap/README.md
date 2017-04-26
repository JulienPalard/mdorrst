Burlap - configuration management designed for simplicity and speed
===================================================================

[![](https://img.shields.io/pypi/v/burlap.svg)](https://pypi.python.org/pypi/burlap) [![Build Status](https://img.shields.io/travis/chrisspen/burlap.svg?branch=master)](https://travis-ci.org/chrisspen/burlap) [![](https://pyup.io/repos/github/chrisspen/burlap/shield.svg)](https://pyup.io/repos/github/chrisspen/burlap)

Overview
--------

Burlap is a [configuration management](https://en.wikipedia.org/wiki/Comparison_of_open-source_configuration_management_software)
tool and framework for deploying software to servers.

It's written in Python and is built ontop of [Fabric](http://www.fabfile.org/) to run commands remotely over SSH.

Unlike [Chef](https://www.chef.io/) or [Ansible](http://www.ansible.com/) that target large "web-scale" platforms at the expense of great complexity, Burlap targets small to medium-scale platforms and keeps its configuration simple.

Much of the code is also heavily influenced by [Fabtools](https://github.com/fabtools/fabtools), another Fabric-based toolkit.

Installation
------------

Install the package via pip with:

    pip install burlap

[Click here for full documentation](http://chrisspen.github.io/burlap/).
