[![Build Status](https://travis-ci.org/lsst-sqre/sqre-codekit.svg?branch=master)](https://travis-ci.org/lsst-sqre/sqre-codekit)

# sqre-codekit

LSST DM SQuaRE misc. code management tools

## Installation

sqre-codekit runs on Python 2.7 or 3.5. You can install it with

```bash
pip install sqre-codekit
```

This will also install dependencies: `github3`, `urllib3`, `requests`, `progress` and `gitpython`.

## Example usage

To generate a personal user token (you will be prompted for your password):

```bash
github-auth -u {{username}}
```

Or to generate a token with delete privileges:

```bash
github-auth -u {{username}} --delete-role
```

To clone all github.com/lsst repos into an GitHub organization called `{{username}}-shadow`:

```bash
github-fork-repos -u {{username}} --org {{username}}-shadow
```
    
You'll need to create this shadow organization in advance. Working in a shadow organization is useful for testing.

If you want to take a recent fork, you will need to delete the existing shadow repos first:

```bash
github-delete-shadow -u {{username}}
```

That requires a token with delete privileges. 

To get more debugging information, set your `DM_SQUARE_DEBUG` variable before running any command, or use the `-d` debug flag on the command line.

## Available commands

- `github-auth`: create a GitHub authentication token.
- `github-fork-repos`: fork repositories into a shadow GitHub organization.
- `github-list-repos`: list repositories in a GitHub organization, showing teams.
- `github-mv-repos-to-team`: move repositories from one team to another.
- `github-tag-version`: tag all repositories in a GitHub org using a team-based scheme.
- `lsst-bp`: upgrade LSST DM code to [RFC-45](https://jira.lsstcorp.org/browse/RFC-45)-style.

Use the `--help` flag with any command to learn more.

## Development

To develop codekit, create a Python virtual environment, and

```bash
git clone https://github.com/lsst-sqre/sqre-codekit.git
cd sqre-codekit
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python setup.py develop
```

Note that all scripts (in `codekit/cli`) are installed using setuptools `entry_points`. See `setup.py`.

Tests can be run with [pytest](http://pytest.org/latest/):

```bash
py.test tests
```
