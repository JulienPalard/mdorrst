# What is this?

For python applications that need to generate windows installer packages,
there are two options that I know of: the builtin `msilib`, which is 
greatly underdeveloped, and this package.

 This package wraps `go-msi`, which is an existing MSI framework that allows
 simple generation of windows installers. `go-msi` was chosen because it already
 does the hard work, allowing this package to have a tiny footprint.

 Most of the code in this package focuses on detecting and installing `go-msi`
 and its dependency, the WiX toolset. The principle current use of this package
 is [subzero][1].

 [1]: https://github.com/xoviat/subzero