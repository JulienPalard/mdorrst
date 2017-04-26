|CircleCI| |Codacy Badge| |License| |CHUV|

I2B2 Import
===========

Introduction
------------

This library provides functions to import data into an I2B2 DB schema.

Installation
------------

Run: ``pip install i2b2_import``

Usage
-----

To import brain features (and/or other observations) from a CSV file,
use:

::

    features_csv_import.csv2db(file_path, i2b2_conn, dataset, config):
        Import brain features and other observation facts data from a CSV file into the I2B2 DB schema.
        * param file_path: Path to the CSV file.
        * param i2b2_db_url: URL of the I2B2 DB.
        * param dataset: Data set name.
        * param config: A few settings. It is a dictionary that accepts the following fields:
            - pid_in_vid: Rarely, a data set might mix patient IDs and visit IDs. E.g. : LREN data. In such a case, you
            to enable this flag. This will try to split PatientID into VisitID and PatientID.
            - sid_by_patient: Rarely, a data set might use study IDs which are unique by patient (not for the whole study).
            E.g.: LREN data. In such a case, you have to enable this flag. This will use PatientID + StudyID as a sessionID.
        * param regions_name_file: CSV file containing the abbreviated regions name in the first column and the full names
            in the second column.

or from a folder:

::

    features_csv_import.folder2db(folder, i2b2_conn, dataset, config):
        Import brain features and other observation facts data from a folder containing CSV files into the I2B2 DB schema.
        * param folder: Folder path
        * param i2b2_db_url: URL of the I2B2 DB.
        * param dataset: Data set name.
        * param config: A few settings. It is a dictionary that accepts the following fields:
            - pid_in_vid: Rarely, a data set might mix patient IDs and visit IDs. E.g. : LREN data. In such a case, you
            to enable this flag. This will try to split PatientID into VisitID and PatientID.
            - sid_by_patient: Rarely, a data set might use study IDs which are unique by patient (not for the whole study).
            E.g.: LREN data. In such a case, you have to enable this flag. This will use PatientID + StudyID as a sessionID.
        * param regions_name_file: CSV file containing the abbreviated regions name in the first column and the full names
            in the second column.

To import metadata from the data-catalog-db, use:

::

    data_catalog_import.catalog2i2b2(data_catalog_conn, i2b2_conn):
        Import meta data from the Data Catalog DB to the I2B2 schema.
        * param data_catalog_conn: Connection to the Data Catalog DB.
        * param i2b2_db_url: URL of the I2B2 DB.

To import metadata from extra files (XML, JSON, ...), use:

::

    ppmi_xml_import.meta2i2b2(file_path, db_conn, dataset):
        Import meta-data from a file into the I2B2 schema.
        * param file_path: File (XML, JSON, ...) containing meta-data for a given dataset (PPMI, EDSD, ...).
        * param i2b2_db_url: Connection to the I2B2 DB.
        * param dataset: Dataset ID (each dataset uses its own meta-data files format)

or from a folder:

::

    ppmi_xml_import.folder2db(folder, db_conn, dataset):
        Import meta-data from files from a given folder (recursive) and for a given dataset into the I2B2 schema.
        * param folder: Folder containing meta-data files for a given dataset.
        * param i2b2_db_url: URL of the I2B2 DB.
        * param dataset: Dataset ID (each dataset uses its own meta-data files format)

Test
----

Open the tests directory and run ``./test.sh``.

NOTE: Docker is needed.

build
-----

Run ``./build.sh``.

Push on PyPi
------------

Run ``./publish.sh``.

(This builds the project prior to pushing it).

.. |CircleCI| image:: https://circleci.com/gh/LREN-CHUV/i2b2-import.svg?style=svg
   :target: https://circleci.com/gh/LREN-CHUV/i2b2-import
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/850854199e9c4fbca8386a10bf1c4867
   :target: https://www.codacy.com/app/mirco-nasuti/i2b2-import?utm_source=github.com&utm_medium=referral&utm_content=LREN-CHUV/i2b2-import&utm_campaign=Badge_Grade
.. |License| image:: https://img.shields.io/badge/license-Apache--2.0-blue.svg
   :target: https://github.com/LREN-CHUV/i2b2-import/blob/master/LICENSE
.. |CHUV| image:: https://img.shields.io/badge/CHUV-LREN-AF4C64.svg
   :target: https://www.unil.ch/lren/en/home.html
