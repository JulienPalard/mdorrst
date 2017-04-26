# AWS Encryptor
CLI and Python client for encrypting/decrypting a json settings file using KMS and upload to/download from S3.  Upload an encrypted copy of your secret variables from the command line and access them from your python files.
## Requirements
Must have an AWS account with access to S3 and KMS, and an AWS credentials file stored in your `~/.aws` directory with your `aws_access_key_id` and `aws_secret_access_key`:

```shell
[default]
aws_access_key_id = <aws access key id>
aws_secret_access_key = <aws secret access key>
```

Create a json file with your secret variables; `secrets.json` is the default file name but a different name can be used:

```javascript
// secrets.json
{ 
    'secret_1': 'a',
    'secret_2': 'b',
    'secret_3': 'c'
}
```
## Installation
```shell
$ pip install encryptor
```
## Usage
### Encrypting & Uploading
To encrypt and upload a file, run command from command line:

```shell
$ encryptor encrypt_upload <aws region> <s3 bucket> <optional=filepath>
```

Default is a `secrets.json` file in the same directory.

Encrypt and upload `secrets.json` to S3 bucket:

```shell
$ encryptor encrypt_upload us-west-1 my-bucket
```

Encrypt and upload `my-settings.txt` file from same directory:

```shell
$ encryptor encrypt_upload us-west-1 my-bucket my-settings.txt
```
Encrypt and upload `my-settings.txt` file from child directory:

```shell
$ encryptor encrypt_upload us-west-1 my-bucket ./child_dir/my-settings.txt
```

The S3 key name of your encrypted files will be the original file name plus `.enc`:

`secrets.json.enc`

`my-settings.txt.enc`

### Downloading and Decrypting
#### CLI
To view decrypted file, run command from command line:

```shell
$ encryptor decrypt_download <aws region> <s3 bucket> <optional=s3_key>
```
Default s3_key is `secrets.json.enc`.

Download and decrypt `secrets.json.enc` from S3 bucket:

```shell
$ encryptor download_decrypt us-west-1 my-bucket
```

Download and decrypt `my-settings.txt.enc` from S3 bucket:

```shell
$ encryptor download_decrypt us-west-1 my-bucket my-settings.txt.enc
```
This command will print the contents of the decrypted file to the console:

```shell
$ encryptor download_decrypt us-west-1 my-bucket
$ {'secret 1': 'a', 'secret 2': 'b', 'secret 3': 'c'}
```
#### Python Client
To use python client, import AWS_Encryptor from encryptor:

```python
from encryptor import AWS_Encryptor
```
Initialize client:

```python
from encryptor import AWS_Encryptor

client = AWS_Encryptor(<aws region>, <bucket>)
```
Get a value, `get`:

```python
client.get(
    <key>,
    <optional=default_value>,
    <optional=s3_key>, 
    <optional=buckt>
)
```

```python
from encryptor import AWS_Encryptor

client = AWS_Encryptor(<aws region>, <bucket>)

# key exists
secret_1 = client.get('secret 1', 'default')
secret_1 == 'a' # True

# key does not exist
secret_99 = client.get('not_here', 'default')
secret_99 == 'default' # True

# different s3_key (default is secrets.json.enc)
secret_diff_key = client.get(
    'secret 1',
    'default',
    'other_s3_key'
)

# different bucket than intialized bucket
secret_diff_bucket = client.get(
    'secret 2',
    'default',
    's3_key',
    'diff_bucket'
)
```
Put a value, `put`:

```python
client.put(
    <key>,
    <value>,
    <optional=s3_key>,
    <optional=bucket>
)
```

```python
from encryptor import AWS_Encryptor

client = AWS_Encryptor(<aws region>, <bucket>)

secret_1 = client.put('secret 1', 'z')
secret_1 == 'a' # False
secret_1 == 'z' # True

# put value in different S3 key
secret_2 = client.put(
    'secret 2',
    'b',
    'diff_s3_key'
)

# put value in different bucket
secret_3 = client.put(
    'secret_3',
    'c',
    's3_key',
    'diff_bucket'
)
```

## Credits
Owen Rumney, for his great blog post, [Client side encryption using Boto3 and AWS KMS](http://www.owenrumney.co.uk/2015/01/06/Boto3-client-side-encryption-using-KMS.html).

Kushal Das, for his great blog post, [Building command line tools in Python with click](https://kushaldas.in/posts/building-command-line-tools-in-python-with-click.html)
## License
Copyright 2017 Jonathan Wilson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.