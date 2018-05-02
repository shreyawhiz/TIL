# commands that we can run on a file
# 1. read - reads contents of a file
# 2. readline - read one line of a file
# 3. close - closes a file
# 4. truncate - empties a file
# 5. write(stuff) - writes stuff to a file
from sys import argv
script, file_name = argv
print "truncating file - %s" %file_name
print "hit CTRL+C(^C) incase you dont want it to be truncated"
print "else hit any key to continue"
raw_input(">")
file = open(file_name, 'w')
file.truncate()
print "file truncated successfully"
print "Enter text to write to a file";
line1 = raw_input("Line1 - ")
line2 = raw_input("Line2 - ")
line3 = raw_input("Line3 - ")
print "writing lines to the same file %s" %file
file.write(line1)
file.write('\n')
file.write(line2)
file.write('\n')
file.write(line3)
file.write('\n')
print "DONE"
file.close()
