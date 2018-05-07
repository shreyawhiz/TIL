counting = [1,2,3,4,5,6]
fruits = ["kiwi", "apple", "banana", "strawberry", "mango", "grapes"]

for count in counting:
	print count

for fruit in fruits:
	print fruit



new_array = []

for i in range(0,10):
	new_array.append(i)

for i in new_array:
	print i


i=0
new_array=[]
while i<10:
	new_array.append(i)
	i=i+1

print "new_array %s" %new_array


def create_arrays(count):
	new_array = []
	# method 1 :
	# for i in range(1,count+1):
	# 	new_array.append(i)
	
	# method 2 :
	i = 1
	while i < 11:
		new_array.append(i)
		i = i+1
	return new_array

arr = create_arrays(10)
print "arr created - %s" %arr