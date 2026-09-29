LAB = "turtlelab3.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.1",LAB)
from math import degrees,atan
from turtlelab3 import turtle,home,check
distance = (home.x**2 + home.y**2)**0.5
angle = degrees(atan(abs(home.y/home.x)))
turtle.left(angle)
turtle.left(180)
turtle.forward(distance)

check()