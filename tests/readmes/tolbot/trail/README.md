# trail

Keep track of your thoughts. 

### Installation

```
$ pip install trail
```

### Usage:

Save a new trail, in current directory (creates a ".trail" file), for example:
```
$ trail enter some text here ...
$ trail "Use quotes if your trail contains weird-f@r-bash characters!"
$ trail "is inspired by https://github.com/jonromero/trail "
```

Print trails found in current directory .trail file.
```
$ trail
```

Save a new "global" trail (in "~/.trail/.trail", requires dir to exist)
```
$ trail -g enter some text here ...
```

Print "global" trails.
```
$ trail -g
```
