`cat command` is useful in displaying entire file content.

But in some cases, we have to print part of file. 

`head and tail commands`
are very useful when you want to view a certain part at the beginning or at the end of a file, specially when you are sure you want to ignore the rest of the file content.

## Tail command ##

`Tail` command prints the last few number of lines (10 lines by default) of a certain file, then terminates.

Example 1: By default “tail” prints the last 10 lines of a file, then exits.

`tail /path/to/file`

We can change this default number of lines with the help of the following command.

`tail -n <number_of_lines> /path/to/file`


## The MOST IMPORTANT tail command!!!!!! ##
`tail -f /path/to/file`

-f stands for follow.

Unlike the default behaviour which is to end after printing certain number of lines, `the -f option will keep the stream going`. 
It will start printing extra lines on to console added to the file after it is opened. 
This command will keep the file open to display updated changes to console until the user breaks the command.






## Head command ##

Very similar to the tail commands, it justs prints the beginning lines of a file

Ex. `head /path/to/file`

`head -n <number_of_lines> /path/to/file` will print the first n lines of the selected file.





## Combine head and tail command in Linux ##

As tail and head commands print different parts of files in an effective way, we can combine these two to print some advanced filtering of file content. 

Ex. To print 15th line to 20th line in /etc/passwd file use below example.

`head -n 20 /etc/passwd | tail -n 5`



Link : https://www.linux.com/blog/14-tail-and-head-commands-linuxunix
