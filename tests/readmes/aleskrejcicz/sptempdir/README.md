# (SP)TEMPDIR

**Function parameters:**

	sptempdir.TemporaryDirectory(suffix="", prefix="", dir=None, delete=True)

By default temporary directory will be deleted when function it is closed.


### Example 1:

The `name` property returns the name of a temporary directory.

```python
import os
from sptempdir import TemporaryDirectory

with TemporaryDirectory(prefix="prefbegin_", suffix="_suffend") as temp:
	print('temp.name:', temp.name)  # retrieve the name temporary directory
	print('Inside:', os.path.exists(temp.name))
	
print('Outside:', os.path.exists(temp.name))
```

*Terminal output:*

	$ temporary_directory.py
	temp.name: /tmp/prefbegin_66XxiFkN6Nm4_suffend
	Inside: True
	Outside: False


### Example 2:

```python
import os
from sptempdir import TemporaryDirectory

temp = TemporaryDirectory()
print('temp.name:', temp.name)  # retrieve the name temporary directory
print('Tempdir exists:', os.path.exists(temp.name))

temp.rmtemp()  # manually remove temporary directory
print('Tempdir exists:', os.path.exists(temp.name))
```

*Terminal output:*

	$ temporary_directory.py
	temp.name: /tmp/RCgAzfsATQnb
	Tempdir exists: True
	Tempdir exists: False


### Example 3:

If the delete parameter is `delete=False`, the temp directory is not deleted. 

```python
import os
from sptempdir import TemporaryDirectory

temp = TemporaryDirectory(delete=False)
print('temp.name:', temp.name)  # retrieve the name temporary directory
print('Tempdir exists:', os.path.exists(temp.name))

temp.rmtemp()  # manually remove temporary directory
print('Tempdir exists:', os.path.exists(temp.name))
```

*Terminal output:*

	$ temporary_directory.py
	temp.name: /tmp/kWwCWn42NRsr
	Tempdir exists: True
	Tempdir exists: False


### Example 4:

Specific `dir` where you want to create temporary directory.

```python
from sptempdir import TemporaryDirectory

temp = TemporaryDirectory(dir="/home/user/Desktop")
print(temp.name)  # retrieve the name temporary directory
```

*Terminal output:*

	$ temporary_directory.py
	/home/user/Desktop/4ZdTvLNqVuyE


### Installation:

	pip install sptempdir


### License:

	BSD

-----------------------

(SP)TEMPDIR = **( S**imple **P**ython **)** **TEMPDIR**

-----------------------

[![Travis](https://img.shields.io/travis/aleskrejcicz/sptempdir/master.svg)]() [![PyPI](https://img.shields.io/pypi/v/sptempdir.svg)]() [![PyPI](https://img.shields.io/pypi/pyversions/sptempdir.svg)]() [![PyPI](https://img.shields.io/pypi/l/sptempdir.svg)]()
