# Amet 

Amet is a Python 2/3 library to read and write complex configuration from and to environment variables.

## Motivation

Some time ago I had to deploy an application to Heroku. This meant that I had to read the application's configuration from environment variables instead of the JSON files I had previously created. I wrote this library so that I could dump those configuration files into
environment variables and then load them. 

This means that you do not need to give up the benefits of using a JSON file (or YML or other formats) while using environment variables for configuration.

## How to use

Install the library with a simple `pip install amet`.

### Loading

In order to load configuration values from environment variables, the `load_from_environment` function is provided. It expects a dictionary, `proto`, as its first argument and optionally two strings, `prefix` and `separator`, and a boolean value, `force_uppercase`. This function will iterate over `proto` and read environment variables that can be used to fill it.

The environment variables that will be read are expected to have a particular format: `<prefix><separator><key-1><separator>...<key-n>` where `prefix` and `separator` are the arguments passed to `load_from_environment`. `key-1` through `key-n` correspond to the keys of nested dictionaries. If `force_uppercase` is set, the environment variables will be converted to uppercase.

For example, the following dictionary...

```python
proto = {
	'root': {
		'nested': None
	},
	'value': None
	'integer': int
}
```
...will be filled with the value from the following environment variables (asuming `prefix` is left empty, `separator` is `_` and `force_uppercase` is `True`):

* `ROOT_NESTED`
* `VALUE`
* `INTEGER`

A new dictionary is returned, the input dictionary will be left untouched.

### Conversion of values

Amet will attempt to convert values to Python primitive types. If the value for a given key is of type `int`, `float`, or `bool` (or the types themselves), upon reading the corresponding environment variables, Amet will attempt to convert those values. If the type of the value is `str` or `NoneType`the read value if left as is (which is `str`).

For example, in the previous example, `root.nested` and `value` are assumed to be strings, however, `integer` will be converted to `int` as that is the value given to that key. If a number such as `0` or `1` had been set then the value of `integer` would have also been converted.

### Dumping

The `dump` function is also provided. this function will return a dictionary of the key-value pairs that should be set as environment variables. If we called `dump` with the dictionary in the previous example, the output would be:

```python
{
	'ROOT_NESTED': ...,
	'VALUE': ...,
	'INTEGER': ...
}
```

`prefix`, `separator` and `force_uppercase` can also be passed.

### Exceptions

When a problem occurs loading or dumping a dictionary, errors may be raised.

* `IncompatibleTypeError`, a subclass of `TypeError` will be raised if a key in the dictionary is not a `str` object or if a value is not a `dict`, `str`, `int`, `float` or `bool` value.
* `KerError` is raised if an environment variable cannot be read.
* `ValueError` is raised if a value cannot be parsed, for example if an integer is expected but the value is a string not corresponding to a number.

## TODO

- [ ] Improve this README.
- [ ] Add some useful examples for `dump` such as setting those variables in Heroku.
- [ ] Add support for lists.
- [ ] Check for possible name clashes when loading or dumping variables.
- [ ] Improve unit tests.

## Contributing

If you find any issues feel free to report them [here](https://github.com/maurodec/amet/issues/new). If you want you can also fork the project and submit a pull request.