# Display Free Disk Space

The `df` utility is a handy way to display the free disk space available on
on a specific file system or all mounted file systems.

Use `df` with the `-h` flag to display the disk space usage and availability
in a human-readable format.

Here is the output from a linode box of mine:

```bash
➜  df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2        92G   65G   23G  75% /
none            4.0K     0  4.0K   0% /sys/fs/cgroup
udev            3.9G  4.0K  3.9G   1% /dev
tmpfs           791M  1.4M  790M   1% /run
none            5.0M     0  5.0M   0% /run/lock
none            3.9G   70M  3.8G   2% /run/shm
none            100M   64K  100M   1% /run/user
/dev/sda1       9.5G  3.4M  9.5G   1% /boot/efi
/dev/sda5        94G   32K   94G   1% /windows
```
