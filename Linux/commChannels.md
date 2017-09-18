Every process has atleast three communication channels available to it:
1. STDIN
2. STDOUT
3. STDERR

In UNIX, each channel is named with a small integer called a "File Descriptor".
															 ------------------
STDIN has 0,
STDOUT has 1, and
STDERR has 2
So they can also be referred by these numbers.

Most commands accept their inputs from STDIN, and write their poutput to STDOUT and error to STDERR.

The shell interprets >, <, and >> as instructions to reroute a command's input or output to or from a file.
For instance,
$ echo "This is a test text." > ~/dir/file.txt
This stores a single line to the file ~/dir/file.txt, creating the file if necessary.

$ mail -s "Test Mail" johndoe < /dir/mailToSend.text
This emails the contents of file mailToSend.text to johndoe.