import math
def circle_stats(radius):
   area = (radius**2)*math.pi
   circumference = 2*math.pi*radius
   return round(area,2),round(circumference,2)

a,c = circle_stats(9)

print("Area :",a," Circumference :",c)