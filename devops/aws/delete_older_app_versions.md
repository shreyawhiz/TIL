I ran the eb command to deploy a new version

```javascript
eb deploy TEST_ENV
```

But, i got the following error

**ERROR: You cannot have more than 1000 Application Versions. Either remove some Application Versions or request a limit increase.**

To fix this, run the following command

```javascript
eb labs cleanup-versions --older-than DAYS
```
