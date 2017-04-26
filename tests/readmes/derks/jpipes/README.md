# Jenkins Pipeline Automation

Create a config file with your Jenkins server credentials:

**~/.jpipes.yml**:

```yaml
---
# jpipes:
#     plugin_dir: /var/lib/jpipes/plugins/
#     plugin_config_dir: /etc/jpipes/plugins.d/

jenkins:
    url: https://jenkins.example.com
    username: john.doe
    password: oober-secure-password
    prefix: pipeline-
```

Create pipelines in Jenkins with a prefix of `pipeline-`:

**pipeline-example-test**:

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo BUILDING EXAMPLE APP'
            }
        }
        stage('Test'){
            steps {
                sh 'echo RUNNING EXAMPLE APP TESTS'
            }
        }
    }
}
```

**pipeline-example-deploy**:

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo BUILDING EXAMPLE APP'
            }
        }
        stage('Test'){
            steps {
                sh 'echo RUNNING EXAMPLE APP TESTS'
            }
        }
        stage('Deploy'){
            steps {
                sh 'echo DEPLOYING EXAMPLE APP'
            }
        }
    }
}
```


JPipes automatically pulls these in via the Jenkins API:

```bash
$ jpipes --help
usage: jpipes [-h] [--debug] [--quiet] [-o {yaml}]
              {example-test,example-deploy} ...

Jenkins Pipeline Automation

optional arguments:
  -h, --help            show this help message and exit
  --debug               toggle debug output
  --quiet               suppress all output
  -o {yaml}             output handler

sub-commands:
  {example-test,example-deploy}
    example-test        pipeline sub-controller
    example-deploy      pipeline sub-controller


### run pipeline-example-test job

$ jpipes example-test
INFO: WAITING FOR JOB TO START: https://jenkins.example.com/queue/item/569/api/json
INFO: JOB STARTED: https://jenkins.example.com/job/pipeline-example-test/2/
Started by user BJ Dierkes
[Pipeline] node

Running on jenkins-slave01.example.com in /var/lib/jenkins/workspace/pipeline-example-test
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] sh

[pipeline-example-test] Running shell script
+ echo BUILDING EXAMPLE APP
BUILDING EXAMPLE APP
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Test)

[Pipeline] sh
[pipeline-example-test] Running shell script
+ echo RUNNING EXAMPLE APP TESTS
RUNNING EXAMPLE APP TESTS
[Pipeline] }
[Pipeline] // stage

[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS

INFO: JOB COMPLETED SUCCESSFULLY


### run pipeline-example-deploy job

$ jpipes example-deploy
INFO: WAITING FOR JOB TO START: https://jenkins.example.com/queue/item/571/api/json
INFO: JOB STARTED: https://jenkins.example.com/job/pipeline-example-deploy/1/
Started by user BJ Dierkes
[Pipeline] node
Running on jenkins-slave02.example.com in /var/lib/jenkins/workspace/pipeline-example-deploy
[Pipeline] {

[Pipeline] stage
[Pipeline] { (Build)

[Pipeline] sh
[pipeline-example-deploy] Running shell script
+ echo BUILDING EXAMPLE APP
BUILDING EXAMPLE APP
[Pipeline] }
[Pipeline] // stage

[Pipeline] stage
[Pipeline] { (Test)
[Pipeline] sh
[pipeline-example-deploy] Running shell script
+ echo RUNNING EXAMPLE APP TESTS
RUNNING EXAMPLE APP TESTS
[Pipeline] }

[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Deploy)
[Pipeline] sh

[pipeline-example-deploy] Running shell script
+ echo DEPLOYING EXAMPLE APP
DEPLOYING EXAMPLE APP
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node

[Pipeline] End of Pipeline
Finished: SUCCESS

INFO: JOB COMPLETED SUCCESSFULLY
```

## Parameterized Builds

Currently `jpipes` supports the simple `String Parameter`, and will 
automatically add sub-parser options for each job based on the required
parameters defined in Jenkins:

```bash
$ jpipes example-test --help
usage: jpipes example-test [-h] --foo FOO {} ...

optional arguments:
  -h, --help  show this help message and exit
  --foo FOO   the notorious foo parameter

sub-commands:
  {}

$ jpipes example-test --foo=bar
...
```

Support for all other parameter types will be added at some point.

## Project Based Configurations

Configuration files are looked for in the following order:

- `/etc/jpipes/jpipes.yml`
- `~/.jpipes.yml`
- `~/.jpipes/config`
- `jenkins/jpipes.yml`


The above allows you to set global Jenkins settings (url, creds, etc) but
have project-local based overrides (i.e. `prefix`):

**my-project-root/jenkins/jpipes.yml**:

```yaml
---
jenkins:
    prefix: pipeline-my-project-prefix-
```

The above will simplify the `jpipes` usage when inside a project directory:

```bash
### run pipeline-my-project-prefix-test

$ jpipes test


### run pipeline-my-project-prefix-deploy

$ jpipes deploy


### run pipeline-my-project-prefix-deploy with parameters?

$ jpipes deploy \
    --to staging \
    --from-branch my-feature-branch-in-git
```

Etc...
