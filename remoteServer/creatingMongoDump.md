-------------------------------------------------------------------------
## How to transfer a mongoDB from a remote server to your local machine ##
-------------------------------------------------------------------------

1. mongodump -d 'DB name'
	- creates a binary export of the data base.
	
2. tar -zcvf testDump.tar testDump/
	- Creates a compressed .tar file of the dump
	
3. sudo scp -i "accessKey.pem" username@ipOfRemoteServer:/path/of/the/file/testDump.tar "/destination/on/local/machine"

4. tar -xvzf testDump.tar.gz
	- Extract the contents from the .tar file
	
5. mongorestore
