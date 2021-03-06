====
tmtk
====

A toolkit for ETL curation for the tranSMART data warehouse. The
TranSMART curation toolkit (``tmtk``) can be used to edit and validate
studies prior to loading them with `transmart-batch`_.

Some features: 
 - create a transmart-batch ready study from clinical data files.
 - load an existing study and validate its contents. 
 - edit the transmart concept tree in The Arborist graphical editor. 
 - create chromosomal region annotation files.

Disclaimer
          

tmtk is a ``python3`` package meant to be run in ``Jupyter notebooks``.
Results for other setups may vary.

For documentation visit `readthedocs`_.

Usage
-----

Step 1: Opening a notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^

First open a Jupyter Notebook, open a shell and change directory to some
place where your data is. Then start the notebook server:

.. code:: sh

    cd /path/to/studies/
    jupyter notebook

This should open your browser to Jupyters file browser, create a new
notebook for here.

Step 2: Using tmtk
^^^^^^^^^^^^^^^^^^

.. code:: py

    # First import the toolkit into your environment
    import tmtk

    # Then create a <tmtk.Study> object by pointing to study.params of a transmart-batch study
    study = tmtk.Study('~/studies/a_tm_batch_ready_study/study.params')
    # Or, by using the study wizard on a directory with correctly structured, clinical data files.
    # (Visit the transmart-batch documentation to find out what is expected.)
    study = tmtk.wizard.create_study('~/studies/dir_with_some_clinical_data_files/')

Now we have loaded the study as a ``tmtk.Study`` object we have some
interesting functions available:

.. code:: py

    # Check whether transmart-batch will find any issues with the way your study is setup
    study.validate_all()

    # Graphically manipulate the concept tree in this study by using The Arborist
    study.call_boris()

For more, see the `examples`_.

Installation
------------

To install tmtk and all dependencies into your Python environment, and enable the Arborist Jupyter notebook extension, run:

.. code:: sh

    $   pip3 install tmtk

or..

.. code:: sh

    $   pip3 install -r requirements.txt
    $   python3 setup.py install

or if you want to run the tool from code in development mode:

.. code:: sh
    $   pip3 install -r requirements.txt
    $   python3 setup.py develop
    $   jupyter-nbextension install --py tmtk.arborist
    $   jupyter-serverextension enable tmtk.arborist

Requirements
^^^^^^^^^^^^

These dependencies will have to be installed:
 - pandas>=0.19.2
 - ipython>=5.3.0
 - jupyter>=1.0.0
 - jupyter-client>=5.0.0
 - jupyter-core>=4.3.0
 - jupyter-console>=5.1.0
 - notebook>=4.2.0
 - requests>=2.13.0
 - tqdm>=4.11.0
 - mygene>=3.0.0

Licence
-------
GPLv3

.. _transmart-batch: https://github.com/thehyve/transmart-batch/
.. _readthedocs: https://tmtk.readthedocs.io/en/latest/
.. _examples: examples