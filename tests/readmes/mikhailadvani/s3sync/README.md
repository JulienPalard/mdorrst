# aws_s3sync

## Installation

`pip install aws_s3sync`

## Execution

#### Pre-requisites

Setup the following environment variables

* **AWS_ACCESS_KEY_ID**
* **AWS_SECRET_ACCESS_KEY**

#### Commands

`sync_to_s3`

`sync_from_s3`

#### Arguments

```
  -h, --help            show this help message and exit
  -b BUCKET, --bucket BUCKET
                        Upload: Selects the S3 bucket to upload data to.
                        Download: Selects the S3 bucket to download data from
  -f FILE_PATH, --file_path FILE_PATH
                        Upload: Path of the file to be uploaded. Download:
                        Path to download file to
  -k KEY, --key KEY     Key of the object. Same as file_path is undefined for
                        upload
  -m {auto,sync,single-part-upload}, --mode {auto,sync,single-part-upload}
                        Mode of upload/download
  --chunk_size CHUNK_SIZE
                        Size of chunk in multipart upload in MB
  --multipart_threshold MULTIPART_THRESHOLD
                        Minimum size in MB to upload using multipart
```

##### Mode

* `auto` : Upload: Single-part upload or multi-part upload will be chosen based on the file being smaller/larger than `multipart_threshold`
* `sync` : Upload/downloand file to/from S3 only if the local/remote file have different signatures. Checked based on ETag/MD5
* `single-part-upload` : Force single-part upload. Applicable only for files of size larger than `multipart_threshold`


