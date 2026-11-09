LAB = "turtlelab2.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.3",LAB)

from turtlelab2 import turtle,home,check
turtle.left(180)
turtle.forward(abs(home.x))
turtle.left(90)
turtle.left(180)
turtle.forward(abs(home.y))

check()