## snappy_stream

Streaming snappy compression for Python file-like objects.

The main interface is through adapters.  These are classes which wrap around existing file-like objects and transparently compress or decompress.

The adapters are meant for byte streams.  To read and write text, you'll want another layer on top of this.

There are also a few helpers for opening read/write streams to s3 and local filesystem.  The S3 variants of these require the `smart_open` package.

## usage
### wrapper interface

For writing, there's SnappyWriteWrapper:
```python
from snappy_stream import SnappyWriteWrapper
with open('./something', 'wb') as some_file:
    with SnappyWriteWrapper(some_file, owns_sink=False) as wrapped:
        wrapped.write(b"something)
```

For reading, there's SnappyReadWrapper:
```python
from snappy_stream import SnappyReadWrapper
with open('./something', 'rb') as some_file:
    with SnappyReadWrapper(fin, owns_source=False) as wrapped:
        decompressed = wrapped.read()
```

#### ownership
The read wrapper has a required `owns_source` parameter, and the write wrapper has an analogous `owns_sink`.  This is required for properly propagating the `io.IOBase.close()` method.

If you expect to close the underlying stream in another way, the value of these should be `False`.  In this case:
* On the reader, `.close` does nothing.
* On the writer, `.close` flushes its compression buffer.

If you want the wrapper to assume ownership, pass `owns_source=True` or `owns_sink=True`.  In this case:
* On the reader, `.close` closes the underlying stream.
* On the writer, `.close` flushes its compression buffer, flushes the underlying stream, and then closes the underlying stream.

##### Example
Not passing ownership:
```python
some_file = open('./something', 'rb')
with SnappyReadWrapper(some_file, owns_source=False) as wrapped:
    data = wrapped.read()
assert not some_file.closed
some_file.close()
```

Passing ownership:
``` python
some_file = open('./something', 'rb')
with SnappyReadWrapper(some_file, owns_source=True) as wrapped:
    data = wrapped.read()
assert some_file.closed
```

If you're going to hand over ownership write after constructing another stream, you can just do this:
``` python
with SnappyReadWrapper(open('./something', owns_source=True)) as some_file:
    data = some_file.read()
```

### helpers

#### filesystem
```python
from snappy_stream.openers import open_fs_read_bytestream, open_fs_write_bytestream
with open_fs_write_bytestream('./something.snappy') as fout:
    fout.write(b"message")

with open_fs_read_bytestream('./something.snappy') as fin:
    data = fin.read()
```

#### s3
The s3 helpers require the `smart_open` package.
```python
from snappy_stream.openers import open_s3_read_bytestream, open_s3_write_bytestream
with open_s3_write_bytestream('s3://some-bucket/something') as fout:
    fout.write(b"message")

with open_s3_read_bytestream('s3://some-bucket/something') as fin:
    data = fin.read()
```

## design
The adapter interfaces are intentionally one-way -- there's no adapter for both reading and writing.  You can do something like this by using separate read and write wrappers to one stream.


## license

MIT

