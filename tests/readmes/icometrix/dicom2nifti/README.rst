=============
 dicom2nifti
=============

Python library for converting dicom files to nifti

:Author: Arne Brys
:Organization: `icometrix <https://www.icometrix.com>`_
:Repository: https://github.com/icometrix/dicom2nifti
:API documentation: http://dicom2nifti.readthedocs.io/en/latest

=====================
 Using dicom2nifti
=====================
---------------
 Installation
---------------
.. code-block:: bash

   pip install dicom2nifti

---------------
 Updating
---------------
.. code-block:: bash

   pip install dicom2nifti --upgrade

---------------
 Usage
---------------
Command line
^^^^^^^^^^^^^
.. code-block:: bash

   dicom2nifti [--no-compression] [--no-reorientation] input_directory output_directory

for more information

.. code-block:: bash

   dicom2nifti -h

From python
^^^^^^^^^^^^

Converting a directory with dicom files to nifti files

.. code-block:: python

   import dicom2nifti

   dicom2nifti.convert_directory(dicom_directory, output_folder)

Converting a directory with only 1 series to 1 nifti file

.. code-block:: python

   import dicom2nifti

   dicom2nifti.dicom_series_to_nifti(original_dicom_directory, output_file, reorient_nifti=True)

----------------
 Supported data
----------------
Most anatomical data for CT and MR should be supported as long as they are in classical dicom files.

Try avoiding "Implicit VR Endian" if possible as this makes converting non anatomical (i.e. DTI, fMRI, ...) much more difficult.

There is some vendor specific support, more specifically for 4D imaging like fMRI and DTI/DKI

GE MR
^^^^^^
Anatomical data should all be support.
4D images like fMRI and DTI/DKI are supported.

Siemens MR
^^^^^^^^^^^
Anatomical data should all be support.
4D images like fMRI and DTI/DKI are supported.

Philips MR
^^^^^^^^^^^
For classic dicom files dicom2nifti support anatomical.
For classic dicom files 4D images like fMRI and DTI/DKI are supported.

For "Philips Enhanced Dicom" there is no support for "Implicit VR Endian" transfer syntax.
For the others we support anatomical and 4D images like fMRI and DTI/DKI.

------------------
 Unsupported data
------------------
If you encounter unsupported data you can help the development of dicom2nifti by providing a dataset. This dataset should be anonymised (but leave as much of the private fields as possible).


