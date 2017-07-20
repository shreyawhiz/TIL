>install docker for mac from [here](https://docs.docker.com/docker-for-mac/install/)

### Install and Run Docker for Mac
1. Double-click *Docker.dmg* to open the installer, then drag Moby the whale to the Applications folder
2. Double-click *Docker.app* in the Applications folder to start Docker




![That's it!!](https://vignette2.wikia.nocookie.net/looneytunes/images/e/e1/All.jpg/revision/latest/scale-to-width-down/260?cb=20150313020828)


Docker application is now running on your system.

Open iTerm or any other terminal, and type
```javascript
docker info
```

This will tell you evrything currently running in docker and what all images it currently has, its version and much more

```javascript
Containers: 0
 Running: 0
 Paused: 0
 Stopped: 0
Images: 8
Server Version: 17.06.0-ce
Storage Driver: overlay2
 Backing Filesystem: extfs
 Supports d_type: true
 Native Overlay Diff: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
 Volume: local
 Network: bridge host ipvlan macvlan null overlay
 Log: awslogs fluentd gcplogs gelf journald json-file logentries splunk syslog
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: cfb82a876ecc11b5ca0977d1733adbe58599088a
runc version: 2d41c047c83e09a6d61d464906feb2a2f3c52aa4
init version: 949e6fa
Security Options:
 seccomp
  Profile: default
Kernel Version: 4.9.36-moby
Operating System: Alpine Linux v3.5
OSType: linux
Architecture: x86_64
CPUs: 2
Total Memory: 1.952GiB
Name: moby
ID: TUVS:WITH:LRVO:Y66A:Y5KH:Q64R:2Y4C:6JJP:J5W5:JX4M:WQ3V:EVE2
Docker Root Dir: /var/lib/docker
Debug Mode (client): false
Debug Mode (server): true
 File Descriptors: 17
 Goroutines: 29
 System Time: 2017-07-20T10:38:03.69251751Z
 EventsListeners: 1
No Proxy: *.local, 169.254/16
Registry: https://index.docker.io/v1/
Experimental: true
Insecure Registries:
 127.0.0.0/8
Live Restore Enabled: false
```
