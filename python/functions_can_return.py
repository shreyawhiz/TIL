def add(a,b):
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



a = int(raw_input("Add numbers to add:"))