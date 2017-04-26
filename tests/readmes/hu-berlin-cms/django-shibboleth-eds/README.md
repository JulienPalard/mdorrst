# django-shibboleth-eds
app to embed [shibboleth embedded discovery service (eds)][1] into a django project.

# install

1. Install the app (i.e. by using pip)
2. add it to `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS += (
        'shibboleth_eds',
    )
    ```
    
3. Add it to `urls.py`:

     ```python
    urlpatterns += [
        url(r'^ds/', include('shibboleth_eds.urls', namespace='shibboleth_eds')),
    ]
    ```
    
4. Run `manage.py collectstatic`.

# configure

Adjust the template `discovery.html` to fit into your project. Modify the settings found in `views.py` according to your needs.

[1]: http://shibboleth.net/products/embedded-discovery-service.html "Shibboleth Embedded Discovery Service"
