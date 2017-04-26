=======
ec2-ssh
=======

.. image:: https://img.shields.io/pypi/v/ec2-ssh.svg
    :target: https://pypi.python.org/pypi/ec2-ssh

.. image:: https://travis-ci.org/YPlan/ec2-ssh.svg?branch=master
    :target: https://travis-ci.org/YPlan/ec2-ssh


A pair of command line utilities for finding and SSH-ing into your Amazon EC2
instances by tag (such as 'Name').

Forked from Instagram original code by YPlan.

Installation
------------

From pip:

.. code-block:: bash

    pip install ec2-ssh

Usage
-----

.. code-block:: bash

    # ec2-ssh

    % ec2-ssh nginx2
    # equivalent to
    # ssh ubuntu@ec2-123-45-67-89.compute-1.amazonaws.com

    % ec2-ssh root@appserver
    % ec2-ssh deploy@nginx2 sudo restart nginx

    # Specifying the user with an environment variable
    % EC2_SSH_USER=deploy ec2-ssh nginx2

    # ec2-host

    # w/o arg: prints all active instances
    % ec2-host
    ec2-123-45-67-89.compute-1.amazonaws.com
    ec2-132-45-67-89.compute-1.amazonaws.com
    ec2-231-45-67-89.compute-1.amazonaws.com

    # w/ arg
    % ec2-host backend
    ec2-132-45-67-89.compute-1.amazonaws.com
    ec2-132-45-67-90.compute-1.amazonaws.com

    # w/ tag arg too
    % ec2-host -t environment production
    ec2-132-45-67-90.compute-1.amazonaws.com
    ec2-111-45-67-90.compute-1.amazonaws.com
