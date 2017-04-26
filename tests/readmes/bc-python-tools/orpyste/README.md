What about this package  ?
==========================

**orPyste**, which is an anagram of **pyStore**, has been built to make easy to work with textual datas easy stored in a text file.

***If you want more informations and examples than thereafter, just take
a look in the docstrings.***


What's new in this version `1.3.0-beta` ?
=========================================

One useful new feature : you can now aggregate different virtual ¨peuf files inside a single physicial one using sections.


What was new in the preceding version `1.2.0-beta` ?
====================================================

There are some important changes in this version.

1. The mode ``multikeyval``, for repeatable keys in the same block, has been totally implemented.

1. You can now use a context manager with the classes ``Read``, ``ReadBlock`` and ``Clean``. By using ``with ... as ...:``, you let the package calls for you the methods ``build`` and ``remove_extras`` *(this last method had name ``remove`` before)*.

1. The class ``ReadBlock`` no longer has the methods ``flatdict`` and ``recudict``. Instead, it has two properties ``flatdict`` and ``treedict`` that allow to work with ``dict`` like variables. For customized dictionaries, you can use the new method ``mydict``.

1. The old method ``rtu_datas`` of the class ``Infos`` has been replaced by the property ``rtu`` which outputs are easier to "understand", and there is also an iterator ``yrtu`` to work with the "same" kind of datas with the classes ``Read`` and ``ReadBlock``.


I beg your pardon for my english...
===================================

English is not my native language, so be nice if you notice misunderstandings, misspellings or grammatical errors in my documents and my codes.


Why yet another tiny language to store textual datas ?
======================================================

The package `orpyste` was born from a need to quickly write simple and structured datas to configuration files and for unit tests. Before getting into the details, here is a small example of an `orpyste` file storing informations on players. Sorry for the lack of originality ...


```
joueur_1::
    date  = 1985
    sexe  = masculin
    score = 18974
    alias = Super Mario

joueur_2::
    date  = 1991
    sexe  = féminin
    score = 32007
    alias = Sonic
```

Writing this with XML could be done like this :

```xml
<joueur_1 date="1985" sexe="masculin" score="18974" alias="Super Mario"/>

<joueur_2 date="1991" sexe="féminin" score="32007" alias="Sonic"/>
```

Using JSON, we could use the following variable.

```json
{
    "joueur_1": {
        "date": "1985",
        "sexe": "masculin",
        "score": "18974",
        "alias": "Super Mario",
    },
    "joueur_2": {
        "date": "1991",
        "sexe": "féminin",
        "score": "32007",
        "alias": "Sonic",
    }
}
```

As you can see, for simple datas, `orpyste` gives a very simple and efficient way to store informations.


How to write files readable by `orpyste` ?
==========================================

The specification of the files readeable by `orpyste` is named `peuf`. So the two questions become : *"What is a well formatted `peuf` file ?"*.
To answer this, let's look at the following example.

```
/*
Long comment: here, we use the first block as a container.

Note the use of two consecutive double points so as to indicate a block.
*/  
book::
// Short comment: then the block `general` uses a key-value storing.
    general::
        author = M. Nobody
        title  = Does this book have a title ?
        date   = 2012, May the 1st

// Short comment: the last block `resume` uses a verbatim content.
    resume::
        This book is an ode to the passing time...


////
```


Let's explain the content of the preceding example.

1. You can comment your `peuf` files using C-like comments but **a comment can only start at the very beginning of a line**.

1. Datas are structured in blocks which can be of three different kinds.

  * A block is indicated using two consecutive double points and its content is indented.

  * A block can be a container like the block `book`. This is for gathering different blocks.

  * The block `general` stores key-value datas with the possibility to choose the separators. **Here we have used `=` but it is not an obligation.** You can also choose to allow or not multiple use of the same key.

  * The last kind of blocks is for a verbatim content. The last empty lines are removed except if you use the magic comment `////` as we have done. In our example the block `resume` has a content made of `This book is an ode to the passing time...` followed by two empty lines.


Reading the datas line by line
==============================

Let's consider the following file where `book` is a container, `general` is a classical key-value content using the separator `=` and `resume` has a verbatim content.  

```
book::
    general::
        author = M. Nobody
        title  = Does this book have a title ?
        date   = 2012, May the 1st

    resume::
        This book is an ode to the passing time...
        A challenging thinking.
```


Let's suppose that `user/example.peuf` is the path of our storing file. Using the following code shows how to read our datas.

```python
from pathlib import Path
import pprint

from orpyste.data import Read

with Read(
    content = Path("user/example.peuf"),
    mode    = {
        "container" : ":default:",
        "keyval:: =": "general",
        "verbatim"  : "resume"
    }
) as datas:
    for onedata in datas:
        if onedata.isblock():
            print('--- {0} ---'.format(onedata.querypath))
        elif onedata.isdata():
            pprint.pprint(onedata.rtu)
```

Launching in a terminal, the script will produce the following output where you can note that a "querypath" like `book/general` indicates that the block `general` is inside the block `book`.

