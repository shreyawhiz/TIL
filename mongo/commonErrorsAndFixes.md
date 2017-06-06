## 1. createIndex error: The field 'safe' is not valid for an index specification.

In previous versions of MongoDB, lower than 3.4, extra indexes specifications can be added. Those were used by specific drivers.

In 3.4, mongodb added a validation on indexes specification:

That's why you have this error. I am afraid you need to ensure that the index in your 3.2 version does not have invalid index specificaitons, and after that do the mongodump.

You can do 
#### mongorestore --noIndexRestore, 
this should work fine.

https://stackoverflow.com/questions/41036442/mongodb-dump-from-3-2-restore-with-3-4-error-index-save-null
