LAB = "turtlelab9.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)



from turtlelab9 import turtle, check

def visit_line(num_houses):
    for i in range(num_houses):
        turtle.forward(i*50)
        turtle.backward(i*50)

# East
visit_line(6)

# North-East
turtle.left(45)
visit_line(6)

# North
turtle.left(45)
visit_line(6)

# North-West
turtle.left(45)
visit_line(6)

# West
turtle.left(45)
visit_line(6)

# South-West
turtle.left(45)
visit_line(6)

# South
turtle.left(45)
visit_line(6)

# South-East
turtle.left(45)
visit_line(6)

check()
