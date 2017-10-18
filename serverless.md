[https://www.npmjs.com/package/serverless](https://www.npmjs.com/package/serverless)

[https://github.com/serverless/serverless](https://github.com/serverless/serverless)

**Serverless** is a node module which helps to build applications comprised of microservices that run in response to events, auto-scale for you, and only charge you when they run.

#### To connect serverless to a AWS Lambda
```javascript
serverless config credentials --provider aws --key {awskey} --secret {awssecret} --profile {awsuser}
```

#### Deploy a git repo to a Lambda
```javascript
serverless deploy function -f {functionName}
```
