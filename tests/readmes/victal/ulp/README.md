# ulp is a Location Picker

Ulp is a command-line tool that can be used to find and interact with URLs from a given input. 

Think of something like Facebook's [PathPicker](https://github.com/facebook/pathpicker), but for URLs.

## Installing

Ulp is a python package and as such it can be installed via pip. Until it's on PyPI, you can try installing it from this repo using
```
pip install git+https://github.com/victal/ulp.git@master
```

## Requirements

Ulp is being developed/used with Python 3.5, but it might just work with **Python > 3.0**

*Copy to clipboard* functionality depends on [Pyperclip](https://github.com/asweigart/pyperclip) and as such you might need to install additional modules for it to work. Check Pyperclip's Readme for details.


## Usage

Simply pipe or redirect the input from which you want to pick the URLs into **ulp**. Yes, just like PathPicker. Yes, it's on purpose.

**Example:**

If you're pushing to a BitBucket repository, for example, the output of `hg push` will give you the URL where you can create a new PR from the branch you just pushed to, so you can do

```
hg push | ulp
```

and open the given URL in a browser or copy it for later.

If you just want to list the URLs in a given input, you can use the **ulp_extract** helper script, like this:

```
cat huge_text_with_lots_of_urls | ulp_extract
```

## License

Ulp is licensed with the [MIT License](https://github.com/victal/ulp/blob/master/LICENSE)

## TODO

* Publish package to PyPI
* Finish 'Copy to Clipboard' (deal with error dependencies)
* Add a 'Command mode' similar to fpp
* Add a 'filter' option within the UI
* Add an example image/gif in this readme
* Tidy up - clean up code, ad a --help, tests and clean up code
