# A file in Python is kind of like an old tape drive on a mainframe, or maybe a DVD player. It has
# a READ HEAD, and you can SEEK this read head around the file to positions, then work with
# it there. Each time you do f.seek(0), you are moving to the start of the file. Each time you do
# f.readline(), you are reading a line from the file and moving the read head to right after the
# \n that ends that file


from sys import argv
scan, file_name = argv

def print_file(file_name):
	print file_name.read()

def rewind_file(file_name):
	file_name.seek(0)


# The readline() function returns the \n that is in the file at the end of that line. This means that
# print \n is being added to the one already returned by readline(). To change this behavior
# simply add a , (comma) at the end of print so that it does not print its own \n.
def print_a_line(line_number,file_name):
	print file_name.readline()
	# print file_name.readline(),


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
