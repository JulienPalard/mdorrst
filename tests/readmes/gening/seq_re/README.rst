2-dimensional Sequence Regular Expression (SEQ RE)
==================================================

This module provides regular expression matching operations over a sequence of tuples
(or a sequence of sequence) data structure. It looks like the following::

    seq_m_n = [[str_11, str_12, ... str_1n],
               [str_21, str_22, ... str_2n],
                ...,
               [str_m1, str_m2, ... str_mn]]

The sequence is a homogeneous 2D array, that is a matrix with m rows and n columns.
In practice, m maybe vary from sequence to sequence, while n is usually a fixed-size.

A element in the tuple of the sequence can be considered as either a string, a word, a phrase,
a char, a flag, a token or a tag, and maybe a set of tags or values (multi-values) in the future.

To match a pattern over a sequence of tuples,
the SEQ RE patterns is written like one of the examples::

    ([;;PERSON]+) [was|has been] [an]? .{0,3} ([^painter|drawing artist|画家])

    (?P<name@0,1,2>[;;PERSON]) [;VERB be;] [born] [on] (?P<birthday@0:3>([;;NUMBER|MONTH]|[-]){2,3})


1. The syntax of SEQ RE pattern
-------------------------------

A SEQ RE pattern is very similar to the ordinary regular express (RE) used in Python,
in which the delimiters ``[...]`` is to indicate a tuple -- the second dimension of the sequence.

1.1 Inside ``[...]``
++++++++++++++++++++

- ``[`` and ``]``

  is the beginning and end delimiter of the tuple, e.g. ``[...]``.

- ``;``

  separates each element which the tuple contains,
  and the continuous ``;`` at the tail can be omitted,
  e.g. ``[A|B;X;;]``, ``[A|B;X]``.

- ``|``

  indicates the different values of one element, e.g. ``A|B``.
  These values form a set, and any string in the set will be matched,
  e.g. ``A|B`` will match ``A`` or ``B``.

- ``^``

  be the first character of an element,
  all the string that are not in the value set of this element will be matched.
  And ``^`` has no special meaning if it’s not the first character of the element.
  If ``^`` comes the first character of an element but it is a part of a literal string,
  ``\^`` should be used to escape it.

- The priority of above-mentioned operations:

  ``[`` ``]`` < ``;`` < ``^`` (not literal) < ``|`` < ``^`` (literal) .

- ``\``

  is an escaping symbol before aforementioned special characters.
  Characters other than ``]``, ``:`` or ``\`` lose their special meaning inside ``[...]``.
  To express ``]``, ``:`` or ``|`` in literal, ``\`` should be added before ``]``, ``:`` or ``|``.
  Meanwhile, to represent a literal backslash ``\`` before ``]``, ``;`` or ``|``,
  ``\\`` should be used in the plain text
  that is to say ``'\\\\'`` must be used in the Python code.

1.2 Outside ``[...]``
+++++++++++++++++++++

- The special meanings of special characters in the ordinary RE are available here,
  but with the limitations discussed below.

  1. **Not** support ``[`` and ``]`` as special characters to indicate a set of characters.

  2. **Not** support the following escaped special characters:
     ``\number``, ``\A``, ``\b``, ``\B``, ``\d``, ``\D``, ``\s``, ``\S``,
     ``\w``, ``\W``, ``\Z``, ``\a``, ``\b``, ``\f``, ``\n``, ``\r``, ``\t``, ``\v``,
     ``\x``.

  3. **Not** support ranges of characters,
     such as ``[0-9A-Za-z]``, ``[\u4E00-\u9FBB\u3007]`` (Unihan and Chinese character ``〇``)
     used in ordinary RE.

  4. The whitespace and non-special characters are ignored.

- ``.`` is an abbreviation of an arbitrary tuple ``[]`` or ``[;]``.

- The named groups in the pattern are very useful.
  As an extension, a format string starting with ``@`` can be followed after the group name,
  to describe which element of the tuples belonging this group will be output as the result.
  For example: ``(?P<name@d1,d2:d3>...)``,
  in which ``d1``, ``d2`` and ``d3`` are all 0-based position index number of elements in the tuple.

  1. ``@0,2:4`` means in the matched result only the 0th
     and from 2nd to 3rd elements of tuples will be output.

  2. ``@@`` means the pattern of the group itself will be output other than the matched result.
     one can choose whether to include the group name and parentheses or not.

  3. ``@`` means all elements of tuples in the matched result will be output.

1.3 Boolean logic in the ``[...]``
++++++++++++++++++++++++++++++++++

Given a sequence of 3-tuple ``[[s1, s2, s3], ... ]``,

- AND

  ``[X;;Y]`` will match ``s1`` == ``X`` && ``s3`` == ``Y``.
  Its behavior looks like the ordinary RE pattern ``(?:X.Y)``.

- OR

  ``[X;;]|[;;Y]`` will match ``s1`` == ``X`` || ``s3`` == ``Y``.
  Its behavior looks like the ordinary RE pattern ``(?:X..)|(?:..Y)``

- NOT

  If ``[;^P;]`` will match ``s2`` != ``P``.
  Its behavior looks like the ordinary RE pattern ``(?:.[^P].)``.

  We can also use a negative lookahead assertion of the ordinary RE,
  to give a negative covering its following.
  e.g. ``(?![;P;][Q])[;;][;;]`` <==> ``[;^P;][^Q;;]``,
  which behavior looks like the ordinary RE pattern ``(?!(?:.P.)(?:Q..))...``.

2. Notes
--------

**Not** support comparing the number of figures.

Multi-values of one element is not supported now, but this feature may be improved in the future.

Although SEQ RE has sufficient ability to express a pattern over sequences of tuples,
it is still not a cascaded regular expressions (see also: `Stanford TokensRegex
<https://nlp.stanford.edu/software/tokensregex.html>`_).


3. Examples
-----------

The usage of seq_re module::

    from __future__ import print_function
    import seq_re

    n = 3
    pattern = ('(?P<name@0>[;;PERSON]+) [is|was|has been] [a|an]? '
               '(?P<attrib@0,1>.{0,3}) ([artist])')
    seq = [['Vincent van Gogh', 'NNP', 'PERSON'],
           ['was', 'VBD', 'O'],
           ['a', 'DT', 'O'],
           ['Dutch', 'JJ', 'O'],
           ['Post-Impressionist', 'NN', 'O'],
           ['painter', 'NN', 'OCCUPATION'],
           ['who', 'WP', 'O'],
           ['is', 'VBZ', 'O'],
           ['among', 'IN', 'O'],
           ['the', 'DT', 'O'],
           ['most', 'RBS', 'O'],
           ['famous', 'JJ', 'O'],
           ['and', 'CC', 'O'],
           ['influential', 'JJ', 'O'],
           ['figures', 'NNS', 'O'],
           ['in', 'IN', 'O'],
           ['the', 'DT', 'O'],
           ['history', 'NN', 'O'],
           ['of', 'IN', 'O'],
           ['Western art', 'NNP', 'DOMAIN'],
           ['.', '.', 'O']]
    placeholder_dict = {'artist': ['painter', 'drawing artist']}

    sr = seq_re.SeqRegex(n).compile(pattern, **placeholder_dict)
    match = sr.search(seq)
    if match:
        for g in match.group_list:
            print(' '.join(['`'.join(tup) for tup in g[1]]))
        for name in sorted(match.named_group_dict,
                           key=lambda gn: match.named_group_dict[gn][0]):
            print(name, match.format_group_to_str(name, True))

