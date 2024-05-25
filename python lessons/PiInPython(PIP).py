import math
print("Circles in Extent")

radius = float(input("Provide the radius of the circle to see it's respective area and circunference. Radius: "))

area = math.pi*(radius*radius)
#radius ** 2 or (radius**2)
circunference = 2*math.pi*radius
#Always write the module that is been used like the above.

print("Here it is! \nThe Area:", round(area,3), "\nThe Circunference", round(circunference,3))

#If you use Radius: 3 without round() function, you shall get results like follow.
#Here it is! 
#The Area: 28.274333882308138 
#The Circunference 18.84955592153876
#With the Round( radius, 3) you shall get: Here it is! 
#The Area: 28.274 
#The Circunference 18.85
