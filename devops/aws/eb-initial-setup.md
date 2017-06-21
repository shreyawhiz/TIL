The Elastic Beanstalk Command Line Interface (EB CLI) is a command line client that you can use to create, configure, and manage Elastic Beanstalk environments.


The primary distribution method for the EB CLI on Linux, Windows, and macOS is pip, a package manager for Python that provides an easy way to install, upgrade, and remove Python packages and their dependencies


### Install Pip with apt-get

```sh
$ apt-get update
$ apt-get -y install python-pip
```

Check the version of Pip that is installed:
```sh
$ pip -V
```

### Install python
First, install some dependencies:
```sh
$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```

Then download using the following command:
```sh
$ version=2.7.13
$ cd ~/Downloads/
$ wget 'https://www.python.org/ftp/python/$version/Python-$version.tgz'
```

Extract and go to the directory:
```sh
$ tar -xvf Python-$version.tgz
$ cd Python-$version
$ ./configure
$ make
$ sudo checkinstall
```

If you already installed pip and a supported version of Python, you can install the EB CLI with the following command:
```sh
$ pip install --upgrade --user awsebcli
```

(The **--upgrade** option tells pip to upgrade any requirements that are already installed. The --user option tells pip to install the program to a subdirectory of your user directory to avoid modifying libraries used by your operating sytem.)


After you install the EB CLI, add the path to the executable file to your PATH variable:

```sh
Linux – ~/.local/bin
macOS – ~/Library/Python/3.4/bin
```

Verify that the EB CLI installed correctly by running eb --version.
```sh
$ eb --version
$ EB CLI 3.7.8 (Python 3.4.3)
```

If you need to uninstall the EB CLI, use pip uninstall.
```sh
$ pip uninstall awsebcli
```

## PROCESS OF DEPLOYMENT

1. Go to directory to deploy

```sh
$ cd ~/Documents/work/toDeployFolder
$ eb init
```
	- configure your eb setup
```sh
$ eb deploy
```
	- to deploy local directory to elasticbeanstalk
