# PyCAMVerter

[![Build Status](https://img.shields.io/travis/white-lab/pycamverter.svg)](https://travis-ci.org/white-lab/pycamverter)
[![Build status](https://ci.appveyor.com/api/projects/status/0uew150mwdh2qesx?svg=true)](https://ci.appveyor.com/project/naderm/pycamverter)
[![Coverage Status](https://img.shields.io/coveralls/white-lab/pycamverter.svg)](https://coveralls.io/r/white-lab/pycamverter?branch=master)
[![Documentation Status](https://readthedocs.org/projects/pycamverter/badge/?version=latest)](https://readthedocs.org/projects/pycamverter/?badge=latest)
[![Requirements Status](https://requires.io/github/white-lab/pycamverter/requirements.svg?branch=master)](https://requires.io/github/white-lab/pycamverter/requirements/?branch=master)
[![PyPI](https://img.shields.io/pypi/v/pycamverter.svg)](https://pypi.python.org/pypi/pycamverter)


Utility for converting searched mass spec data into a format readable by [CAMV](https://github.com/white-lab/pycamverter/blob/master/README.md).

![pycamverter demo](https://zippy.gfycat.com/CleverGrotesqueErmine.gif)

## Installation

To download a completely packaged Windows executable, visit our [releases page](https://github.com/white-lab/pycamverter/releases)

To install the core pycamverter python library, run the following command:

```
pip install pycamverter
```

## Usage

To use pycamverter, select your raw data file, your search files (either MASCOT .xml or ProteomeDiscoverer .msf), and an optional excel listing scan numbers in a file browser. Then simply drag-and-drop them onto PyCAMVerter.exe.

After a few minutes of processing, you should see the output .camv.gz file in the same directory as your raw file.

For a full list of arguments, run PyCAMVerter.exe from the command line:

```
usage: PyCAMVerter [-h] [-v] [-q] [-V] [--show_gui]
                   [--raw_paths RAW_PATHS [RAW_PATHS ...]]
                   [--search_path SEARCH_PATH] [--scans_path SCANS_PATH]
                   [--scans [SCANS [SCANS ...]]] [--out_path OUT_PATH]
                   [files [files ...]]

Aww yeah, mass specs!

positional arguments:
  files                 Raw, search, or scan list files, determined by file
                        extension.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increase verbosity of output.
  -q, --quiet           Decrease verbosity of output.
  -V, --version         show program's version number and exit
  --show_gui            Show GUI for converting files.
  --raw_paths RAW_PATHS [RAW_PATHS ...]
                        Raw data file(s) containing mass spec data.
  --search_path SEARCH_PATH
                        MASCOT or ProteomeDiscoverer search files.
  --scans_path SCANS_PATH
                        .xlsx or .csv file listing scans to select for
                        validation.
  --scans [SCANS [SCANS ...]]
                        Individual scans to select for validation.
  --out_path OUT_PATH   Output path for CAMV export.
```
