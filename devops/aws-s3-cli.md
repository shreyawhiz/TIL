### install awscli

- install aws using pip3
```sh
$ pip3 install --upgrade --user awscli

$ aws --version
aws-cli/1.11.84 Python/3.5.2 Linux/4.4.0-59-generic botocore/1.5.47

```


### aws-s3-cli

```sh
aws s3 help
```

Methods provided
---------------

* cp
* mv
* rm
* sync
* ls
* mb
* rb

### sync

To sync sync a folder from local machine or an ec2 instance to s3 bucket
```sh
aws s3 sync localPath s3Uri
```
**--region** option
```
aws s3 sync localPath s3Url --region ap-south-1
```

```sh
/usr/local/bin/aws s3 sync public/uploads/users/ s3://files.eb.in/users --region ap-southeast-1
```
