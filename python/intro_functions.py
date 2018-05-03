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


def print_args(*args):
	arg1, arg2 = args
	print "arg1: %s and arg2: %s" %(arg1,arg2)

print_args("Hakuna", "Matata")

# uncomment code from line 43-47 and try running it
# Gives the following error:
# Traceback (most recent call last):
#   File "intro_functions.py", line 39, in <module>
#     print_args("Hakuna", "Matata", "No Worries")
#   File "intro_functions.py", line 36, in print_args
#     arg1, arg2 = args
# ValueError: too many values to unpack

# def print_args(*args):
# 	arg1, arg2 = args
# 	print "arg1: %s and arg2: %s" %(arg1,arg2)

# print_args("Hakuna", "Matata", "No Worries")
