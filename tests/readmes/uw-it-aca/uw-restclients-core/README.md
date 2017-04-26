[![Build Status](https://api.travis-ci.org/uw-it-aca/uw-restclients-core.svg?branch=master)](https://travis-ci.org/uw-it-aca/uw-restclients-core)
[![Coverage Status](https://coveralls.io/repos/uw-it-aca/uw-restclients-core/badge.png?branch=master)](https://coveralls.io/r/uw-it-aca/uw-restclients-core?branch=master)

uw-restclients-core
===================

This module provides useful interfaces for webservice clients.

If you're writing an application that includes mock resource files, you'll want to include code like this somewhere in your application's startup process:

```
from restclients_core.dao import MockDAO
import os
custom_path = os.path.join(abspath(dirname(__file__), "app_resources"))
MockDAO.register_mock_path(custom_path)
```

For more information, see https://github.com/uw-it-aca/uw-restclients-core/wiki/Mock-resources

If you're writing a webservice client, here is some documentation: https://github.com/uw-it-aca/uw-restclients-core/wiki/Writing-a-webservice-client

If you want to contribute, please send a pull request to the develop branch, or submit an issue.
