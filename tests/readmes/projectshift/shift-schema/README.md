[![Build Status](https://api.travis-ci.org/projectshift/shift-schema.svg)](https://travis-ci.org/projectshift/shift-schema)
[![Coverage Status](https://coveralls.io/repos/projectshift/shift-schema/badge.svg?branch=master)](https://coveralls.io/r/projectshift/shift-schema?branch=master)
# shift-schema


Filtering and validation library for Python3. Can filter and validate data in 
model objects and simple dictionaries with flexible schemas. 

Main idea: decouple filtering and validation rules from web forms into
flexible schemas, then reuse those schemas in forms as well as apis and cli. Model validation and filtering rules should be part of the model and your domain logic, not your views or forms logic.

## model:

You can use any kind of object or a dictionary as your model.
If you use filtering model will be changed in-place by applying 
the filters you define. 

## schema:


Schema is a collection of rules to filter and validate properties of your
model (object or dictionary). There are several ways to create a schema
most nice being by subclassing `Schema` object:


```python
from shiftschema.schema import Schema
from shiftschema import validators as validator

class MySchema(Schema):
    def schema(self):
        self.add_property('name', required=True)
        self.name.add_validator(validator.Length(min=3, max=100))
        
        self.add_property('email')
        self.email.add_validator(validator.Email)

schema = MySchema()
```

Or alternatively you can pass spec dictionary to constructor:

```python
from shiftschema.schema import Schema
from shiftschema import validators as validator

schema = Schema({
    'properties': {
        'name' = dict(
            required=True,
            validators = [validator.Length(min=3, max=100)]
        ),
        'email' = dict(
            validators = [validator.Email()]
        )    
    }
})
```




## validation:

You can then use this schema to filter and validate your model data, or `process` it (filter and validate as single operation).
To validate a model pass it to your schema and get back `Result`:

```python
model = dict(name=None, email='BAD')
valid = schema.process(model)
print(valid == True) # False - validaation failed
print(valid.errors) # errors: name='Required', email='Invalid'
```

There is a number of common validators provided and you can easily plug your own.

## filtering:

You can attach filters to your schema. Those will be applied in turn and update model data in-place before doing any validations.

```
person = Person(name='   Morty   ', birthyear = 'born in 1900')
schema = Schema({
    'properties': {
        'name': dict(
            filters: [Strip()]
        ),
        'birthyear': dict(
            filters: [Digits(to_int=True)]
        )
    }
})

print(person.name) # 'Morty' (stripped of spaces)
print(person.birthyar) # 1900 (int)
```

As with validators there are some filters provided and you can easily plug your own.

## errors are objects:

Validation on a model gets you a `Result` objects that evaluates to boolean
`True` or `False` depending on if it was valid or not:

```python
valid = schema.validate(model) # return shiftschema.result.Result
bool(valid) # True if valid, False otherwise
```

All the errors the result contains are `Error` objects that 
simple validators (like `Length`)return. You can easily get those errors as string 
messages with:

```python
errors_dict = result.get_messages()
```

All errors are translated, so you can have them in any language supported
by passing a locale (defaults to 'en'):

```python
errors_dict = result.get_messages(locale='en') # translate to locale
```

## translation:

You can pass `translator` and `locale` to `Result` object manually but
the most easy way to use translations is through globally available
`Translator` that exists on the `Schema`. Schemas will inject this translator
and locale in to result objects they create. So you can simply:

```python
from shiftschema.schema import Schema

Schema.translator # preconfigured with default translations
Schema.translator.add_.location(path) # but you can add your own
Schema.locale # is 'en' by default
Schema.locale = 'ru' # but you can change that
```

After setting those you will get errors by default in Russian with
your custom translations loaded.

```python
valid = schema.validate(model)
if not valid:
    valid.get_messages() # in russian per global setting
    valid.get_messages(locale='en') # or whatever you specify
```

## provided filters:

There is a number of implemented filters already and we are constantly adding more. You also can implement your own by extending from `AbstractFilter` class. Currently the follwing filters are provided:

##### Digits
Removes everything from the string leaving just the digits and optionally converts result to integer.

##### Lowercase
Converts incoming string to lowercase. If incoming data is not a string it will be converted to one implicitly.

##### Strip
Removes spaces, newlines or any specified characters either from fron, back or both sides of a string.

##### Uppercase
Converts incoming string to uppercase. If incoming data is not a string it will be converted to one implicitly.


## provided validators:

##### Choice
Checks if provided value exists in an iterable of valid choices provided to constructor.

##### Digits
Validates that passed value consists only of digits.

##### Email
Validates that passed in value is a valid email. The check is regex only so we don't do any deep MX checks here

##### Length
Validates an input for being proper length. You can check for minimum length, maximum length or both.


## flask wtforms extension:

Extension allows you to use schemas to validate wftforms in flask applications. Forms can represent full model data or just a smaller subset of your model. Both filtering and validation will be applied to form data according to rules defined in schema.
And you can mix wtf validation with schema validation. Here is a usage typical pattern:

```python
from shiftschema.ext.flask_wtf import Form
from shiftschema.schema import Schema
from shiftschema import validators, filters
from wtforms import StringField, PasswordField

# extend your form from provided mixin
class UserForm(Form):
    """ User form used for creating new users """
    username = StringField('username')
    email = StringField('email')
    password = PasswordField('password')
    
# define a schema
class UserSchema(Schema):
    """ User model filtering and validation schema"""
    def schema(self):
        self.add_property('username', required=True)
        self.username.add_filter(filters.Strip())
        self.username.add_validator(validators.Length(min=3, max=200))

        self.add_property('email', required=True)
        self.email.add_filter(filters.Strip())
        self.email.add_validator(validators.Length(min=3, max=200))
        self.email.add_validator(validators.Email())

        self.add_property('password', required=True)
        self.password.add_validator(validators.Length(min=3, max=200))		
```

You can now use chema to validate and filter form data in your views. The usage is similar to regular forms and workflow:

```python
@app.route('/register/', methods=['GET', 'POST'])
def register_view(self):
    # just remember to tell the form what schema to use
    form = UserForm(schema=UserSchema())
    if form.validate_on_submit():
        user = User(
            username=form.username.data, 
            email=form.email.data, 
            password=form.password.data
        )
        user_service.save(user)
        return redirect(url_for('thank.you'))
        
    return render_template('user/register.html')
```








