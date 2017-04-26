# pippy
pippy-json is a performance point(PP) calculator for Osu! **Standard** beatmaps.
The output is json to allow easier use with other programs.
Most of the code is based on the C++ version located [here](https://github.com/Francesco149/oppai).

# Usage

This program is written in python and requires version **3.x** (tested only with 3.5).
There are several supported arguments.

* -link `Link to the beatmap (like https://osu.ppy.sh/b/1337)`
* -acc `Accuracy percentage`
* -c100 `Number of 100's`
* -c50 `Number of 50's`
* -m `Number of misses`
* -sv `Score version (1 or 2)`
* -mods `String describing which mods are used (like - HDHR)`

Examples:
```python
python console_calc.py map.osu
python console_calc.py map.osu -mods HDDTHR
python console_calc.py -link https://osu.ppy.sh/b/994495 -mods HD -acc 95.61
```

# Installing pippy with pip
`pip install osupippy`
or
```
git clone https://github.com/jamesguessis/pippy-json
cd pippy-json
pip install .
```