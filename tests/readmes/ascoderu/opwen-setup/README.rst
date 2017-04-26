Opwen setup
===========

.. image:: https://travis-ci.org/ascoderu/opwen-setup.svg?branch=master
    :target: https://travis-ci.org/ascoderu/opwen-setup

What's this?
------------

This repository contains scripts to set up:

* The Opwen Lokole `web-application <https://github.com/ascoderu/opwen-webapp>`_
* The Opwen `cloud-server <https://github.com/ascoderu/opwen-cloudserver>`_

.. code:: bash

    # download the script
    wget --no-check-certificate https://raw.githubusercontent.com/ascoderu/opwen-setup/master/{setup-webapp,.shared}.sh
    chmod +x setup-webapp.sh

    # find out how to use the script
    ./setup-webapp.sh -h

Support
-------

The `setup-webapp.sh` script is tested with hardware:

* `Raspberry Pi 3 <https://www.raspberrypi.org/products/raspberry-pi-3-model-b/>`_
  running Raspbian Jessie lite v2016-05-27, v2017-01-11 and v2017-04-10

* `Orange Pi Zero <http://www.orangepi.org/orangepizero/>`_
  running Ubuntu server 16.04 LTS v0.8.1

The `setup-webapp.sh` script is tested with USB modems:

* Huawei E303s-65

The `setup-cloudserver.sh` script is tested on:

* `Azure Standard DS1 v2 <https://docs.microsoft.com/en-us/azure/virtual-machines/virtual-machines-linux-sizes?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#dsv2-series>`_
  running Ubuntu 14.04 LTS

* `Azure Standard DS1 v2 <https://docs.microsoft.com/en-us/azure/virtual-machines/virtual-machines-linux-sizes?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#dsv2-series>`_
  running Ubuntu 16.04 LTS

License
-------

The original version of this code was written during the 2016 Microsoft OneWeek
hackathon which is why this project is released under the Microsoft Tech4Good
license (MIT) instead of under the Apache 2 license that is the standard for
Ascoderu projects.
