```javascript
docker pull dockerize/mongodb
```

That's it!

Now get the list of all available docker images
```javascript
docker images

REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
shreyawhiz/lbb-platform   latest              29654a00b544        About an hour ago   1.06GB
node                      boron               cf1a65507771        8 days ago          656MB
dockerize/mongodb         latest              376a511cfe12        3 years ago         760MB
```

Run it using
```javascript
docker run -d -p 27017:27017 -p 28017:28017 dockerize/mongodb
```

Now if you do,
```javascript
docker ps
```

You will see
```javascript
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                                                NAMES
77918e68af5e        dockerize/mongodb   "mongod"            4 seconds ago       Up 2 seconds        0.0.0.0:27017->27017/tcp, 0.0.0.0:28017->28017/tcp   inspiring_lumiere
```
