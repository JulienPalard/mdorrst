# NOCExec #
[![Build Status](https://travis-ci.org/velp/nocexec.svg?branch=master)](https://travis-ci.org/velp/nocexec)
[![Coverage Status](https://coveralls.io/repos/velp/nocexec/badge.svg)](https://coveralls.io/r/velp/nocexec)

NOCExec is a python (2 and 3 version) library for automating the processes of configuration and administration of network infrastructure. Provides a high level of performance for working with network devices without distinction of each operating system.

Supported protocols for connecting to devices:

 * SSH
 * Telnet
 * [NetConf](https://tools.ietf.org/html/rfc6241)

The following vendors of network equipment are supported:
 * Cisco: IOS (SSH, Telnet)
 * Juniper: JunOS (NetConf only)
 * Extreme networks: ExtremeXOS (SSH, Telnet)

## Installation
NOCExec can be installed from PyPi:
```bash
pip install nocexec
```

## Examples
Using a basic SSH client

```python
    >>> from nocexec import SSHClient
    >>> with SSHClient("192.168.0.1", "user", "password") as cli:
    ...     cli.execute("terminal length 0", wait=["#"])
    ...     cli.send("exit")
    ...
    ['terminal length 0', 'cisco-router']
```

Using a basic NetConf client

```python
    >>> from nocexec import NetConfClient
    >>> with NetConfClient("192.168.0.1", "user", "password") as cli:
    ...     cli.view("show system uptime", tostring=True)
    ...     cli.validate()
    ...     if cli.compare() is not None:
    ...         cli.commit()
    ...
    '<rpc-reply message-id="urn:uuid:a89b27fb-209c-4e61-9a38-993b51b54eae">\n<system-uptime-information>\n<current-time>\n
    .....
    </current-time>\n</system-uptime-information>\n</rpc-reply>\n'
```

Using driver for Juniper device with JunOS operating system:

```python
    >>> from nocexec.drivers.juniper import JunOS
    >>> with JunOS("192.168.0.1", "user", "password") as cli:
    ...     cli.edit("set interfaces ae0.0 description Test")
    ...     cli.save()
    ... 
    <ncclient.xml_.NCElement object at 0x7fd9581d6c90>
    True
    >>> with JunOS("192.168.0.1", "user", "password") as cli:
    ...     cli.view("show system uptime", tostring=True)
    ... 
    '<rpc-reply message-id="urn:uuid:ea3192f8-3e94-4565-86ce-c81f07269845">\n  <system-uptime-information>\n    <current-time>\n      <date-time seconds="1493113938">2017-04-25 12:52:18 MSK</date-time>\n    </current-time>\n    <system-booted-time>\n      <date-time seconds="1490603699">2017-03-27 11:34:59 MSK</date-time>\n      <time-length seconds="2510239">4w1d 01:17</time-length>\n    </system-booted-time>\n    <protocols-started-time>\n      <date-time seconds="1490749306">2017-03-29 04:01:46 MSK</date-time>\n      <time-length seconds="2364632">3w6d 08:50</time-length>\n    </protocols-started-time>\n    <last-configured-time>\n      <date-time seconds="1493113807">2017-04-25 12:50:07 MSK</date-time>\n      <time-length seconds="131">00:02:11</time-length>\n      <user>vponomarev</user>\n    </last-configured-time>\n    <uptime-information>\n      <date-time seconds="1493113938">\n12:52PM\n</date-time>\n      <up-time seconds="2510269">\n29 days,  1:17\n</up-time>\n      <active-user-count format="2 users">\n2\n</active-user-count>\n      <load-average-1>\n0.02\n</load-average-1>\n      <load-average-5>\n0.07\n</load-average-5>\n      <load-average-15>\n0.07\n</load-average-15>\n    </uptime-information>\n  </system-uptime-information>\n</rpc-reply>\n'
```

Using driver for Cisco device with IOS operating system:

```python
    >>> from nocexec.drivers.cisco import IOS
    >>> with IOS("192.168.0.1", "user", "password") as cli:
    ...    cli.edit("interface FastEthernet 0/31")
    ...    cli.edit("description Test")
    ...    cli.save()
    ... 
    ['interface FastEthernet 0/31']
    ['description Test']
    True
    >>> with IOS("192.168.0.1", "user", "password") as cli:
    ...     cli.view("sh run interface Fa0/31")
    ... 
    ['sh run interface Fa0/31', 'Building configuration...', '', 'Current configuration : 126 bytes', '!', 'interface FastEthernet0/31', ' description Test', ' switchport access vlan 9', ' switchport mode access', ' spanning-tree portfast', 'end', '']
```

Using driver for Extreme networks device with XOS operating system:

```python
    >>> from nocexec.drivers.extreme import XOS
    >>> with XOS("192.168.0.1", "user", "password") as cli:
    ...     cli.edit("create vlan Test tag 1000")
    ...     cli.save()
    ... 
    [' create vlan Test tag 1000', '', '* ']
    True
    >>> with XOS("192.168.0.1", "user", "password") as cli:
    ...     cli.view("show switch")
    ... 
    [' show switch', '', '', 'SysName:          swm', 'SysLocation:      ', 'SysContact:       ', 'System MAC:       00:04:96:52:D9:8D', 'System Type:      X670-48x', '', 'SysHealth check:  Enabled (Normal)', 'Recovery Mode:    All', 'System Watchdog:  Enabled', '', 'Current Time:     Tue Apr 25 14:02:30 2017', 'Timezone:         [Auto DST Disabled] GMT Offset: 240 minutes, name is not set.', 'Boot Time:        Mon Mar 20 20:27:10 2017', 'Boot Count:       23', 'Next Reboot:      None scheduled', 'System UpTime:    35 days 17 hours 35 minutes 20 seconds ', '', 'Current State:    OPERATIONAL             ', 'Image Selected:   primary                 ', 'Image Booted:     primary                 ', 'Primary ver:      15.3.2.11               ', 'Secondary ver:    12.6.2.10   ', '', 'Config Selected:  primary.cfg                                          ', 'Config Booted:    primary.cfg                                          ', '', 'primary.cfg       Created by ExtremeXOS version 15.3.2.11', '                  254518 bytes saved on Tue Apr 25 14:01:57 2017']
```

## Tests
You can run the tests by invoking
```bash
tox
```
in the repository root.