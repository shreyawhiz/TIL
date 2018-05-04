from sys import argv
scan, file_name = argv

def print_file(file_name):
	print file_name.read()

def rewind_file(file_name):
	file_name.seek(0)

def print_a_line(line_number,file_name):
	print file_name.readline()


print "file entered is %s" %file_name

file_data = open(file_name)

print "reading the whole file - "
print_file(file_data);

print "-"*20

rewind_file(file_data)

print "file rewinded"

# wont print anything if rewind_file is not called first
print_a_line(1, file_data);
print_a_line(2, file_data);
print_a_line(3, file_data);
