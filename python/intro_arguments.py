# On line 1 we have whats called an import. This is how you add features to your script from the
# Python feature set. Rather than give you all the features at once, Python asks you to say what you
# plan to use. This keeps your programs small, but it also acts as documentation for other programmers
# who read your code later.

# The argv is the argument variable, a very standard name in programming that you will fi nd
# used in many other languages. This variable holds the arguments you pass to your Python script
# when you run it. In the exercises you will get to play with this more and see what happens.

# Line 3 UNPACKS argv so that, rather than holding all the arguments, it gets assigned to four
# variables you can work with: script, first, second, and third. This may look strange, but
# unpack is probably the best word to describe what it does. It just says, Take whatever is in
# argv, unpack it, and assign it to all these variables on the left in order.
from sys import argv
script, first, second, third = argv
print "script is called", script
print "first var is", first
print "second var is", second
print "third var is", third
x = raw_input("4th variable is???")
print x

# $ python ex13.py first 2nd
#  Traceback (most recent call last):
#  File "ex13.py", line 3, in <module>
#  script, first, second, third = argv
#  ValueError: need more than 3 values to unpack

# This happens when you do not put enough arguments on the command when you run it (in
# this case just first 2nd). Notice when I run it I give it first 2nd, which caused it to give an
# error about need more than 3 values to unpack, telling you that you didnt give it enough
# parameters