```
--- book/general ---
(4, 'author', '=', 'M. Nobody')
(5, 'title', '=', 'Does this book have a title ?')
(6, 'date', '=', '2012, May the 1st')
--- book/resume ---
(9, 'This book is an ode to the passing time...')
(10, 'A challenging thinking.')
```

You can see that verbatim contents are given line by line, and that the separator between one key and its value is always indicated. This last behavior is due to the fact that you can use different separators if you want.
The number of lines in the original content are always given so as to let other applications the possibility to use them for messages.


Let's see another example with the following data file.

```
logic::
    A <==> B
    A ==> B
    A <== P
```

This file is easy to read with the code above where `mode = "multikeyval:: <==> <== ==>"` is a shortcut for `mode = {"multikeyval:: <==> <== ==>": ":default:"}`. This setting allows multiple uses of the same key.

```python
from pathlib import Path
import pprint

from orpyste.data import Read

with Read(
    content = Path("user/example.peuf"),
    mode    = "multikeyval:: <==> <== ==>"
) as datas:
    for onedata in datas:
        if onedata.isblock():
            print('--- {0} ---'.format(onedata.querypath))
        elif onedata.isdata():
            pprint.pprint(onedata.rtu)
```

The output below shows the necessity here to always have the separators.

```
--- logic ---
(3, 'A', '<==>', 'B')
(4, 'A', '==>', 'B')
(5, 'A', '<==', 'P')
```


Reading the datas block by block
================================

We go back to our second example with the following file whose path is `user/example.peuf`.

```
book::
    general::
        author = M. Nobody
        title  = What is the title ?
        date   = 2012, May the 1st

    resume::
        This book is an ode to the passing time...
        A challenging thinking.
```


The class `ReadBlock` is a subclass of `Read` so you can use any methods working with `Read`. But the goal of `ReadBlock` is to work with dictionaries instead of reading datas line by line *(for large files this last choice is a better one)*. Let's see first the property `flatdict`.

```python
from pathlib import Path

from orpyste.data import ReadBlock

with ReadBlock(
    content = Path("user/example.peuf"),
    mode    = {
        "container" : ":default:",
        "keyval:: =": "general",
        "verbatim"  : "resume"
    }
) as datas:
    print(datas.flatdict)
```


The code launched in one terminal gives us the following output *(which has been hand formatted)*.

```
MKOrderedDict([
    (id=0,
     key='book/general',
     value=MKOrderedDict([
        (id=0,
         key='author',
         value={'nbline': 4, 'value': 'M. Nobody', 'sep': '='}),
        (id=0,
         key='title',
         value={'nbline': 5, 'value': 'What is the title ?', 'sep': '='}),
        (id=0,
         key='date',
         value={'nbline': 6, 'value': '2012, May the 1st', 'sep': '='})
     ])
    ),
    (id=0,
     key='book/resume',
     value=(
        {'nbline': 9, 'value': 'This book is an ode to the passing time...'},
        {'nbline': 10, 'value': 'A challenging thinking.'})
    )
])
```


As you can see, the keys are "querypaths" and the values are the datas. You can also use the property `treedict` which produces a dictionary with a structure similar to the one of the blocks in the content analyzed. The following code is merly the same as the previous one *(`[...]` indicates the first lines of the preceding code)*.

```python
[...]

with ReadBlock(...) as datas:
    print(datas.treedict)
```


Here are the dictionary produced *(the ouput has been hand formatted)*.

```
RecuOrderedDict([
    ('book',
     RecuOrderedDict([
        ('general',
         RecuOrderedDict([
            ('author',
             {'nbline': 4, 'sep': '=', 'value': 'M. Nobody'}),
            ('title',
             {'nbline': 5, 'sep': '=', 'value': 'What is the title ?'}),
            ('date',
             {'nbline': 6, 'sep': '=', 'value': '2012, May the 1st'})
         ])
        ),
        ('resume',
         (
            {'nbline': 9,
             'value': 'This book is an ode to the passing time...'},
            {'nbline': 10,
             'value': 'A challenging thinking.'}
         )
        )
     ])
    )
])
```


If you want to customize a little the dictionary build by ``ReadBlock``, you can use the method `mydict` like in the following example *(see the "docstrings" for more informations)*.

```python
[...]

with ReadBlock(...) as datas:
    print('--- Standard "flat" dict ---')
    print(datas.mydict("std nosep nonb"))

    print('--- Standard "tree" dict ---')
    print(datas.mydict("tree std nosep nonb"))
```


We obtain here two standard dictionaries with neither separators, nor number lines.

```
--- Standard "flat" dict ---
{
    'book/general': {
        'author': 'M. Nobody',
        'date': '2012, May the 1st',
        'title': 'Does this book have a title ?'
    },
    'book/resume': (
        'This book is an ode to the passing time...'
        'A challenging thinking.'
    )
}
--- Standard "tree" dict ---
{
    'book': {
        'general': {
            'author': 'M. Nobody',
            'date': '2012, May the 1st',
            'title': 'Does this book have a title ?'
        },
        'resume': (
            'This book is an ode to the passing time...',
            'A challenging thinking.'
        )
    }
}
```


