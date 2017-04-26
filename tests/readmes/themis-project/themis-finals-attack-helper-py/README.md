# themis-finals-attack-helper-py
[Themis Finals](https://github.com/aspyatkin/themis-finals) attack helper library.

## Installation
```
$ pip install themis.finals.attack.helper
```

## Usage
### Command line mode
```
$ THEMIS_FINALS_HOST=10.0.0.2 themis-finals-attack 035585b41e6bbd70834a05690d2575ad=
```
**Note:** 10.0.0.2 stands for an IP address of contest checking system. You may specify FQDN as well.

You can pass several flags at once. Please be aware of flag submitting restrictions (see [Themis Attack Protocol](https://github.com/aspyatkin/themis-attack-protocol) for additional information).

### Library mode
```python
from themis.finals.attack.helper import Helper

h = Helper('10.0.0.2')
flags = [
    '035585b41e6bbd70834a05690d2575ad=',
    'cdfdc8cbdcbe4c1e2e7378c52e1f35a5='
]

r = h.attack(*flags)  # [<Result.SUCCESS_FLAG_ACCEPTED: 0>, <Result.SUCCESS_FLAG_ACCEPTED: 0>] - stands for two successful attacks
```
To get information about all available result codes, please check out [Themis Attack Protocol](https://github.com/aspyatkin/themis-attack-protocol) and [themis.finals.attack.result](https://github.com/aspyatkin/themis-finals-attack-result-py).  
**Note:** `themis.finals.attack.Helper.attack` method can throw exceptions. These exceptions are subclasses of `themis.finals.attack.helper.AttackBaseError` class.

## License
MIT @ [Alexander Pyatkin](https://github.com/aspyatkin)
