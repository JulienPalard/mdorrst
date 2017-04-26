[![Version](https://img.shields.io/pypi/v/filelogger.svg)](https://pypi.python.org/pypi/filelogger)

#### Wrapper class for RotatingFileHandler from logging module

#### Installation

```sh
    pip install filelogger
```


#### Usage

```python

    from filelogger import FileLogger


    logger = FileLogger('path_for_file.log')
    logger.info(string) # print and save string in the path_for_file
    logger.info(arg1, arg2) # use couple of args
    logger.warning(string) # print and save string in the path_for_file
    logger.error(string) # print and save string in the path_for_file
```

#### Customization

```python

    from filelogger import FileLogger

    # Set file counts for the rotation
    # default 0 (meaning 1 file using)
    logger = FileLogger('path_for_file.log', file_counts=0)

    # Set max file size for the rotation (in bytes)
    # default 5242880 (5Mb)
    logger = FileLogger(path_for_file.log', max_file_size=5242880)

    # Disable print function call
    logger = FileLogger('path_for_file.log', stdout=False)
```
