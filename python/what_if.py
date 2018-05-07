# cats = 100
# cows = 20

# if cats < cows:
# 	print "cats"
# elif 0:
# 	print "Forever"
# else:
# 	print "ahahha"

print "you enter a dark room with two doors. Which door do you go through, door #1 or #1?"
door_no = int(raw_input("> "))
if door_no==1:
	print "you chose door #1"
	print "Now there is a giant bear eating ice cream. What do you do?"
	print "1. take the ice cream"
	print "2. scream"
	decision_2 = raw_input("> ")
elif door_no==2:
	print "you chose door #2"
else:
	print "Choose a valid number."