Searching for blocks
====================

Here we consider the following file whose path remains equal to `user/example.peuf`.

```
main::
    test::
        a = 1 + 9
        b <>  2
        c = 3 and 4

    sub_main::
        sub_sub_main::
            verb::
                line 1
                    line 2
                        line 3
```


The classes `Read` and `ReadBlock` allow to search for data blocks using queries on "querypaths". The special syntax to use tries to catch the best of the Python regex and the Unix-glob syntaxes. Take a look at the documentation of the function ``data.regexify`` for details. The following examples give some examples of queries.

```python
from pathlib import Path

from orpyste.data import Read

with Read(
    content = Path("user/example.peuf"),
    mode    = {
        "container"    : ":default:",
        "keyval:: = <>": "test",
        "verbatim"     : "verb"
    }
) as datas:
    for query in [
        "main/test",    # Only one path
        "**",           # Anything
        "main/*",       # Anything "contained" inside "main"
    ]:
        title = "Query: {0}".format(query)
        hrule = "="*len(title)

        print("", hrule, title, hrule, sep = "\n")

        for oneinfo in datas[query]:
            if oneinfo.isblock():
                print(
                    "",
                    "--- {0} [{1}] ---".format(
                        oneinfo.querypath,
                        oneinfo.mode
                    ),
                    sep = "\n"
                )

            else:
                for data_rtu in onedata.yrtu():
                    print(data_rtu)
```


This gives the following outputs as expected.

```
================
Query: main/test
================

--- main/test [keyval] ---
(4, 'a', '=', '1 + 9')
(5, 'b', '<>', '2')
(6, 'c', '=', '3 and 4')

=========
Query: **
=========

--- main/test [keyval] ---
(4, 'a', '=', '1 + 9')
(5, 'b', '<>', '2')
(6, 'c', '=', '3 and 4')

--- main/sub_main/sub_sub_main/verb [verbatim] ---
(11, 'line 1')
(12, '    line 2')
(13, '        line 3')

=============
Query: main/*
=============

--- main/test [keyval] ---
(4, 'a', '=', '1 + 9')
(5, 'b', '<>', '2')
(6, 'c', '=', '3 and 4')
```


Storing your datas in a `json` variable
=======================================

The class `ReadBlock` has a method `forjson` that allows to store your datas in a `json` file *(the storing has to be done by you)*. The following code will give us just after the structure used.

```python
from orpyste.data import ReadBlock

content = '''
main::
    test::
        a = 1 + 9
        b <>  2
        c = 3 and 4

    sub_main::
        sub_sub_main::
            verb::
                line 1
                    line 2
                        line 3
'''

with ReadBlock(
    content = content,
    mode    = {
        "container"    : ":default:",
        "keyval:: = <>": "test",
        "verbatim"     : "verb"
    }
) as datas:
    jsonobj = datas.forjson
    print(jsonobj)
```


Launched in a terminal, we obtain the following output which has been hand formatted. As you can see, we use the format `[key, value]` so as to store the keys and the values of the `python` dictionary given by the method `ReadBlock.flatdict` and `ReadBlock.recudict`. You can also note that for verbatim content we use a `null` key *(this is to ease other applications to extract informations from a "symmetric" `json` variable)*.

```json
[
    [
        [0, "main/test"],
        [
            [
                [0, "a"],
                {"nbline": 4, "sep": "=", "value": "1 + 9"}
            ],
            [
                [0, "b"],
                {"nbline": 5, "sep": "<>", "value": "2"}
            ],
            [
                [0, "c"],
                {"nbline": 6, "sep": "=", "value": "3 and 4"}
            ]
        ]
    ],
    [
        [0, "main/sub_main/sub_sub_main/verb"],
        [
            null,
            [
                {"nbline": 11, "value": "line 1"},
                {"nbline": 12, "value": "    line 2"},
                {"nbline": 13, "value": "        line 3"}
            ]
        ]
    ]
]
```


You can easily go back to the `python` dictionary thanks to the function `loadjson` that transforms one json variable stored in one string or in a file into a flat dictionary that is an instance of the class `ReadBlock.MKOrderedDict`.


How to use sections ?
=====================

The following partial snippet shows how to use sections which allow to work with virtual files containing classical `peuf` contents indicating by `...` here.

```
==
Section 1
==

...


==
Section 2 after the section 1
==

...
```


Above we have used minimal forms for naming sections using only two equal signs. You can use more signs and maybe you would prefer the following convention.

```
=========
Section 1
=========

...


=============================
Section 2 after the section 1
=============================

...
```


Working with this kind of `peuf` files needs to import `Read` or `ReadBlock` from `orpyste.section` instead of `orpyste.data`.


For querypaths and also json representations, the sections are indicated using brackets around their name.