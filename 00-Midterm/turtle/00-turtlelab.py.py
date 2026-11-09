LAB = "turtlelab4.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.1",LAB)

from turtlelab4 import turtle,check

def paint_square(size):
    """Commands the Turtle to paint a square of the size specified"""
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)

def paint_triangle(size):
    """Commands the Turtle to paint a triangle of the size specified"""
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
paint_square(50)

paint_triangle(200)
check()