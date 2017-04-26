# skillful

[![PyPIVersion](https://img.shields.io/pypi/v/skillful.svg)](https://pypi.python.org/pypi/skillful)
[![BuildStatus](https://travis-ci.org/bmweiner/skillful.svg?branch=master)](https://travis-ci.org/bmweiner/skillful)
[![Coverage](https://coveralls.io/repos/github/bmweiner/skillful/badge.svg?branch=master)](https://coveralls.io/github/bmweiner/skillful?branch=master)

*A Python package for building Amazon Alexa skills.*

## Features

* Request and response objects for [custom skills](https://goo.gl/JpVGm4)
* Simple definition of response logic for each request type
* Built-in request parsing/validation, intent dispatch, and response
  construction

## Installation

    pip install skillful

## Example

    import skillful
    from skillful.tests import data

    application_id = 'amzn1.echo-sdk-ams.app.000000-d0ed-0000-ad00-000000d00ebe'
    skill = skillful.Skill(application_id)

    @skill.launch
    def on_launch():
        print('Launched: {}'.format(skill.request.session.session_id))
        text = 'Welcome to skillful. Would you like to build an Alexa skill?'
        skill.response.set_speech_text(text)
        ssml = ('<speak>Please tell me if you would like to build an Alexa '
                'skill.</speak>')
        skill.response.set_reprompt_ssml(ssml)

    @skill.intent('yes')
    def on_intent_yes():
        text = ('Great! Building Alexa skills is easy with skillful. Open '
                'the Alexa app to see more information on skillful, a '
                'Python package for building Alexa skills.')
        skill.response.set_speech_text(text)
        title = 'skillful'
        content = ('A Python package for building Alexa skills.\n\n'
                   'Visit: https://github.com/bmweiner/skillful')
        skill.response.set_card_simple(title, content)
        skill.terminate()

    @skill.intent('no')
    def on_intent_no():
        text = ('Well, if you change your mind, open the Alexa app to see '
                'more information on skillful, a Python package for '
                'building Alexa skills.')
        skill.response.set_speech_text(text)
        title = 'skillful'
        content = ('A Python package for building Alexa skills.\n\n'
                   'Visit: https://github.com/bmweiner/skillful')
        skill.response.set_card_simple(title, content)
        skill.terminate()

    @skill.session_ended
    def on_session_ended():
        print('Ended: {}'.format(skill.request.session.session_id))
        skill.terminate()

    # simulate request body
    body = data.SAMPLE_LAUNCH_REQUEST
    skill.process(body)

Output:

    Launched: amzn1.echo-api.session.0000000-0000-0000-0000-00000000000

    {
      "version": "1.0",
      "response": {
        "outputSpeech": {
          "text": "Welcome to skillful. Would you like to build an Alexa skill?",
          "type": "PlainText"
        },
        "shouldEndSession": false,
        "reprompt": {
          "outputSpeech": {
            "ssml": "<speak>Please tell me if you would like to build an Alexa skill.</speak>",
            "type": "SSML"
          }
        }
      }
    }
