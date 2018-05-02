from sys import argv
script, user_name = argv;
# print "user_name selected is %s" %user_name
promt = "> "
print "Hi %s, I am bot. Please answer the following questions truthfully." %user_name
print "Do you like me %s ?" %user_name
likes_me = raw_input(promt)
print "Do you think trump is stupid?"
is_stupid = raw_input(promt);
print "."*20
print """
Alright, so you said %s to liking me
and %s for if you think trump is stupid
""" %(likes_me, is_stupid)
# print "like value selected is \"%s\"" %like