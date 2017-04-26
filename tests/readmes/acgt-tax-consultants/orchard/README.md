<p align="center"><img src="images/logo.png"></p>
<p align="center">A pipeline creation framework for simplifying reruns and branching</p>

[![Build Status](https://travis-ci.org/acgt-tax-consultants/orchard.svg?branch=master)](https://travis-ci.org/acgt-tax-consultants/orchard) [![Coverage Status](https://coveralls.io/repos/github/acgt-tax-consultants/orchard/badge.svg?branch=master)](https://coveralls.io/github/acgt-tax-consultants/orchard?branch=master)


### Installation
###### (Development mode [after setting up your environment](https://github.com/acgt-tax-consultants/gitting-started)):  

```bash
$ git clone https://github.com/(your_username)/orchard.git
$ cd orchard
$ pip install -e .
```

---

### Running

In one tab (as `luigid` blocks, and `luigid --background` is a pain to kill)

```bash
$ luigid
```

In a separate tab

```bash
$ cd example
$ orchard template link.yaml
# Fill in the configuration file that was generated using the first infile as
# 'test_files/a.txt'
$ orchard build link.yaml config.yaml
$ orchard launch test.py ModuleThree  # This will eventually not be necessary
```

[1]: images/logo.png
