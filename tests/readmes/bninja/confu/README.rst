=====
confu
=====

.. image:: https://travis-ci.org/bninja/confu.png
   :target: https://travis-ci.org/bninja/confu

.. image:: https://coveralls.io/repos/bninja/confu/badge.png
   :target: https://coveralls.io/r/bninja/confu

Helpers for using these infrastructure tools:

- `troposphere <https://github.com/cloudtools/troposphere>`_
- `aws cfn <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html>`_
- `ansible <http://docs.ansible.com/>`_

dev
---

.. code:: bash

   $ git clone git@github.com:bninja/confu.git
   $ cd confu
   $ mkvirtualenv confu
   (confu)$ pip install -e .[tests]
   (confu)$ py.test tests/ --cov=confu

install
-------

.. code:: bash

   $ pip install con-fu


settings
--------

Read and merged from these ``ini`` files:

- ``~/.confu.cfg``
- ``.confu.cfg``

and these environment variables:

- ``CONFU_PROFILE``
- ``CONFU_REGION``
- ``CONFU_LOG``

To see what they are:

.. code:: bash

   $ confu cfg
   {
       "atlas": {
           "source_dir": "infras/global/atlas"
       }, 
       "aws": {
           "default_region": "us-west-1", 
           "regions": [
               "us-west-1"
           ]
       }, 
       "cfn": {
           "bucket_format": "{profile}-confu-cfn-{region}", 
           "bucket_key": "vault", 
           "parameters": {
               "ConfName": "infra-vault", 
               "ConfSource": "{profile}-confu-pkg", 
               "InfraSilo": "vault", 
               "KeyName": "ai-gazelle", 
               "LogArchiveBucket": "{profile}-confu-log"
           }, 
           "stack_name_format": "{Prefix}-{AppEnv}-{random}", 
           "stack_tags": {
               "infra-silo": "vault"
           }
       }, 
       "pkg": {
           "bucket_format": "{profile}-{region}-confu-pkg", 
           "default_includes": [
               "group_vars/", 
               "host_vars/", 
               "roles/", 
               "/ansible.cfg", 
               "!*/ansible.cfg", 
               "*.yml", 
               "!.project", 
               "!*.git", 
               "!*.pyc", 
               "!*.pyo", 
               "!*.git*", 
               "!*.travis.yml", 
               "!*.md", 
               "!Vagrantfile", 
               "!*/test/", 
               "!test.yml"
           ], 
           "includes": [
               "infras/", 
               "!infras/global/mq.yml", 
               "!infras/global/site.yml", 
               "!infras/global/.confu.cfg", 
               "!infras/global/inventories/", 
               "!infras/global/formations/", 
               "!infras/global/roles/", 
               "inventories/", 
               "ops/"
           ], 
           "name": "{source.dir_name}", 
           "source_dir": "./", 
           "stage_dir": "/tmp/confu/{package.name}-{package.version}", 
           "version": "{source.git_version}"
       }, 
       "profile": "julius", 
       "region": "us-west-1"
   }

shell
-----

Source completion and functions like:

.. code:: bash

   $ source <(confu shell env; confu shell complete)

or use in all shells like:

.. code:: bash

   $ (confu shell env; confu shell complete) > ~/confu.sh
   $ cat >> ~/.bashrc <<EOF
   
   . ~/confu.sh
   EOF

confue
------

Shell function for managing ``confu`` environments which are just these environment variables:

- ``CONFU_PROFILE``
- ``CONFU_REGION``
- ``CONFU_LOG`` 

like this:

.. code:: bash

   $ confue
   CONFUE_NAME=
   CONFU_PROFILE=
   CONFU_REGION=
   CONFU_LOG=
   $ confue jj-us-w1
   $ confue -p julius -r us-west-1 -l i
   $ confue
   CONFUE_NAME=jj-us-w1
   CONFU_PROFILE=julius
   CONFU_REGION=us-west-1
   CONFU_LOG=i
   $ confue off
   $ confue
   CONFUE_NAME=
   CONFU_PROFILE=
   CONFU_REGION=
   CONFU_LOG=
   $ confue ls
   jj-us-w1
