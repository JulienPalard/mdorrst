=============================
Object-like Entrypoint Access
=============================

.. image:: https://travis-ci.org/klmitch/entrypointer.svg?branch=master
    :target: https://travis-ci.org/klmitch/entrypointer

The ``setuptools`` package provides a handy feature known as
"entrypoints".  An entrypoint is a named reference to a Python object,
such as a function, class, or value, which other packages can
reference using the entrypoint group and name.  These are useful for
creating extendable Python projects, as one project can create
entrypoints that will be used as hooks or plugins by another project.
However, making use of entrypoints is rather awkward; ``setuptools``
provides the ``pkg_resources.iter_entry_points()`` function, which
iterates through the defined entrypoints, but the caller must still
load the entrypoint, which could possibly result in some errors which
must be caught so the next entrypoint with the given name can be
tried.

This package provides an alternative interface to entrypoints which
eliminates this boilerplate, is easier to use, and also speeds up
repetitive access to specific entrypoints.  This is done through the
creation of dictionary-like and list-like objects to represent
entrypoint groups and lists of loaded entrypoints.  A special object,
``eps``, is also provided that allows reference to an entrypoint group
via simple attribute access.

Looking Up an Entrypoint
========================

We'll begin with an example.  Let's say your application looks for an
entrypoint named "hook" in the entrypoint group
"example_app.example_group".  This can be as simple as::

  hook = entrypointer.eps.example_app.example_group['hook']

If the named entrypoint doesn't exist, this will raise a ``KeyError``,
but you can use the ``get()`` method to return something else
instead::

  hook = entrypointer.eps.example_app.example_group.get('hook')

For a hook method, your application may actually prefer to call all
defined hooks.  This can be accomplished like so::

  for hook in entrypointer.eps.example_app.example_group.get_all('hook', []):
      hook('calling your hook')

Some applications may wish to use entrypoint group names that happen
to not be valid Python identifiers, e.g., "Example App.Example
Group".  This can be accomplished with a simple ``getattr()`` call on
``entrypoint.eps``::

  group = getattr(entrypointer.eps, 'Example App.Example Group')

The only restriction on a group name is that no component can start
with a leading underscore ('_').

Using Entrypoints without ``entrypointer.eps``
==============================================

The ``entrypointer.eps`` object is provided for convenience; it is not
required to be used.  To obtain a dictionary-like object for an
entrypoint group, simply instantiate the
``entrypointer.EntrypointDict`` class::

  group = entrypointer.EntrypointDict('example_app.example_group')
  hooks = group.get_all('hook')

This class provides all of the basic ``dict`` methods, such as
``keys()`` and ``values()``.  It also provides variants, such as
``items_all()``, which yield list-like objects of entrypoints.  This
allows use of entrypoints for a wide variety of effects, such as the
"hook" pattern demonstrated above, or for extending commands your
application makes available, or for a variety of other uses.

Obtaining a List of Entrypoints
===============================

Although it is recommended to use the ``entrypointer.EntrypointDict``
class for accessing entrypoints, it is possible to use the list-like
object, ``entrypointer.EntrypointList``, directly.  It is instantiated
with the entrypoint group name and the name of the entrypoint itself,
e.g.::

  hooks = entrypointer.EntrypointList('example_app.example_group', 'hook')

Efficiency Considerations
=========================

The ``pkg_resources.iter_entry_points()`` function is somewhat slow.
The ``entrypointer.EntrypointList`` and
``entrypointer.EntrypointDict`` classes are designed to call it as few
times as possible and cache the results for future use.  Further, they
are optimized for the common case of using the first entrypoint with a
given name; they stop loading entrypoints after the first one that
loads successfully.  Finally, these classes do their work lazily,
calling ``pkg_resources.iter_entry_points()`` only when necessary to
implement the method being called.  This causes the expense of using
entrypoints to be amortized over the lifetime of the application,
while still maintaining a high speed due to the caching.  However, one
side effect of this caching is that changes to the installed packages
that would be picked up by calling
``pkg_resources.iter_entry_points()`` will not be detected when using
``entrypointer``; if this is important to your application, you may
want to call the ``entrypointer.EntrypointDict`` and
``entrypoint.EntrypointList`` classes directly and discard them when
you are done; note that this will reduce the efficiency, as they will
need to call ``pkg_resources.iter_entry_points()`` more frequently.
