> `Nodejs`
> `node-statsd`
> `statsd`
> `aws-cloudwatch-statsd-backend`


 
## `statsd`

`StatsD` is originally a simple daemon to aggregate and summarize application metrics.
With StatsD, applications are to be instrumented by developers using language-specific client libraries. 
These libraries will then communicate with the StatsD daemon using its dead-simple protocol, 
and the daemon will then generate aggregate metrics and relay them to virtually any graphing or monitoring backend.


The StatsD program is not available in the Ubuntu default repositories. However, it is available on GitHub and has the configuration files necessary to compile it into an Ubuntu package.


## So How does StatsD work?

The StatsD `client library` you are using (node-statsd for me) sends each individual call to the StatsD server over a UDP datagram. 
Since UDP is a disconnected protocol in which the recipient of a datagram doesn’t send any acknowledgement to the sender, the library doesn’t need to block when submitting data as it would with TCP or HTTP-based protocols. 

`echo "metric_name:metric_value|type_specification" | nc -u -w0 127.0.0.1 8125`

This will send a UDP packet to the port that StatsD is listening on.


`Statsd daemon` listens for UDP packets. It collects all of the packets sent to it over a period of time (10 seconds by default). It then aggregates the packets it has received and flushes a single value for each metric to the backend of your choice (aws-cloudwatch-statsd-backend for me; could be `Graphite` or `Carbon`)

The `monitoring backend` will turn your metrics from a stream of numbers on the wire into usable charts and alert you when needed. 	



## install statsd dependencies

We need `git` so that we can clone the repository. 
	https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
	
	
We also need `node.js` because `StatsD is a node application`.

#### Install `Node.js` from here
	
	>  [https://nodejs.org/en/download/]
	>  https://nodejs.org/en/download/package-manager/
	
	
	
We also need `devscripts` `debhelper`.

These will allow us to build an Ubuntu package. 

Get all these in Ubutnu by the following command
	`sudo apt-get install git nodejs devscripts debhelper`
	



We are going to create the package in our home directory. More specifically, we will create a directory called "build" in our home directory to complete this process.

Create the directory now:
	`mkdir ~/build`
	
Now, we will clone the StatsD project into that directory. Move into the directory and then issue the clone command:

	`cd ~/build`
	`git clone https://github.com/etsy/statsd.git`
	
	
# Build and Install the Package

Move into the new directory that contains our StatsD files:
	`cd statsd`
	
	
Now, we can create the StatsD package by simply issuing this command:
	`dpkg-buildpackage`
	
A .deb file will be created in ~/build directory. Let's move back out into that directory.
	`cd .. `

We can then install the package into our system:
	sudo dpkg -i statsd*.deb
	
	

At this point of time, I got an error while creating the deb file.
I installed `dh-systemd`
	`sudo apt-get update`
	`sudo apt-get install dh-systemd`
	
This resolved the issue.


### SUCCESS! :)
	
	
### Statsd is now loaded as a node application in your system.

`➜  ~ ls /usr/share/statsd`

`drwxr-xr-x  2 root root  4096 Mar  8 15:27 backends`

`drwxr-xr-x  2 root root  4096 Mar  8 15:27 lib`

`drwxr-xr-x 34 root root  4096 Mar  8 19:01 node_modules`

`-rw-r--r--  1 root root  1112 Mar  6 13:30 package.json`

`-rw-r--r--  1 root root  8369 Mar  6 13:30 proxy.js`

`drwxr-xr-x  2 root root  4096 Mar  8 15:27 servers`

`-rw-r--r--  1 root root 14388 Mar  6 13:30 stats.js`	



### start statsd service

`sudo service statsd start`



## Configure StatsD

The first thing that we should do is modify the StatsD configuration file.

	`➜  ~ ls /etc/statsd `
	
	`-rw-r--r-- 1 root root 312 Mar  8 19:10 localConfig.js`
	
	`-rw-r--r-- 1 root root 169 Mar  6 13:30 proxyConfig.js`
	

Open localConfig in your local editor or vi

It should look like this:

`{`
`  graphitePort: 2003`
`, graphiteHost: "localhost"`
`, port: 8125`
`}`

StatsD configuration file by default is configured to be used by Graphite backend.

You can see `graphite.js`
	`➜  ~ ls /usr/share/statsd/backends
	
	`-rw-r--r-- 1 root root 1.4K Mar  6 13:30 console.js`
	
	`-rw-r--r-- 1 root root  11K Mar  6 13:30 graphite.js`
	
	`-rw-r--r-- 1 root root 3.1K Mar  6 13:30 repeater.js`


`

## MONITORING BACKEND (aws-cloudwatch-statsd-backend)

StatsD backend for AWS CloudWatch.

> https://www.npmjs.com/package/aws-cloudwatch-statsd-backend
	
With this package you can replace Graphite in favour of AWS Cloudwatch for your monitoring purposes, appropriate for sites on the Amazon EC2 cloud.
 
 `➜  ~ ls /usr/share/statsd/
 `npm install aws-cloudwatch-statsd-backend` (installing ACSB as a statsd dependency)
 

The following demonstrates the minimum statsd config for the CloudWatch backend.
Edit /etc/statsd/localConfig.js to look like this

`{`
`  graphitePort: 2003`
`, graphiteHost: "localhost"`
`, port: 8125,
`debug: true,`
`backends: ["./backends/console", "aws-cloudwatch-statsd-backend"],`
`cloudwatch:`
`    {`
`        accessKeyId: 'YOUR_ACCESS_KEY_ID',`
`        secretAccessKey:'YOUR_SECRET_ACCESS_KEY',`
`        region:"YOUR_REGION"`
`    }`
`}`


The above will create a metric with the default namespace, AwsCloudWatchStatsdBackend, and send an http request to CloudWatch via awssum.

Also will print everything out in console.


## CLIENT-LIBRARY (node-statsd)

There are many great StatsD client libraries that make it easy to send statistics from the apps you are creating using whatever programming logic makes sense.

I personally found `node-statsd` very userful
	`https://www.npmjs.com/package/node-statsd`




In one terminal, start StatsD with the following

	`cd /usr/share/statsd`
	`node stats.js /etc/statsd/localConfig.js`
	
	
In another terminal,

`echo "metric_name:metric_value|type_specification" | nc -u -w0 127.0.0.1 8125`

This will send a UDP packet to the port that StatsD is listening on.



