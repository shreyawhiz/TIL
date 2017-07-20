1. create a file named *Dockerfile* in your current node repo folder.

```javascript
touch Dockerfile
```

2. Open the file in your favorite editor
```javascript
subl Dockerfile
```

3. Copy-Paste this
```javascript
// The first thing we need to do is define from what image we want to build from
FROM node:argon
//Next create a directory to hold the application code inside the image, this will be the working directory for the application:
RUN mkdir /app
WORKDIR /app
//This image comes with Node.js and NPM already installed so the next thing we need to do is to install your app dependencies using the npm binary
COPY package.json /app
RUN npm install
//To bundle your app's source code inside the Docker image, use the COPY instruction:
COPY . /app
//if the app binds to port 3000 so you'll use the EXPOSE instruction to have it mapped by the docker daemon:
EXPOSE 3000
//define the command to run the app using CMD which defines your runtime
CMD ["npm", "start"]
```


4. **.dockerignore file**

Create a .dockerignore file in the same directory as your Dockerfile with following content:
```javascript
node_modules
npm-debug.log
```

5. **Building your image**
Go to the directory that has your Dockerfile and run the following command to build the Docker image. The -t flag lets you tag your image so it's easier to find later using the docker images command:
```javascript
$ docker build -t <your username>/node-web-app .
```

###Your image will now be listed by Docke
```javascript
shreyabatra@Shreyas-MacBook-Pro ~/Documents/lbb/codebase/lbb-platform (master●●)$ docker images                                                                                                                                                                [ruby-2.0.0p648]
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
shreyawhiz/lbb-platform   latest              29654a00b544        13 minutes ago      1.06GB
node                      boron               cf1a65507771        8 days ago          656M
```


**We have successfully created a docker image!!!**


