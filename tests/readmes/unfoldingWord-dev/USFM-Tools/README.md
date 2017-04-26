master:
[![Build Status](https://travis-ci.org/unfoldingWord-dev/USFM-Tools.svg?branch=master)](https://travis-ci.org/unfoldingWord-dev/USFM-Tools) 
[![Coverage Status](https://coveralls.io/repos/github/unfoldingWord-dev/USFM-Tools/badge.svg?branch=master)](https://coveralls.io/github/unfoldingWord-dev/USFM-Tools?branch=master)

develop:
[![Build Status](https://travis-ci.org/unfoldingWord-dev/USFM-Tools.svg?branch=develop)](https://travis-ci.org/unfoldingWord-dev/USFM-Tools) 
[![Coverage Status](https://coveralls.io/repos/github/unfoldingWord-dev/USFM-Tools/badge.svg?branch=develop)](https://coveralls.io/github/unfoldingWord-dev/USFM-Tools?branch=develop)

# USFM-Tools

This project comprises a framework for transforming .usfm files into specified targets.

It is primarily used for the Open English Bible, and may need adjustment if used for other purposes.

This fork of USFM-Tools includes basic support for conversion to USX.

# Installation

# Prerequisites

    sudo easy_install pyparsing

# Get code

    git clone https://github.com/kbuildsyourdotcom/USX.git
    cd USX
    python transform.py --setup
 
(This downloads ConTeXt and may take a while.)
 
# Font Setup

After getting the Noto fonts installed on the system, the following can be run to get the Noto fonts into ConTeXt:

    . /opt/context/tex/setuptex
    export OSFONTDIR="/usr/local/share/fonts;$HOME/.fonts"
    mtxrun --script fonts --reload
    context --generate
    
Running `mtxrun --script fonts --list --all --pattern=*oto*` should now list a bunch of the Noto fonts.  More information at http://wiki.contextgarden.net/Fonts_in_LuaTeX.


# Run

When running the conversion, you may split the results by book (currently only supported for USX):

    python transform.py --target=usx --usfmDir=./docs/source/ --builtDir=./docs/translation/ --fileByBook

To output the results to single file (supported by all output formats):

    python transform.py --target=usx --usfmDir=./docs/source/ --builtDir=./docs/translation/ --name=MyTranslation

# Production Use

This script will be used in the process of converting USFM text from Etherpad into USX format. The text in Etherpad will first be combined using this script https://github.com/Door43/tools/blob/master/uwb/ep_export.py. The output of the afor mentioned script will then be processed by the script in this repository to transform the USFM to USX. This USX output will at some point become available in the translationStudio api under the Bible translation projects.
