import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # Create the turtle Brad - Draw a square
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("green")
    brad.speed(1)
    draw_square(brad)
    # Create the turtle Angie - Draw a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()

draw_art()
    
