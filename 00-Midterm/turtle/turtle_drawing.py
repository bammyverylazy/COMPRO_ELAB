LAB = "turtlelab6.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.7",LAB)

from turtlelab6 import turtle,home,rocky,mozart,check
from math import sqrt,atan2,degrees
def cal_displacement(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)
def walkto(x,y):
    """Have Turtle walk straight to location (x,y)"""
    dx = x - turtle.x
    dy = y - turtle.y
    dist = sqrt(dx**2 + dy**2)
    angle = degrees(atan2(dy,dx))
    turtle.left(angle-turtle.heading) # Turtle's current heading may not be 0
    turtle.forward(dist)

sum_dis_r_t=cal_displacement(rocky.x,rocky.y,turtle.x,turtle.y)
sum_dis_m_t=cal_displacement(mozart.x,mozart.y,turtle.x,turtle.y)
sum_dis_r_h=cal_displacement(rocky.x,rocky.y,home.x,home.y)
sum_dis_m_h=cal_displacement(mozart.x,mozart.y,home.x,home.y)
sum_dis_r_m=cal_displacement(rocky.x,rocky.y,mozart.x,mozart.y)

comb1=sum_dis_r_t+ sum_dis_r_h+sum_dis_r_m
comb2=sum_dis_m_t+sum_dis_m_h+sum_dis_r_m
if comb1>=comb2:
    walkto(rocky.x,rocky.y)
    walkto(mozart.x,mozart.y)
    walkto(home.x,home.y)
else:
    walkto(mozart.x,mozart.y)
    walkto(rocky.x,rocky.y)
    walkto(home.x,home.y)

check()