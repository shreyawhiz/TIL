# Functions do three things:
#  1. They name pieces of code the way variables name strings and numbers.
#  2. They take arguments the way your scripts take argv.
#  3. Using #1 and #2, they let you make your own mini- scripts or tiny commands.

#  You can create a function by using the word def in Python

def print_name(name):
	print "Your name is %s" %name

print_name('shreyawhiz')


def print_name_from_argument():
	from sys import argv
	script, name = argv
	print "name entered as argument is %s" %name

print_name_from_argument()

def print_name_using_prompt_input():
	name = raw_input("What is your name?")
	print "Name entered is %s" %name

print_name_using_prompt_input()