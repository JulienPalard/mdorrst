# mdorrst

[![PyPI](https://img.shields.io/pypi/v/mdorrst.svg)](https://pypi.org/project/mdorrst/)
[![PyPI](https://img.shields.io/pypi/l/mdorrst.svg)](https://github.com/JulienPalard/mdorrst/blob/master/LICENSE)
[![Tests](https://github.com/JulienPalard/mdorrst/workflows/Tests/badge.svg)](https://github.com/JulienPalard/mdorrst/actions?query=workflow%3ATests)

Tell appart Markdown and reStructuredText.


## Usage

The package exposes a single function, `sniff(content)`, trying to
deduce the format used, returning it as a string: `md`, `rst` or
`txt`:

```pycon
>>> import mdorrst
>>> mdorrst.sniff("[hey](http://example.com)")
'md'
>>> mdorrst.sniff("`hey <http://example.com>`__")
'rst'
```
