# Show Disk Usage For The Current Directory

The `du` utility can be used to show disk usage for a particular directory
or set of directories.
When used without any arguments, it will show the disk usage for the current directory.

```bash
$ du
260	./node_modules/fsevents/node_modules/json-schema
36	./node_modules/fsevents/node_modules/dashdash/node_modules/assert-plus
40	./node_modules/fsevents/node_modules/dashdash/node_modules
20	./node_modules/fsevents/node_modules/dashdash/etc
...
```

with the `-h` command we can see it all in a human-readable format

```bash
$ du -h
196K	./.git/logs/refs/remotes
428K	./.git/logs/refs
768K	./.git/logs
4.0K	./.git/branches
8.0K	./meta/passport-auth
648K	./meta/mongoScripts

```

and to get an even clearer picture we can pipe that through `sort -nr`

```bash
$ du -h | sort -nr
20K	./.git/info
19M	./node_modules/phantomjs
16K	./node_modules/spawn-sync/lib/json-buffer
12K	./node_modules/touch/test
...
```

This sorts it numerically in reverse order putting the largest stuff at the
top.
