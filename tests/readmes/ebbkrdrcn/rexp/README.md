# RexP

Simple Pattern Compiler Library

```python
pip install rexp
```

```python
import re
from rexp.patterns import DEFAULT_PATTERN_SET
from rexp.compiler import PatternCompiler

if __name__ == '__main__':
    log = 'GET /api/v1/sources?$filter=Id%20eq%20oid%27507f191e810c19729de860ea%27 HTTP/1.1'
    
    compiler = PatternCompiler(pattern_set=DEFAULT_PATTERN_SET)
    compiler.register(pattern_set=dict(
        HTTP_VERB=r'(GET|POST|PUT|DELETE)'
    ))
    
    expr = compiler.compile(
        pattern='$1{HTTP_VERB} $2{RE(.+)} HTTP/$3{NUM}',
        capture_names=[
            'http_verb',
            'relative_url',
            'http_ver'
        ])
        
    m = re.search(expr, log)
    result = m.groupdict()
    print result

    assert result == {
        'http_verb': 'GET',
        'relative_url': '/api/v1/sources?$filter=Id%20eq%20oid%27507f191e810c19729de860ea%27',
        'http_ver': '1.1'
    }
````

#


