from sys import exit

def dead(reason):
	print "You are dead - %s" %reason
	exit(0)


def gold_room():
	print "This room is full of gold. How much do you take?"
	next = raw_input("> ")
	print "next %s" %next
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			print "gold room"
			gold_room()
		else:
			print "I got no idea what that means."

def start():
	print """
	You are in a dark room. 
	There is door to your left and right
	which one do you take
	"""
	next = raw_input("> ")

	if next == "left":
		print "Left chosen"
		bear_room()
	elif next == "right":
		print "Right chosen"
	else:
		dead("You stumble around the room until you starve.");

start()