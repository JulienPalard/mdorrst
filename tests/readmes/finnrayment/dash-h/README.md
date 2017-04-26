# dash-h

[![Build Status](https://travis-ci.org/finnrayment/dash-h.svg?branch=master)](https://travis-ci.org/finnrayment/dash-h)
[![Requirements Status](https://requires.io/github/finnrayment/dash-h/requirements.svg?branch=master)](https://requires.io/github/finnrayment/dash-h/requirements/?branch=master)

Automatically generate POSIX-standard shell utilities from YAML files.

## Description

With the large amount of utilities used by programmers, being able to parse arguments to the program allows for a range of options that are otherwise unavailable. Parsing booleans, numbers and strings before the program is run can be effective and run inside the program itself. The issue is however, that multiple implementations exist, and each language handles arguments in a different way.

dash-h is an attempt to unify this, by writing a simple configuration file in standard YAML notation, major languages can be targeted and have the argument parsing utility automatically generated for them.

Not only will the generated file contain language-idiomatic functions to automatically parse arguments, but a POSIX-standard 'usage' file is also generated, and can be included where needed.

## Installation

Multiple versions of Python are supported, however the version of Python must be > 2.7 or 3.

dash-h has a list of requirements in `requirements.pip` and can be installed with the following command:

```
pip install -r requirements.pip
```

After doing so, create a yaml file abiding by the standards discussed below and execute the following line with Python to generate the utility:

```
python dash_h.py -i input_file -o output_folder -l language
```

Output folder is optional. If not specified, one will be automatically generated.  
Language is optional, and will change localisation strings in generated file. English is default.

## Usage

To specify the target language, write the `language` key and set the value to one of the available languages listed at the bottom.

To create argument flags, write yaml keys following the below syntax:

```
arguments:
    -
        - short: '-h'     # Short argument flag. (Optional)
        - long: '--help'  # Long argument flag. (Optional)
        - description: 'Example argument.'  # Description in usage file. (Optional)
        - return: usage   # Will print whatever is here.
        - name: false    # The name given to the value. (Optional)
	- range: 0 3.5    # Only available when value points to an identifier. (Optional)
	- optional: true # Determines weather or not argument is required.
```

Note that only **either** the `short` or `long` key is required, as both do not *have* to coexist.

Note that also the `return` key is special, in that by making the value: `usage`, the usage file will be printed instead of the word. By appending a `$` in front of the word, a file of choice can be read from.

If the `value` key is defined as a string other than `false`, or not defined at all, a variable will be generated with a manipulatable value of whatever is typed in after the flag call. eg. `--example-flag 3.1` will store the value of `3.1`. Error checks are automatically generated.

By presenting a `range` key, the value forcibly required to be an `int` or `float` and is cast upon generation. If the range desired extends to infinity on either the minimum or maximum side, the range can be written with `min` and `max`. eg. `range: min 314` will create a range from negative infinity to positive 314.

Input arguments work in the same way as flags but only take two keys:

```
inputs:
    -
        - description: The file to open.
        - value: filename
```

While the first is optional, the `description` key once again serves as a description of the argument for the usage file, but the `value` key will generate a variable containing the input which the user can access and manipulate.

### Example file

Below is the complete yaml file that was used to generate arguments for dash-h, and the usage file that was generated with it:

```
language: 'python'

arguments:
    -
        - short: '-h'
        - long: '--help'
        - description: 'Displays this help file.'
        - return: usage
        - store: false
		- optional: true
    -
        - short: '-v'
        - long: '--version'
        - description: 'Displays the program version.'
        - return: $VERSION.txt
        - store: false
		- optional: true
	-
        - short: '-i'
        - long: '--input'
        - description: 'The YAML configuration file to generate from.'
    	- store: filename
		- optional: false
	-
        - short: '-o'
        - long: '--output'
        - description: 'The folder to output the generation to.'
    	- store: outputpath
		- optional: false
	-
        - short: '-l'
        - long: '--language'
        - description: 'Language localisation to generate with.'
    	- store: language
		- optional: true
```

```
Usage: dash_h [-hv] [-l language] -i filename -o outputpath
	-h, --help                     Displays this help file.
	-v, --version                  Displays the program version.
	-i, --input                    The YAML configuration file to generate from.
	-o, --output                   The folder to output the generation to.
	-l, --language                 Language localisation to generate with.
```

## Project status

Languages that can be targeted for generation:
* Python. `language: python`

Localisation translations: (Currently looking for willing translators!)
* English. `-l en`

## Contributing

Any contributions of quality are accepted and highly appreciated, any pull-requests will also be checked and managed. Consider checking the 'Issues' tab, or the 'TODO' file containing matters that have yet to be solved.

## License

All software is licensed under the Thusix Software License.
