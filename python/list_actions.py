my_list = "arrow super_girl batman wolverine cyclops"
stuff = my_list.split(' ')
print len(stuff)

print "make this 15 items";
more_stuff = ["ironman", "hulk", "thor", "captain_america", "spiderman", "vision", "loki", "black_widow", "strange", "superman"]

# if final_count>len(more_stuff), we get the following error - 
# Traceback (most recent call last):
#   File "list_actions.py", line 9, in <module>
#     next = more_stuff.pop()
# IndexError: pop from empty list
final_count = 15
while len(stuff) != final_count:
	next = more_stuff.pop()
	stuff.append(next)

# print "stuff %s" %stuff
print stuff
print stuff[-1] #prints the last element
print "Len %s" %(len(stuff))


# join is the opposite of split
print ' '.join(stuff)

print ','.join(stuff[0:5])

print ','.join(stuff[0:len(stuff)])


# print join('%', stuff)
