# Gasp-tools

*Gasp* streamlines and automates repetitive tasks in development workflows:

- **build**: create new project build
- **deploy**: incremental deploy to target host
- **watch**: automate builds and deployments triggered by local modifications
- **download**, **upload**: transfer files/directories to/from target host
- **ssh**: ssh into target host
- **run**, **sudo**: execute command on target host as [un]privileged user
- user-defined tasks

*Gasp* runs smoothly on Linux and macOS, and relies on [Fabric](http://www.fabfile.org) and [rsync](https://en.wikipedia.org/wiki/Rsync). 
It's SSH-based, so it doesn’t require installing any agents on remote hosts.

# Installation

Install `gasp-tools` using [pip](http://www.pip-installer.org):

~~~
$ pip install gasp-tools
~~~

> If the installation fails, you might need to install the SSL development libraries. On Ubuntu and Debian Linux distributions: `sudo apt-get -fy install libssl-dev`. On macOS `brew install openssl`.

> To upgrade: `pip install gasp-tools --upgrade`

Dependencies: Install `rsync`. On Ubuntu and Debian Linux distributions:

~~~
$ sudo apt-get -fy install rsync
~~~

On macOS with [brew](http://brew.sh):

~~~
brew install rsync
~~~

# Usage

Copy the file [gaspfile.py](https://github.com/micheda/gasp-tools/blob/master/gasp_tools/data/templates/default/gaspfile.py) into your project directory, tune it and you're ready to go!

## Command line arguments

~~~
usage: gasp [-h] [--src SRC] [--dst DST] [--log LOG] [--nocolor] [--verbose]
            task [id] [cmdline [cmdline ...]]

Gasp 0.0.11 streamlines and automates repetitive tasks in development
workflows.

positional arguments:
  task        task to execute: clean, build, deploy, watch, ssh, download,
              upload, list, run, sudo [, user-defined]
  id          id of target host. Required for some tasks
  cmdline     command line to be executed on the target host

optional arguments:
  -h, --help  show this help message and exit
  --src SRC   copy from local path SRC
  --dst DST   copy to remote path DST (default: DEPLOY_DIR)
  --log LOG   log stdout to file
  --nocolor   disable colors
  --verbose   enable verbose mode
  ~~~


## Task: build

The `build` task executes a `clean`, copies the files/directories listed in BUILD_INCLUDES into the BUILD_DIR directory and executes the user-defined task `build` (if defined).

Example:
~~~
$ gasp build
~~~

## Task: deploy

The `deploy` task synches the content of the BUILD_DIR directory with the DEPLOY_DIR directory on the target host and executes the user-defined task `deploy` (if defined). The synchronisation is incremental and is performed using *Rsync*.

Example using `srv` as id of target host:
~~~
$ gasp deploy srv
~~~


## Task: watch

The `watch` task executes a `deploy` and looks for changes in files located inside the SRC_DIR. Whenever a change is detected, a `deploy` is triggered.

Example using `srv` as id of target host:
~~~
$ gasp watch srv
~~~


## Task: ssh

The `ssh` task opens an SSH shell on the target host.

Example using `srv` as id of target host:
~~~
$ gasp ssh srv
~~~


## Task: run and sudo

The `run` and `sudo` tasks execute a command on the target host as unprivileged and privileged user, respectively.

Examples of run and sudo tasks using `srv` as id of target host and `whoami` as command:
~~~
$ gasp run srv whoami
$ gasp sudo srv whoami
~~~

## Task: download and upload

The `upload` task uploads a local file or directory to the target host. Relative paths specified with `--src` are relative to the current directory. The file will be uploaded on the home directory of **USER** if a destination path is not specified with `--dst`.

The `download` task downloads a remote file or directory to the local host. Relative paths specified with `--src` are relative to the home directory of **USER**. The file will be downloaded to the local directory **./ADDRESS/** if a destination path is not specified with `--dst`.

Example of upload and download tasks using `srv` as id of target and `x` as source file.
~~~
$ gasp upload vm1 --src x
$ gasp download vm1 --src x
~~~
 
## Task: list

The `list` task lists the available target hosts.

Example:
~~~
$ gasp list
~~~

# Configuration file

The configuration file `gaspfile.py` is evaluated as a Python script and contains the parameters and the user-defined tasks of the project. It must be located in the top directory of the project. *Gasp* injects for you these global variables:

- `config`: dictionary defining paths and other parameters
- `include`: function to include additional configuration files
- `gasp`: object granting access to fabric and other features
- `log`: object adding logging capabilities

## `config` parameters

- `config["SOURCE_DIR"]`: path to project sources
- `config["BUILD_DIR"]`: path to temporary project build
- `config["BUILD_INCLUDES"]`: list of paths to be included in build
- `config["DEPLOY_DIR"]`: remote directory for deployment
- `config["RSYNC_ARGS"]`: additional arguments passed to rsync
- `config["HOSTS"]`: dictionary of target hosts, whose keys are ids and each value is a dictionary with keys "ADDRESS", "PORT", "USER", and "KEY".

All parameters must be set and all paths must be either absolute or relative to the main configuration file.

## `include` function

You can include additional configuration files with `include("path_to_file")`.

> It is good practice to have one central configuration file `~/.gaspfile.py` that defines `config["HOSTS"]` (authentication details) and other common user-defined tasks. `~/.gaspfile.py` can then be included by different projects.

## `gasp` object

`gasp` provides the methods `run`, `local`, `sudo`, `put`, `get` whose name, parameters and semantics are the same of the Fabric [core operations](http://docs.fabfile.org/en/1.13/api/core/operations.html). `gasp.host_id` is the id of the target host. `gasp.host` is the entry in the configuration file for the target host.

## `log` object

`log` provides two convenient methods to manage user-defined, colored output messages: `info(message, color = None)` and `fatal(message)`. Available colors: `"magenta"`, `"blue"`, `"green"`, `"yellow"`, `"red"`, `"white"` and `"cyan"`. Blue is never used by *gasp* internally, and therefore is a good candidate for user-defined messages. Fatal messages are always red and result in an immediate termination of the process.

## user-defined tasks

User-defined tasks are defined as regular functions. User-defined task `build` is called (if defined) by `gasp.build()` once the BUILD_DIR has been generated. User-defined task `deploy` is called (if defined) by `gasp.deploy()` once the content of BUILD_DIR has been synchronized to the target host. Reserved task names that should not be used because not reachable from command line are: `clean, watch, ssh, download, upload, list, run, and sudo`. 

Example of user-defined task `ping`:

In `gaspfile.py`:

~~~
...

def ping():
    gasp.local("ping -c1 %s" % gasp.host["ADDRESS"])
~~~

From command line:

~~~
$ gasp ping srv
~~~



## Example: minimal configuration
Example of minimal configuration file that can be used to synchronize a local directory `src/data` to a remote directory `~/gasp_deployed` on target host id `srv`:

```python
config["SOURCE_DIR"] = "src"
config["BUILD_DIR"] = ".build"
config["BUILD_INCLUDES"] = [ "src/data" ]
config["DEPLOY_DIR"] = "~/gasp_deployed"
config["RSYNC_ARGS"] = ""
config["HOSTS"] = { "srv" :{ "ADDRESS": "127.0.0.1", "PORT": 22, "USER": "mike", "KEY": "~/.ssh/id_dsa" } }
```
