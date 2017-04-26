# datadump • [![Build Status][travis-image]][travis] [![License][license-image]][license]

* Python package for easy saving and loading in directory organized workspaces. *

[travis-image]: https://travis-ci.org/riceric22/datadump.png?branch=master
[travis]: https://travis-ci.org/riceric22/datadump

[license-image]: http://img.shields.io/badge/license-Apache--2-blue.svg?style=flat
[license]: LICENSE

## Why? 
To eliminate repetitive plumbing code when saving and loading data in different
organizational folders. 

### Install
`pip install datadump`

### Usage 

+ `datadump.wd()` returns the working directory
+ `datadump.pwd()` prints the working directory, which by default is `tmp/`
+ `datadump.swd(s)` changes the working directory to `s`
+ `datadump.save(name, *args, **kwargs)` saves `(*args, **kwargs)` to your
working directory, and also returns the tuple. 
+ `datadump.load(name)` returns the tuple stored under `name`. 

### Example

```Python
>>> datadump.pwd()
tmp/
>>> datadump.swd('directory')
>>> datadump.save('experiments1', [1,2,3], alpha=0.1, beta=6)
(([1, 2, 3],), {'alpha': 0.1, 'beta': 6})
>>> datadump.load('experiments1')
(([1, 2, 3],), {'alpha': 0.1, 'beta': 6})
```