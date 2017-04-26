Stellata
========

Stellata is a simple PostgreSQL ORM for Python 3.

Connecting
----------

To connect to a database on the default host/port with a threaded
connection pool of size 10:

::

    import stellata.database

    db = stellata.database.initialize(
        name='database',
        user='user',
        password='password',
        host='localhost',
        port=5432,
        pool_size=10
    )

Defining Models
---------------

A user model might look something like this:

::

    import stellata.fields
    import stellata.model

    class User(stellata.model.Model):
        __table__ = 'users'

        id = stellata.fields.UUID(null=False)
        active = stellata.fields.Integer(default=1)
        name = stellata.fields.Text(null=False)
        hash = stellata.fields.Varchar(length=255)
        email = stellata.fields.Text()
        dt = stellata.fields.Timestamp(null=False)

The ``__table__`` property is the name of the corresponding table in the
PostgreSQL database. Each property corresponds to a column, and the
classes in ``stellata.fields`` are used to define the column types.

Field Types
~~~~~~~~~~~

-  BigInteger
-  Boolean
-  Integer
-  Numeric
-  Text
-  Timestamp
-  UUID
-  Varchar

Relations
~~~~~~~~~

Like any good ORM, Stellata supports relations among models. Here are
two related models, ``A`` and ``B``:

::

    import stellata.model
    import stellata.fields
    import stellata.relations

    class A(stellata.model.Model):
        __table__ = 'a'

        id = stellata.fields.UUID()
        foo = stellata.fields.Text()
        bar = stellata.fields.Integer(default=0, null=False)

        b = stellata.relations.HasMany(lambda: B.A_id, lambda: A)

    class B(stellata.model.Model):
        __table__ = 'b'

        id = stellata.fields.UUID()
        a_id = stellata.fields.UUID()
        bar = stellata.fields.Integer(null=False)

        a = stellata.relations.BelongsTo(lambda: B.a_id, lambda: A)

Indexes
~~~~~~~

Indexes make your queries go fast. Let's add a couple indexes to our
table:

::

    import stellata.model
    import stellata.fields
    import stellata.index
    import stellata.relations

    class A(stellata.model.Model):
        __table__ = 'a'

        id = stellata.fields.UUID()
        foo = stellata.fields.Text()
        bar = stellata.fields.Integer(default=0, null=False)

        b = stellata.relations.HasMany(lambda: B.A_id, lambda: A)

        primary_key = stellata.index.PrimaryKey(lambda: A.id)
        foo_index = stellata.index.Index(lambda: A.foo, unique=True)

Migration
---------

Once you've defined your models, you can sync them with your database by
performing a migration.

::

    stellata.schema.migrate(db, execute=True)

Here, ``db`` is the handle returned by the
``stellata.database.initialize`` call. If you'd like to do a dry run,
without actually executing any queries, do:

::

    stellata.schema.migrate(db)

In both cases, this function will return a list of queries needed for
the migration.

Resetting
~~~~~~~~~

In some development scripts, you might want to clean your database. If
you so desire, you can do this:

::

    stellata.schema.drop_tables_and_lose_all_data(db, execute=True)

As its name suggests, this function is very destructive, so don't do
this on a production database.

CRUD Operations
---------------

Finally, let's walk through how to use Stellata to query your database.

Create
~~~~~~

Let's create a new instance of ``A``.

::

    a = A.create(A(foo='bar', bar=5))
    a.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca'
    a.foo == 'bar'
    a.bar == 4

Or, if we want to create in bulk:

::

    result = A.create([
        A(foo='bar', bar=6),
        A(foo='baz', bar=7)
    ])

    len(result) == 2

If you created a unique index on some fields, you can take advantage of
the PostgreSQL ON CONFLICT feature:

::

    A.create(A(foo='baz', bar=9), unique=(A.foo,))

Now, if there's already a row with ``foo`` having a value of ``baz``,
then the ``bar`` column will be updated to have a value of ``9``, rather
than creating a new row.

Read
~~~~

To read from the database, we'll want to use the ``where`` method. Let's
get the instance of ``A`` we created before:

::

    a = A.where(A.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca').get()
    a.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca'

Jeez Rick, what's that syntax? We're using operator overloading, Morty.
What else can we do?

::

    A.where(A.bar < 5).get()
    A.where(A.bar > 1).get()
    A.where(A.id << ['2a12f545-c587-4b99-8fd2-57e79f7c8bca', '31be0c81-f5ee-49b9-a624-356402427f76']).get()

That last one is a where in query, in case that wasn't burp obvious. We
can also use AND and OR in our queries like so:

::

    A.where((A.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca') | (A.bar < 5)).get()
    A.where((A.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca') & (A.bar > 1)).get()

Finally, we can use those relations we set up earlier with joins. Let's
say we create the following:

::

    a = A.create(A(foo='bar', bar=5))
    a.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca'
    b = B.create([
        B(a_id='2a12f545-c587-4b99-8fd2-57e79f7c8bca', qux=3)
        B(a_id='2a12f545-c587-4b99-8fd2-57e79f7c8bca', qux=5)
    ])

Now, we can do this:

::

    a = A.join(A.b).where(A.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca').get()
    a.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca'
    len(a.b) == 2
    a.b[0].qux == 3
    a.b[1].qux == 5

Or, the other way:

::

    b = B.join(B.a).where(B.qux << [3, 5]).get()
    len(b) == 2
    b[0].qux == 3
    b[0].a.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca'
    b[1].qux == 5
    b[1].a.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca'

By default, joins will be executed via multiple SELECT queries. If you'd
prefer to do a JOIN instead, just do this:

::

    a = A.join_with('join').join(A.b).where(A.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca').get()

The result is the same as before, but the underlying query was
different. Which method you use is entirely up to you, and may vary with
different queries.

Update
~~~~~~

As you might expect, update queries combine the syntax for creating and
reading:

::

    A.where(A.id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca').update(A(bar=7))

Delete
~~~~~~

This one is easy now.

::

    A.where(id == '2a12f545-c587-4b99-8fd2-57e79f7c8bca').delete()
