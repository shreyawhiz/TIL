days = "M T W Th F S S"
months = "\nJ\nF\nM\nA\nM\nJ\nJ\nA\nS\nO\nN\nD"
print "here are the days %s" % days
print "here are the months %s" % months

print """
sample1
sample2
"""

print '''
sample3
sample4
'''

# Another important escape sequence is to escape a single- quote ' or double- quote ". Imagine you have a string 
# that uses double- quotes and you want to put a double- quote in for the output.
# If you do this "I "understand" joe." then Python will get confused since it will think the "
# around "understand" actually ends the string. You need a way to tell Python that the " inside
# the string isnt a real double quote

print "i \"understand\" this"

print "\t i am tabbed"
print "\r i am returned"
print "i am \\ a \\ cat"

print "."*10
print "\n"
print "let's create a list"
print """
\t* one
\t* two
\t* three
"""