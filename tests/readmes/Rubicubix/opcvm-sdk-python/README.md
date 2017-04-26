# Background

OPCVM360 is a [financial data provider] (http://www.opcvm360.com), servicing a broad range of European funds.

Please request a login and password to [Finance Web Working] (http://www.opcvm360.com/solutions-pro#contact-infos) ; or direct contacts as per below:

* email: contact@fww.fr
* tel: +33 (0) 1 83 64 63 06

# Installation

* **From git:**
```bash
git clone https://github.com/Rubicubix/opcvm-sdk-python.git
```
* **From pip:**
```bash
pip install opcvm-sdk-python
```
* **From PyPI:**

Download [the distribution] (https://pypi.python.org/pypi/opcvm-sdk-python) from the Python Package Index.
Once downloaded and unzipped,
```bash
python setup.py install
```

# Code snippets

A little overview of the functionalities for a given fundshare (ISIN: LU0068578508). Enjoy!

* **Retrieve a Fundshare object:**
```python
from opcvm_sdk import OpcvmService, ApiException
_isin = 'LU0068578508'
try:
    _service = OpcvmService()
    _fundshare = _service.get_fundshare_by_isin(_isin)
    print(_fundshare.idFundShare)
except ApiException as e:
    print(e)
```

* **Retrieve a pandas.DataFrame object:**
```python
from opcvm_sdk import OpcvmService, ApiException
_isin = 'LU0068578508'
try:
    _service = OpcvmService()
    _history = _service.get_history_by_isin(_isin, "2017-01-01", "2017-03-15")
    _history['vl'].plot()
except ApiException as e:
    print(e)
```