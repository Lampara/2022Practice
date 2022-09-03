# Python program showing inputing circle radius and getting area
import math
val = input("Enter radius of circle: ")
pie = (math.pi)
area = pie * (int(val) ** 2)
print("Area of " + val + " is " + str(area))
print("rounding to 2 decimals places is: " + str(round(area, 2)))

#adding this for September