# Django Application

## Backend
---

### Dependencies
**[Homebrew - for OSX](http://brew.sh/)**

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    #Verify installation:
    brew --version

**[PIP](https://pip.pypa.io/en/latest/installing.html)**    

    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
    #Verify installation:
    pip --version

**[Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)**    

    pip install virtualenv
    #Verify installation:
    virtualenv --version

### Installation

The first time you set up the project, run the following commands:
    
    git clone git@github.com:ninapavlich/celadon.git
    cd celadon
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Place environment variables in .env at the top level of the project

    python manage.py migrate

    python manage.py loaddata celadon/fixtures/core.json #Note this may take several minutes to complete...
    
    python manage.py runserver

To connect to the Heroku project:
    
    #Ensure you have access to the Heroku project

    #Install the heroku toolbelt: https://toolbelt.heroku.com/
    #Once installed, log in to your Heroku account
    heroku login

    #Link celadon folder with heroku project:
    heroku git:remote -a celadon

    #To push to heroku
    git push heroku master

## Database/Model Updates

    python manage.py makemigrations
    python manage.py migrate

    #Be sure to add new migration file to git
    git add path/to/migration/file.py



## Database Fixtures

Dump a configuration database fixture (contains all content, but no user-generated content):

    python manage.py dumpdata --natural-foreign --indent=4 -e sessions -e admin -e contenttypes -e auth.Permission -e reversion > celadon/fixtures/core.json

Load a fixture file:
    
    python manage.py loaddata celadon/fixtures/core.json

