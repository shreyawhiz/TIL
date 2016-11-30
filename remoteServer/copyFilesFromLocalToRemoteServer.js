// How to copy files from your local machine to a remote server via FTP.

// ------------------------------------
// COMMAND
// ------------------------------------
sudo scp -i "accessKey.pem" folderToCopy.tar.gz  username@testapi:/destination/path

1. Create a tar file.
2. use the above mentioned command to copy the compressed tar file into the destination folder on the remote server.
3. extract the tar file using
					tar -xvzf fileName.tar.gz﻿⁠⁠⁠⁠