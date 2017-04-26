## poolhub

<i>Track threads in your Python program.</i>

<p align="center">
    <img src="https://raw.githubusercontent.com/tsarpaul/poolhub/master/poolhub.png" alt="poolhub demo">
</p>

#### Installation
poolhub is only compatible with Python 3
> pip install poolhub

#### Usage
```
import poolhub
```

Once you run your program, the web browser will open.

To set name and status in your thread:
```
t = threading.Thread(name="Thread no. 1", status='Initializing thread', target=func)
```

To update your thread's status:
```
t = threading.current_thread()
t.status = "Reporting in for duty"
```

<hr>

When you terminate a thread, this raises a 
`KeyBoardInterrupt` inside the thread to terminate it.
