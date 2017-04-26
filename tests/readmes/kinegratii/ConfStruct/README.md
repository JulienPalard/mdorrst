# ConfStruct

![travis](https://travis-ci.org/kinegratii/ConfStruct.svg?branch=master)
[![PyPI version](https://badge.fury.io/py/ConfStruct.svg)](https://badge.fury.io/py/ConfStruct)

## Overview

ConfStruct is a builder and parser between python objects and binary data in a specific scene.

For example, when you send some configure values to a RTU device.You may not send all values in a time,
so these configure values in bytes stream is not in a fixed position.The probably structure may be described as the following table:

| Field       | PC1  | VL1  | V1   | PC2  | VL2  | V 2  | ...  | PC   | VL n | V n  |
| ----------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Byte Length | 1    | 1    | 2    | 1    | 1    | 4    | -    | 1    | 1    | 4    |
| Value       | 0x01 | 0x02 | -    | 0x02 | 0x04 | -    | -    | 0x0A | 0x04 | -    |

Note: PC = param code, VL = value length, V = value

## Basic usage

The configure values what my demo GPRS RTU device support are list in the following table.

| Field Name     | Code | Byte Length | Data type                | Description                     |
| -------------- | ---- | ----------- | ------------------------ | ------------------------------- |
| Delay Restart  | 1    | 4           | Unsigned 32-bit interger | Delay seconds to restart device |
| Server Address | 2    | 6           | 4-byte ip + 2-byte port  | Server address to connect       |
| Awaken Period  | 3    | 2           | Unsigned 16-bit interger | The interval of reporting data  |

Use `ConfStruct` to describe the device config protocol.

```python
from conf_struct import ConfStruct, CField

class ServerAddressStruct:
    def parse(self, binary):
        ip0, ip1, ip2, ip3, port = struct.unpack('>4BH', binary)
        return '{0}.{1}.{2}.{3}:{4}'.format(ip0, ip1, ip2, ip3, port)

    def build(self, value):
        ip, port = value.split(':')
        ip_l = list(map(int, ip.split('.')))
        return struct.pack('>4BH', ip_l[0], ip_l[1], ip_l[2], ip_l[3], int(port))

class DeviceConfigStruct(ConfStruct):
    delayed_restart = CField(code=0x01, fmt='>H')
    server_address = CField(code=0x02, constructor=ServerAddressStruct())
    awaken_period = CField(code=0x03, fmt='>I')
```

Send config value to with `{server_address='192.168.1.200:10200', delayed_restart=180}` .

```
>>>  dcs = DeviceConfigStruct()
>>> dcs.build(server_address='192.168.1.200:10200', delayed_restart=180)
b'\x02\x06\xc0\xa8\x01\xc8\x27\xd8\x01\x02\x00\xb4'
>>> dcs.parse(b'\x03\x04\x00\x00\x0e\x10\x02\x06\xc0\xa8\x01\xc8\x27\xd8')
{'server_address':'192.168.1.200:10200', 'awaken_period': 3600}
```

## Integrate with construct library

[Construct](http://construct.readthedocs.io/en/latest/)  is a powerful **declarative** parser (and builder) for binary data.

Assign an object Implementing `build` and `parse` to `CField.constructor`,The following code fragment has same effect with the above one. 

```python
from construct import Struct, Adapter, Byte, Short, Int
from conf_struct import ConfStruct, CField

class ServerAddressAdapter(Adapter):
    def _encode(self, obj, context):
        ip, port = obj.split(":")
        port = int(port)
        return list(map(int, ip.split("."))) + [port // 256, port % 256]

    def _decode(self, obj, context):
        return "{0}.{1}.{2}.{3}:{4}".format(obj[0], obj[1], obj[2], obj[3], obj[4] * 256 + obj[5])


class DeviceConfigStruct(ConfStruct):
    delayed_restart = CField(code=0x01, constructor=Short)
    server_address = CField(code=0x02, constructor=ServerAddressAdapter(Byte[6]))
    awaken_period = CField(code=0x03, constructor=Int)
```

Besides `Adapter`, `Struct`  and `Sequence ` are also supported.See tests code in the source for more detail.

## Compatibility

The package has been tested in 2.7, 3.4, 3.5, 3.6 .

Note: The result of `build` is not unique due to unordered dict below python3.6.

## LICENSE

This project is under MIT License.