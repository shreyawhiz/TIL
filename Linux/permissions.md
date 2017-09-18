## Fix permissions

Permission errors are the most common problems I see people run into using the command line. Usually this happens when installing a language or language dependency. To fix this, run the following command to set your current user as the owner of the /usr/local directory.
````javascript
sudo chown -R `whoami` /usr/local
````


