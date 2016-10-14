import turtle

def draw_square():
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(10)

	interval = 20

	for i in range(360/interval):
		for n in range(3):

			brad.forward(100)
			brad.right(90)
		
		brad.forward(100)
		brad.right(90+interval)

def draw_circle():
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)

def draw_triangle():
	tony = turtle.Turtle()

	for n in range(2):

		tony.forward(100)
		tony.right(120)
	
	tony.forward(100)

def draw_stuff():
	window = turtle.Screen()
	window.bgcolor("red")

	draw_square()
	draw_circle()
	draw_triangle()

	window.exitonclick()

draw_stuff()
