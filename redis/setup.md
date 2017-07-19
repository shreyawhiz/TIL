How to set up and run Redis as a service on MAC


```javascript
$ brew install redis
```

>After installation, you will see some notification about some caveats on configuring. Just leave it and continue to following some tasks on this article.

**Location of Redis configuration file.**
```javascript
$ /usr/local/etc/redis.conf
```

**Uninstall Redis and its files..**
```javascript
$ brew uninstall redis
$ rm ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
```

**Get Redis package information..**
```javascript
$ brew info redis
```

**Test if Redis server is running.**
```javascript
$ redis-cli ping
```
>If it replies **“PONG”**, then it’s good to go!
