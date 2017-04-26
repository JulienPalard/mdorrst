## zc_common

### Installation
`pip install zc_common`

### Usage

```python
from zc_common import timezone

timezone.now()
```

See the READMEs in submodules for more information.

### Deployment

ZeroCater employees can find instructions [here](https://github.com/ZeroCater/mp-planning/blob/master/devops/deploying_to_pypi.md).

### Running tests

You can run tests to make sure zc_common code behaves as expected. To get started, follow these instructions:
```shell

# Create a new python virtualenv and install dependencies
mkvirtualenv zc_common
workon zc_common
pip install -r requirements

# Run the tests
python runtests.py
```
