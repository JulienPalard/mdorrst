# awschimp
aws utils fit for a chimp

### Installation
```shell
pip install awschimp
```

### Utilities:

#### manage_creds:

Allows you to refer to AWS profiles from both ~/.aws/credentials and
~/.aws/config files.

Search order is:
~/.aws/credentials
~/.aws/config

First match wins.

For role profiles you can call get_temp_keys() and it will fetch temporary keys
form STS and cache them in a dot file in your home directory.

More info on creating role profiles in ~/.aws/config:<br>
http://docs.aws.amazon.com/cli/latest/userguide/cli-roles.html

#### Usage

#### Assuming a role
```shell
>>> import awschimp
>>> creds = awschimp.manage_creds("my_aws_profile", "my-cool-app")
>>> creds.get_temp_keys()
{u'SecretAccessKey': '<secret_key>', u'SessionToken': '<session_token>', u'Expiration': datetime.datetime(2016, 2, 13, 22, 15, 35, tzinfo=tzutc()), u'AccessKeyId': '<access_key>'}
```

```shell
$ ls -a ~/.*.cache
/Users/mschurenko/.my-cool-app_my_aws_profile.cache
```

#### Fetching access key/scret key and role arn from profile
```shell
>>> import awschimp
>>> creds = awschimp.manage_creds("my_aws_profile")
>>> creds.get_from_profile()
('<access_key>', '<secret_key>', 'arn:aws:iam:<account_id>:role/<role_name>')
```
