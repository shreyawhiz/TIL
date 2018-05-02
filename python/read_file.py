from sys import argv
script, file_name = argv
print "Opening and reading file with file name - %s" %file_name
print "-"*15
# open function takes a parameter and returns a value you can set to your own variable.
file_content = open(file_name);
print file_content.read(),
print "-"*15


print "Enter another file name to read"
file_name_2 = raw_input(">")
print "Opening and reading file with file name - %s" %file_name_2
print "-"*15
file_content = open(file_name_2);
print file_content.read(),
print "-"*15


# We call a function on file_content. What you got back from open is a file, and its also got commands you can
# give it. You give a file a command by using the . (dot or period), the name of the command, and
# parameters. Just like with open and raw_input. The difference is that when you say file_content.read()
# you are saying, Hey file_content! Do your read command with no parameters!