# sqre-ghowlauth

GitHub Organization WhiteList Authentication

JupyterHub authentication that uses GitHub OAuth2 but additionally
checks user org membership against a list defined in the environment
variable `GITHUB_ORGANIZATION_WHITELIST`.

## Installation

sqre-ghowlauth runs on Python 3.3 or greater. You can install it with

```bash
pip install sqre-ghowlauth
```

This will also install dependencies: `jupyterhub` and `tornado`.

## Example usage

Your `jupyterhub_config.py` file should contain
`c.JupyterHub.authenticator_class = 'ghowlauth.GHOWLAuthenticator'` (or
you can use `LocalGHOWLAuthenticator` to handle both local and GitHub
auth).

You also must have set the environment variable
`GITHUB_ORGANIZATION_WHITELIST` to be a comma-separated list of organizations
whose members you want to permit,
e.g. `GITHUB_ORGANIZATION_WHITELIST=lsst,lsst-sqre`.

The rest of the instructions are the same as those found at
https://github.com/jupyterhub/oauthenticator (that is, you still need a
callback URL, a client ID, and a client secret).
