### Wrapper for optunity optimisation

##### Enhanced format for search_space

* int (numbers without decimal point)
* bool
* list of strings
* fixed (single keys or single values)
* logspace e.g.[0,3] selects x=0-3 and then 10**x
    
##### Replaces log with runs object

* saves each iteration so resilient to crash or manual interrupt
* shows plots by parameter