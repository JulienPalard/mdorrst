# coati
A tool for generating PowerPoint and Excel based reports.

## Dependencies

The win32api for python should be installed via its
official installer. The rest of the dependencies should be installed via
`pip` with the following command:

```
$ pip install -r requirements.txt
```

For installing dependencies, please ensure that you go to a processes
similar to the following:

```
$ pip install my-dependency
$ pip freeze > requirements.txt
$ git add requirements.txt
```

## Running scripts at 'bin' in windows

In order to run a script from the bin directory,
you will need to set the PYTHONPATH environment
variable first.

At the windows cmd shell, run the following:

```
x:\> set PYTHONPATH=.
```

Which will work for the whole session in that window.
Now you can run a script like this (note the backward slash **\\**):

```
x:\> python bin\my_script.py
```
````````
