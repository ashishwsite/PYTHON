# from turtle import *
import turtle
#this is librery which is help in drawing the diagrame of 
# Turtle name ka class hai jiska ek object t name se bana liya hua 
# t=Turtle()
# wn=Screen()
# wn.bgcolor("green")
# t.shape("turtle")
# t.speed(3)
# t.forward(25)
# t.clone()
pen=turtle.Turtle()
# ^YE EK CLASS AND US CLASS KA OBJECT KO  INTIALLIE KAR RAHA HAI 
# Turtle()=class
# turtle is library
# pen is onject of Turtle() calss
pen.shape("turtle")
# THIS IS FOR EQUILATERAL TRIANGLE DRAW
# for i in range(3):
#     pen.forward(60)
#     pen.right(120)
#FOR HEXAGONAL
for i in range(3):
    pen.right(60)
    pen.forward(60)
    pen.right(60)
    pen.forward(60)

turtle.done()