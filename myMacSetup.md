To find What Shell Is Being Used in Mac OS X, Unix, Linux
```javascript
echo $SHELL
```


Setting up MAMP-PRO

While starting it was giving error that apache could not be started and there was nothing in the apache-server logs as well.
Upon searching, found the following solution thta fixed it

```javascript
mv /Applications/MAMP/Library/bin/envvars  /Applications/MAMP/Library/bin/_envvars
```
