# ckenchanter

Extends the [PyEnchant](http://pythonhosted.org/pyenchant/) library to parse requests from [CKEditor's](http://ckeditor.com) SCAYT spellchecker plugin and return suggested corrections using standard language dictionaries and custom personal word lists. Use it to run your own lightweight spellchecking server.

## Installing

Install to your virtualenv or globally using [pip](https://pip.pypa.io/en/stable/installing/).

```
pip install ckenchanter
```

## Client side configuration

To begin you'll need to add the following lines to your CKEditor `config.js` file. Update the values to reflect your app settings.
```JavaScript
config.scayt_autoStartup = true;
config.scayt_servicePath = '/spellcheck/';
config.scayt_serviceHost = 'localhost';
config.scayt_servicePort = '8005';
config.scayt_serviceProtocol = 'http';
```

This can also be done when CKEditor is initialized in your app through the global `CKEDITOR` object.

The `config.scayt_servicePath` endpoint should submit the request data to a CKEnchanter object and return it's response. Here is an example [Flask](http://flask.pocoo.org/) route:


## Usage on server


```Python
from ckenchanter import CKEnchanter

@views.route('/spellcheck/', methods=['POST'])
def spellcheck():
    """
    Sends a line of text to the ckenchanter module
    """
    cke = CKEnchanter()
    response = cke.parse_ckeditor_request(request.data)
    return jsonify(response)
```

CKEnchanter accepts all arguments supported by PyEnchant's [SpellChecker class](https://github.com/rfk/pyenchant/blob/master/enchant/checker/__init__.py). It has an additional named arg `wl_path` that accepts the absolute path of a custom word list (.txt file) for CKEnchanter to use in addition to the default dictionary.

```Python
import os
from ckenchanter import CKEnchanter

@views.route('/spellcheck/', methods=['POST'])
def spellcheck():
    """
    Sends a line of text to the ckenchanter module
    """
    file_dir = os.path.dirname(__file__)
    word_list_path = os.path.join(file_dir, "dicts/mywords.txt")

    cke = CKEnchanter(wl_path=word_list_path)
    response = cke.parse_ckeditor_request(request.data)
    return jsonify(response)
```

That's it! CKEnchanter will extract the text from CKEditor's request string and run it through PyEnchant, returning a list of suggestions formatted for SCAYT. Enjoy!
