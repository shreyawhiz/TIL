# from sys import argv
# from os.path import exists
# script, from_file, to_file = argv
# print "Copying file contents from %s to %s" %(from_file,to_file)
# file = open(from_file);
# file_data = file.read();
# print "file contents : \n%s" %file_data
# print "Number of bytes to copy - %s" %len(file_data)
# print "does target file exist? - %s" %exists(to_file)
# print "writing to the destination file...."
# target_file = open(to_file, 'w');
# target_file.write(file_data);
# print "writtent successfully"
# print "read file \n%s" %target_file.read()

# Cnverting the whole script into one line and removing extra logs
from sys import argv; from os.path import exists;script, from_file, to_file = argv;open(to_file, 'w').write(open(from_file).read());