## Case Conversion
This is a port of the [CaseConversion Sublime Plugin](https://github.com/jdc0589/CaseConversion), by [Davis Clark's](https://github.com/jdc0589), to a regular python package. I couldn't find any other python packages on PyPi at the time (Feb 2016) that could seamlessly convert from any case to any other case without having to specify from what type of case I was converting. This plugin worked really well, so I separated the (non-sublime) python parts of the plugin into this useful python package. I also added Unicode support using the `regex` package. Credit goes to [Davis Clark's](https://github.com/jdc0589) and the contributors to that plugin (Scott Bessler, Curtis Gibby, Matt Morrison) for their awesome work on making such a robust and awesome case converter.

#### Features

- Autodetection of case (no need to specify explicitly which case you are converting from!)
- Unicode supported (non-ASCII characters for days!)
- Acronym detection (no funky splitting on every capital letter of an all caps acronym like `HTTPError`!)
- And obviously case conversions from/to the following types of cases:
  - `camelcase`
  - `pascalcase`
  - `snakecase`
  - `dashcase`
  - `spinalcase` (alias for `dashcase`)
  - `kebabcase` (alias for `dashcase`)
  - `constcase`
  - `screaming_snakecase` (alias for `constcase`)
  - `dotcase`
  - `separate_words`
  - `slashcase`
  - `backslashcase`
- Oh! Python2 and Python3 supported!


##### Usage

Normal use is self-explanatory.

```python
>>> import case_conversion
>>> case_conversion.kebabcase("FOO_BAR_STRING")
'foo-bar-string'
>>> print(case_conversion.constcase(u"fóó-bar-string"))
FÓÓ_BAR_STRING
```

To use acronym detection set `detect_acronyms` to `True` and pass in a list of `acronyms` to detect as whole words.

```python
>>> import case_conversion
>>> case_conversion.snakecase("fooBarHTTPError")
'foo_bar_h_t_t_p_error'  # ewwww
>>> case_conversion.snakecase("fooBarHTTPError", detect_acronyms=True, acronyms=['HTTP'])
'foo_bar_http_error'  # pretty
```

## Install

```
pip install case-conversion
```


## Licence

Using [MIT licence](LICENSE.txt) with Davis Clark's Copyright
