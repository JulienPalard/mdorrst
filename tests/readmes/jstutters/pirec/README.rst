========
Pirec
========

.. image:: https://travis-ci.org/jstutters/pirec.svg?branch=master
 :target: https://travis-ci.org/jstutters/pirec
 :alt: Build Status

.. image:: https://readthedocs.org/projects/pirec/badge/?version=latest
 :target: http://pirec.readthedocs.org/en/latest/?badge=latest
 :alt: Documentation Status

Pirec is a Python package for wrapping scripts so that their inputs and
outputs are preserved in a consistent way and results are recorded.


Example
-------

.. code:: python

    from pirec import call, record, pipeline
    from pirec.artefacts import TextFile


    @record()
    def pipeline_stage_1(f):
        call(['/bin/cat', f.filename])


    @record()
    def pipeline_stage_2(f):
        call(['/bin/cat', f.filename])


    def my_pipeline(file1, file2):
        pipeline_stage_1(file1)
        pipeline_stage_2(file2)


    def example_pipeline():
        pipeline.run(
            'example',
            my_pipeline,
            '/my/data/directory',
            TextFile('month00/data.txt'), TextFile('month12/data.txt')
        )


    if __name__ == '__main__':
        example_pipeline()


Installation
------------

::
    
    pip install pirec


Requirements
------------

Pirec is tested with Python v2.7 - 3.6.  Use of the MongoDB or SQLDatabase
result recorders requires the installation of the ``pymongo`` or ``sqlalchemy``
modules as appropriate.  Depending on your database SQLAlchemy may require
additional support libraries to be installed.


Documentation
-------------

Full documentation is hosted on `Read the Docs <http://pirec.readthedocs.org>`_.


Contribute
----------

- Issue Tracker: `github.com/jstutters/pirec/issues <http://github.com/jstutters/pirec/issues>`_
- Source Code: `github.com/jstutters/pirec <http://github.com/jstutters/pirec>`_


Support
-------

If you are having problems, please let me know by submitting an issue in the tracker.
