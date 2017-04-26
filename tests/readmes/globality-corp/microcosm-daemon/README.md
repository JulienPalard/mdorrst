# microcosm_daemon

Asynchronous workers using a state machine.


[![Circle CI](https://circleci.com/gh/globality-corp/microcosm-daemon/tree/develop.svg?style=svg)](https://circleci.com/gh/globality-corp/microcosm-daemon/tree/develop)


## Conventions

 -  A state machine calls a single-argument worker function in a loop:

        def func(graph):
            pass

        state_machine = StateMachine(graph, func)
        state_machine.run()

 -  A worker function can return another callable to cause a state transition:

        def next_func(graph):
            pass

        def func(graph):
            return next_func

 -  A worker function can raise `SleepNow` to cause the state machine to sleep
    before processing itself again:

        def func(graph):
            raise SleepNow

 -  A worker function can raise an exception. By default, all exceptions except
    `FatalError` are swallowed by the state machine's error handler although the
    state machine can be made to fail fast by configuring the error policy to be
    strict.
