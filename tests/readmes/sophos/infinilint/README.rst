Infinilint
=======================

Infinilint is a configurable lint runner. The base yaml configuration includes
many common linters and a new linter is added with 3 or 4 lines of yaml. The
linters are Docker images and are run in parallel to maximize feedback and make
it practical to run continuously during development and as a stage in CI.

Requirements
============

Infinilint depends on Docker. Install the latest version for your platform.

Installing
==========

Clone this repo and run::

    pip install .

Usage
=====

To see the configured linters::

    infinilint --list

To run a single linter::

    infinilint rubocop

Run all enabled linters::

    infinilint

Watch a folder continuously and run linters on any changes::

    infinilint --watch

Configuration
=============

In the root of your repository, create a .infinilint.yml file. This file will
be combined with the base.yml in application folder. To enabled linters, create
a file that looks like::

    linters:
        rubocop:
            enabled: true
        yamllint:
            enabled: true

To add a linter not configured in the base.yml, create entries using the
base.yml as a model.

Additional root values you can set in your config::

    timeout: maximum number of seconds the tool is allowed to run
    proxy: address of a local docker registry to pull the images from instead of dockerhub
