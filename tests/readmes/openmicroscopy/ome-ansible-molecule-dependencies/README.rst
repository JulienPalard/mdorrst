Dependencies for testing OME Ansible roles with Molecule
========================================================

.. image:: https://travis-ci.org/openmicroscopy/ome-ansible-molecule-dependencies.png
   :target: http://travis-ci.org/openmicroscopy/ome-ansible-molecule-dependencies

.. image:: https://badge.fury.io/py/ome-ansible-molecule-dependencies.svg
    :target: https://badge.fury.io/py/ome-ansible-molecule-dependencies

A meta-package that installs common dependencies required to test most `OME Ansible Galaxy roles <https://galaxy.ansible.com/openmicroscopy/>`_.

Example `.travis.yml` file for testing Ansible roles:

..  code-block:: yaml

    ---
    sudo: required
    language: python

    services:
      - docker

    install:
      - pip install ome-ansible-molecule-dependencies

    script:
      - molecule test

    notifications:
      webhooks: https://galaxy.ansible.com/api/v1/notifications/
