## ubuntu 16.04 LTS


````javascript
sudo systemctl start mongodb
sudo systemctl status mongodb
````

The last step is to enable automatically starting MongoDB when the system starts.
````javascript
sudo systemctl enable mongodb
````
output :
Created symlink from /etc/systemd/system/multi-user.target.wants/mongodb.service to /etc/systemd/system/mongodb.service.
