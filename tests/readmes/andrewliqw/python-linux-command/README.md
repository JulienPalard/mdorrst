# Python linux command

Provide the functions of os/shutil with the same name used in linux commands.

I am a Linux fan, but loves Python so much. Each time I call the functions such
as os.getcwd(), I have to take two seconds to think about the name. Why not
the same to linux command pwd? That is the reason to have this python module.

Note: This module only support Python 3.5+ and Linux.

## Installation

https://pypi.python.org/pypi/allinux

```shell
pip install allinux
```

## Usage

```python
from allinux import coreutils, shbuiltins


# current working directory
shbuiltins.pwd()

# change to home directory
shbuiltins.cd()


# coreutils.system_context
coreutils.uname('-a')
coreutils.uname('-s -o -r')
```
