# Marguerite

Marguerite provides a declarative, consistent accessor to data layer.

---

# Dependencies
* Python 2.7 or later
* Werkzeug 0.12.7 or later

# Installation
```bash
$ pip install Marguerite
```

# Usage Flow.
Install requests as an example.

```bash
$ pip install requests
```

1. define data layer accessor, and writen access structure
```python
from marguerite import AbstractStructure, AbstractAccessor, Order
from marguerite.accessors import bind

class Accessor(AbstractAccessor):
    def prepare(self, name, value):
        order = self.structure.get_order(name)
        return bind(order, value)

    def create(self, name, value):
        order = self.prepare(name, value)
        return requests.post(order).json()

    def get(self, name, value={}):
        order = self.prepare(name, value)
        return requests.get(order).json()


class UserStructure(AbstractStructure):
    __accessor__ = Accessor

    orders = Order(
        user = "https://example.com/users/:id",
        create = "https://example.com/users/:id?=username=:username"
    )
```

2. get data layer accessor object
```python
from marguerite import Marguerite

marguerite = Marguerite()
accessor = marguerite.get_accessor("path.to.UserStructure")
```

3. fetch data
```python
# execute get logic
result = accessor.get("user", { "id": 1 })
print(result) # {"id": 1, "username": "john"...}

# execute post logic
result = accessor.create("user", { "id": 2, "username": "marguerite" })
print(result) # {"status": "success", {"result": {"id": 2, "username": "marguerite"...}}}
```

# LICENSE
Apache License 2.0
