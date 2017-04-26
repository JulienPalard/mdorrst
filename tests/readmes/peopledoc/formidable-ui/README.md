# Formidable-UI ![logo](https://raw.githubusercontent.com/novafloss/formidable-ui/master/formidable.png)

[![Build Status](https://travis-ci.org/novafloss/formidable-ui.svg?branch=master)](https://travis-ci.org/novafloss/formidable-ui)
[![CircleCI](https://circleci.com/gh/novafloss/formidable-ui.svg?style=shield&circle-token=eec96c2fd598c2f14fe55a4ee75801a20e0d6bb4)](https://circleci.com/gh/novafloss/formidable-ui)
[![LICENSE](https://img.shields.io/github/license/novafloss/formidable-ui.svg)](https://github.com/novafloss/formidable-ui/blob/master/LICENSE)

A form builder made with EmberJS and love, who will succeed to novaFormBuilder.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Node.js](https://github.com/nodesource/distributions) (with NPM)
* [Bower](http://bower.io/)
* [Ember CLI](http://ember-cli.com/)
* [PhantomJS](http://phantomjs.org/)

## Installation

* `git clone <repository-url>` this repository
* change into the new directory
* `npm install`
* `bower install`

## Running / Development

* `ember server`
* Visit your app at [http://localhost:4200](http://localhost:4200).

### Running Tests

* `ember test`
* `ember test --server`

### Building

* `ember build` (development)
* `ember build --environment production` (production)

### Integration

To integrate the app into your website, you have to include the production files:

```html
<link rel="stylesheet" href=".../vendor.css">
<link rel="stylesheet" href=".../formidable.css">

<script src=".../vendor.js"></script>
<script src=".../formidable.js"></script>
```

The app need a root element in the page with the id `formidable`:

```html
<div id="formidable"></div>
```

Then you can start the application easily with:

```html
<script>
  $(document).ready(function() {
      // Listen the valid.form event
      Formidable.on('valid.form', function(status) {
        // actions
      });
      Formidable.start({
        // options
      });
      // Send errors event
      Formidable.send('errors', {
        __all__: ["global error for the form"]
        fieldSlug1: ["error1", "error2"]
        fieldSlug2: ["error3"]
      });
  });
</script>
```

#### Functions

| Function | Description |
|----------|-------------|
| `start` | Start the application with options |
| `on` | Listen event from the application |
| `send` | Send an event to the application |

#### Start Options

| Option | Description | Info |
|--------|-------------| ---- |
| `formID` | The form ID to request | Required (or `formURL`, priority value) |
| `formURL` | The form URL to request | Required (or `formID`) |
| `component` | The page to display | `input` (by default) or `builder` |
| `translations` | The translations you want to use in the interface | english by default |
| `locale` | The locale you want to use in the interface | english by default |
| `namespace` | The namespace used for API calls | `api` by default |
| `host` | The host used for API calls | current base url by default |
| `googleAnalyticsKey` | Activate metrics by GoogleAnalytics | GoogleAnalytics key, deactivate by default |

#### Listen Events

| Event | Description |
|-------|-------------|
| `save.form` | When the data is going to be save |
| `saved.form` | When the data is saved |
| `errors.save.form` | Error(s) on form save |
| `cancel.form` | When the user wants to go back |
| `valid.form` | Boolean which says if the form is valid |

#### Send Events

| Event | Description |
|-------|-------------|
| `errors` | Add errors to the current form |

## Further Reading / Useful Links

* [ember.js](http://emberjs.com/)
* [ember-cli](http://ember-cli.com/)
* Development Browser Extensions
  * [ember inspector for chrome](https://chrome.google.com/webstore/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi)
  * [ember inspector for firefox](https://addons.mozilla.org/en-US/firefox/addon/ember-inspector/)

## Troubleshootings

* Watch error `ENOSPC`: See https://github.com/ember-cli/ember-cli/issues/1240
`echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p`

## Licence

MIT Licence
