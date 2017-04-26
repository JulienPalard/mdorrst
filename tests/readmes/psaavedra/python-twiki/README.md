# python-twiki

python-twiki is a bunch of tools which allow manage a TWiki.

# Install

## From the source

```sh
$ git clone https://github.com/psaavedra/python-twiki.git
$ cd python-twiki
$ sudo python setup.py install
```

## From PyPI

```sh
$ sudo pip install twiki
```

# Examples

## Configuration file (setup.cfg)

```
[global]
loglevel:20
logfile:/dev/stdout
url:http://localhost/twiki

[auth]
type:http_basic
username:user
password:pass
```
where `url` is something like: ''https://wiki.igalia.com/twiki''.

In the other hand, the `auth` settings refer to HTTP Basic
authentication parameters, in necessary case.

## Getting Topics from a Web

```sh 
$ twiki-get-topics -c setup.cfg -o list.csv -w WebName

```

where `list.csv` results something like this:

```
"WebName/WebTopic1",
"WebName/WebTopic2",
```

## Moving a Topic to another Topic parent

```sh
$ twiki-move-topic -c setup.cfg -t WebName/WebTopic -p NewWebTopicParent
$ twiki-move-topic -c setup.cfg -i list.csv
$ twiki-move-topic -c setup.cfg -i list.csv -p NewWebTopicParent

```

where `list.csv` is something like this:

```
"WebName/WebTopic1", "NewWebTopicParent1"
"WebName/WebTopic2", "NewWebTopicParent2"

```

## Renaming Topics

```sh
$ twiki-rename-topic -c setup.cfg -t WebName/WebTopic -n NewWebName/NewWebTopic
$ twiki-rename-topic -c setup.cfg -t WebName/WebTopic -n WebName/NewWebTopic
$ twiki-rename-topic -c setup.cfg -t WebName/WebTopic -n NewWebName/WebTopic
$ twiki-rename-topic -c setup.cfg -i list.csv
```

where `list.csv` is something like this:

```
"WebName/WebTopic1", "NewWebName/NewWebTopic1"
"WebName/WebTopic2", "NewWebName/NewWebTopic2"
```


