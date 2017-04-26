xunit-python-decorator
======================

Easily decorate python functions with a ``with`` statement.

Turn

::

    import time

    start = time.time()
    try:
        # your code
        1 / 0
    except Exception, e:
        errMsg = str(e)
        errTb = traceback...

    end = time.time()
    # add xunit test case with formatted error string + timing data

into

::

    with xunit('name', 'tests.') as tc1:
        1 / 0

    ts = xunit_suite('My Suite', [tc1])
    print(xunit_dump([ts]))

LICENSE
-------

GPL-3.0
