==============================
Peek Platform - Worker Service
==============================

The Peek Worker service provides peek apps with distributed multiprocessing support.
This is provided with Celery.

See http://www.celeryproject.org

.#  Ability to farm out computationally expensive tasks to a cluster, or at least
    multiple threads.

.#  The workers get their own connection to the DB in their own fork.