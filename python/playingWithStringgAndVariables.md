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

x = 'there are %d types of people' %10
binary = 'binary'
dont = 'dont'
print x
y = 'those who know %r and those who %s' %(binary,dont)
print y


print 'i said %s' %x
print 'i also said %s' %y


hilarious = 'false'
joke1 = "isnt this joke funny? - %s" %hilarious
print joke1
joke = "isnt this joke funny? - %s"
print joke % hilarious 
````

#### output

````javascript
python ex1.py
shreya owns a bmw
bmw is awesome
car_pool_capacity is - 400
car_pool_capacity is 400 and car_owner is shreya and space_in_car is 4
there are 10 types of people
those who know 'binary' and those who dont
i said there are 10 types of people
i also said those who know 'binary' and those who dont
isnt this joke funny? - false
isnt this joke funny? - false
````
