# http\_api\_exporter

This is a very simple http server lib designed to export APIs in python.

The lib is based on tornado.

## Usage

```
from http_api_exporter import ApiHttpServer #import the class

def function():                    #define the functions you want to export
    ...
```

Then you have two choices to bind the server with functions.

```
app = ApiHttpServer({"RouteName" : function})
app.start()

or

app = ApiHttpServer()
app.bind("RouteName", function)
app.start()
```

Finally, you have two ways to pass the args.

```
{                                   #pass the args as a list named "Input"
   Input: [args] 
}

{                                   #pass the args as a dict
    arg: value,
    arg0: value,
    ...
}

{                                   #combine both
    Input: [args],
    arg0: value,
    ...
}
```

if your function return multiple results, the results will be wrapped into a list.

## API

__ApiHttpServer.\_\_init\_\_(functionDict = dict(), WelcomePage = "Python APIs are providing.") :__

initialize an instance.
    
&emsp;&emsp;args __:__

&emsp;&emsp;&emsp;functionDict __:__ A dictionary which is composed by "RouteName" as keys and functions as values.

&emsp;&emsp;&emsp;WelcomePage __:__ A string that allow you modify the welcome page, which can be visited at the root route('\\').

<br />

__ApiHttpServer.bind(self, route = None, function = None, dict = None) :__

Bind the function.
    
&emsp;&emsp;args __:__

&emsp;&emsp;&emsp;route __:__ The route to call the corresponding function.

&emsp;&emsp;&emsp;function __:__ The corresponding function.

&emsp;&emsp;&emsp;diction __:__ If "dict" is not none, then the "route" and the "function" will be ignored. And unfold the dict that keys as routes and values as functions.

<br />

__ApiHttpServer.start(port = 80) :__

Start the server.
    
&emsp;&emsp;args __:__

&emsp;&emsp;&emsp;port __:__ Choose which port to listen on.

## Attention

Not every data structure could be jsonified. So the results your function returns must be hashable.

There is a list of hashable structures as I know:

````
int
float
str
list
dictionary
````

## What's more

### DONE

bind the functions to routes.

return multiple results.

makes it possible to pass dictionary args.

### TODO

anything else if anyone need.