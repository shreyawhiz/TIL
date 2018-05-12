def add(a,b):
	"""
	This is add method
	"""
	# print "this is add"
	return a+b

def subtract(a,b):
	return a-b

def multiply(a,b):
	return a*b


def divide(a,b):
	return a/b

total_sum = add(5,6)
minus = subtract(10,2)

print "Sum returned is : %s and subtract result returned is : %s" %(total_sum,minus)

print "Complicated one line script -"
print add(divide(100,5), (divide(add(2,10), subtract(10,4))))
print add.__doc__



# a = int(raw_input("Add numbers to add:"))


# Every Python function returns a value; 
# if the function ever executes a return statement, it will return that value, otherwise
# it will return None, the Python null value.

# -------------------Documenting Functions------------------------
# You can document a Python function by giving it a doc string,
# like i did in the add function
# Everything between the triple quotes is the functions doc string, which documents what the function
# does. A doc string, if it exists, must be the first thing defined in a function 
# Can be accessed using __doc__ attribute which every python function has