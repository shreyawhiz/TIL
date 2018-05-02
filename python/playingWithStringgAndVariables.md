### Different ways of printing string and variables

1. ex1.py
````javascript
car_model = "bmw"
car_owner = "shreya"
print car_owner, "owns a", car_model
print car_model, "is awesome"
space_in_car = 4
car_pool_capacity = 100*space_in_car
print "car_pool_capacity is -", car_pool_capacity
print "car_pool_capacity is %s and car_owner is %s and space_in_car is %d" %(car_pool_capacity,car_owner,space_in_car)

print "." * 10


x = 'there are %d types of people' %10
binary = 'binary'
dont = 'dont'
print x
y = 'those who know %r and those who %s' %(binary,dont)
print y

print "." * 10


print 'i said "%s"' %x
print 'i also said "%s"' %y

print "." * 10

hilarious = 'false'
joke1 = "isnt this joke funny? - %s" % hilarious
print joke1
joke = "isnt this joke funny? - %s"
print joke % hilarious 

print "." * 10

left = "left side of a string...."
right = "right side of a string"
print left + right

print "." * 10

print "mary had a little lamb"
print "its fleece was as white as %s" % 'snow'

print "." * 10

var1 = "C"
var2 = "h"
var3 = "e"
var4 = "e"
var5 = "s"
var6 = "e"
var7 = "B"
var8 = "u"
var9 = "r"
var10 = "g"
var11 = "e"
var12 = "r"

print var1 + var2 + var3 + var4 + var5 + var6
print var7 + var8 + var9 + var10 + var11 + var12

print var1 + var2 + var3 + var4 + var5 + var6,
print var7 + var8 + var9 + var10 + var11 + var12

````

#### output

````javascript
python ex1.py
shreya owns a bmw
bmw is awesome
car_pool_capacity is - 400
car_pool_capacity is 400 and car_owner is shreya and space_in_car is 4
..........
there are 10 types of people
those who know 'binary' and those who dont
..........
i said "there are 10 types of people"
i also said "those who know 'binary' and those who dont"
..........
isnt this joke funny? - false
isnt this joke funny? - false
..........
left side of a string....right side of a string
..........
mary had a little lamb
its fleece was as white as snow
..........
Cheese
Burger
Cheese Burger
````
