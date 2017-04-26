## Django Multitenant ##

[![PyPi](https://img.shields.io/pypi/v/djangomultitenant.svg)](https://pypi.python.org/pypi/djangomultitenant/) [![License](https://img.shields.io/pypi/l/djangomultitenant.svg)](https://github.com/akhilputhiry/djangomultitenant/blob/master/LICENSE.txt) 

This app can be used to implement multitenant architecture within your django project very easily.

Inorder to install the app


```
pip install djangomultitenant
```


Modify the project settings file as shown below


```
DATABASES = {
    'default': {

    },
    
    # DB for tenant 1
    'akhil': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'akhil.sqlite3'),
    },
    
    # DB for tenant 2
    'nikhil': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'nikhil.sqlite3'),
    }
}

INSTALLED_APPS = [
    'djangomultitenant',
]

DATABASE_ROUTERS = [
    'djangomultitenant.Router',
]

MIDDLEWARE = [
    'djangomultitenant.Middleware',  # this has to be the first one
]
```

Use the TENANT-CODE header in all your requests to the django project. You can use [requestly](https://chrome.google.com/webstore/detail/requestly/mdnleldcmiljblolnjhpnblkcekpdkpa?hl=en) to send the headers while accessing project. In the production environment, these headers can be configured in the webservers.

```
TENANT-CODE: akhil
```

Tada !!! You are all equipped with multitenancy !!!

Note: migrations and management commands are not handled by this app. so please dont forget to use --database 
