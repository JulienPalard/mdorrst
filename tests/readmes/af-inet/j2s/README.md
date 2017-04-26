# j2s

json to swagger definition

reads json from STDIN, and writes swagger-like json to STDOUT

## install

```
pip install j2s
```

## use case

`j2s` is most useful when you're writing a swagger definition for an already existing API.

## usage

```
curl "http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC" | j2s
```

