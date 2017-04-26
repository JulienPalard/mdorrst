========================
Team and repository tags
========================

.. image:: http://governance.openstack.org/badges/sahara-image-elements.svg
    :target: http://governance.openstack.org/reference/tags/index.html

.. Change things from this point on

Sahara image elements project
==============================

This repo is a place for Sahara-related for diskimage-builder elements.

Script for creating Fedora and Ubuntu cloud images with our elements and default parameters. You should only need to run this command:

.. sourcecode:: bash

    tox -e venv -- sahara-image-create

Note: More information about script `diskimage-create <https://github.com/openstack/sahara-image-elements/blob/master/diskimage-create/README.rst>`_
