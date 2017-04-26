# Mookfist LimitlessLED Controller v0.0.15

Intended as a simple wrapper around the LimitlessLED wifi protocol written in python.

Supports wifi bridge versions 4, 5, and 6. Current features implemented:

1. color
2. brightnes
3. toggle white color

Color values can be in a range from 0 to 255.
Brightness values can be in a range from 0 to 100.

## Installation

### From Source

Download the code: https://github.com/mookfist/mookfist-limitlessled-controller/archive/master.zip

```
$ unzip master.zip
$ python setup.py install
$ python lled.py --help
```

### From PyPI

```
$ pip install mookfist-lled-controller
$ lled.py --help
```

## API

The API is currently not documented but these examples should help get you going.

### API Examples
```python
# Set brightness to 50% for groups 1 and 2
from mookfist_lled_controller import WifiBridge
from mookfist_lled_controller import get_bridges

ip, macaddr = get_bridges(version=4)[0]

bridge = WifiBridge(ip, 8899, version=4)
bridge.brightness(50, 1)
bridge.brightness(50, 2)
```

```python
# Set color to 128 for group 1
from mookfist_lled_controller import WifiBridge
from mookfist_lled_controller import get_bridges

ip, macaddr = get_bridges(version=4)[0]

bridge = WifiBridge(ip, 8899, version=4)
bridge.color(128, 1)
```

```python
# Fade groups 1 through 4 from 100% to 0%
# This is a blocking operation
from mookfist_lled_controller import WifiBridge
from mookfist_lled_controller import get_bridges
from mookfist_lled_controller import fade_brightness

ip, macaddr = get_bridges(version=6)[0]
bridge = WifiBridge(ip, 5987, version=6)

fade_brightness(bridge, (1,2,3,4), 100, 0)
```

```python
# Fade color from 0 to 255 for groups 2 and 3
# This is a blocking operation
from mookfist_lled_controller import WifiBridge
from mookfist_lled_controller import get_bridges
from mookfist_lled_controller import fade_brightness

ip, macaddr = get_bridges(version=4)
bridge = WifiBridge(ip, 8899, version=4)

fade_color(bridge, (1,2,3,4), 0, 255)
```

```python
# Fade group 1 from 0 to 100% rather slowly
from mookfist_lled_controller import WifiBridge
from mookfist_lled_controller import get_bridges
from mookfist_lled_controller import fade_brightness

ip, macaddr = get_bridges(version=4)[0]
bridge = WifiBridge(ip, 8899, version=4, pause=50, repeat=5)

fade_brightness(bridge, (1), 0, 100)
```


## Command Line Interface

The lled.py script allows you to control your lights from the command line.

### Commands

| Command | Description |
| ------- | ----------- |
| fade <start> <end>   | Fade brightness from <start> to <end>. Values can be between 0 and 100 |
| fadec <start> <end> | Fade the color from <start> to <end>. Values can be between 0 and 255 |
| color <color> | Set color to <color>. Value can be between 0 and 255 |
| brightness <brightness> | Set the brightness to <brightness>. Value can be between 0 and 100 |
| on | Turn on a group |
| off | Turn off a group |
| white | Turn a group white |
| rgb <r> <g> <b> | Set the color using an RGB value. Each color is a number between 0 and 255 |
| colorcycle | Cycle through all available colors |


### Options
| Argument | Description | Default Value |
| -------- | ----------- | ------------- |
| --repeat         | Number of times to repeat a command. Increasing this value could improve smoothness, but means it will take a longer time to perform fades | 1 |
| --pause          | Number of milliseconds to pause between sending commands. Decreasing this value below 100ms might mean some commands are not processed | 100 |
| --group          | Group number. Repeat the argument for each group you want to send a command to | n/a |
| --debug          | Turn on debug logging | false |
| --bridge-ip      | The IP/hostname of the bridge. If omitted the bridge will be automatically scanned down | n/a |
| --bridge-port    | The port number of the bridge. | 8899 or 5987 |
| --bridge-version | The version of the LimitlessLED protocol | 4 |


### Examples


Fade light group 1 to 0% brightness

```
$ python lled.py fade 100 0 --group 1
```

Set color to groups 1 and 2
```
$ python lled.py color 128 --group 1 --group 2
```

Set brightness to 50% for group 3
```
$ python lled.py brightness 50 --group 3
```

Set group 1 to the color white (version 6)

$ python lled.py white --group 1 --bridge-version 6

## Tweaking

The repeat and pause values can be used to tweak how commands are sent. In general, you should wait 100ms between each command sent. But since there is no native fading in LimitlessLED, to achieve fading, the controller sends multiple commands to fade from one value to another.

If the pause is too small, some commands might get missed. But this is what the repeat setting can fix. You can send the same command more than once.

Getting smooth fading is not very easy with the wifi protocol, but you might be able to get better results by playing with these two values
