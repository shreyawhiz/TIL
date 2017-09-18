# Cat A File With Line Numbers

You can quickly view a file using `cat`

`$ cat sampleFile`
 
 To number all output lines, do
 
 `$ cat sampleFile --number`
 
 
 You can use less or more. Both will work.

The less command is more commonly used and provides more functionality than more.

Using both less or more, you can traverse a file page by page using the space bar, and line by line using the enter key.

There's no need to cat and pipe the file, either. You can just run the command on the file.

E.g. less myfile.txt
