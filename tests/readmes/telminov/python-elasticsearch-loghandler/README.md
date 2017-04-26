# python-elasticsearch-loghandler
Python elasticsearch log handler

## Django config
```
LOGGING = {
    'version': 1,
    ...
    'handlers': {
        ...
        'elastic': {
            'class': 'es_loghandler.handlers.ElasticHandler',
            'hosts': [{'host': 'localhost', 'port': 9200}],
        },
        ...
    },
    'loggers': {
        ...
        'app.name': {
            'handlers': ['elastic'],
            'level': 'INFO',
        },
        ...
    }
}

```