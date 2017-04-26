# capy

## Installation

Install `brew` by `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` (if not already installed)

Install `Python` by  `brew install python`

And finally install this tool by `pip install capy` (optionally you need to run `pip install pyyaml` if it fails)

## Usage

You will need a file named `capy_conf.yaml` which will contain all information needed for capy to run.
See ![example](example-capy_conf.yaml) with comments for more info.

And you should also use file named `capy_private.yaml` for your private configuration. (This file should be in `.gitignore`)
See ![example](example-capy_private.yaml) with comments for more info.

## Publish to PYPI

1) Register on `https://pypi.python.org/`)

2) Register new project: `python setup.py register`

3) Upload new build: `python setup.py sdist upload`

