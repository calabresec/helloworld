# connect the Turtle and random libraries (aka "modules")
import turtle, random

# let's make a turtle
tina = turtle.Turtle()
tina.speed(10000)
# list of colors
colors = ["pink", "blue", "purple", "orange", "yellow", "cyan", "black", "brown", "red"]

# squiggles
number_line = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# random color picker
def color_tina():
    pick = random.randint(0, len(colors) - 1)
    tina.color(colors[pick])

    # octagons


def octagon(size):
    tina.color("purple")
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)


# squiggles multiply
tina.color("pink")
for number in number_line:
    tina.forward(number * 10)
    tina.left(60)
    tina.forward(number * 5)
    tina.left(60)


# let's make some methods, like plays in a playbook
def square(some_turtle):
    # stop writing
    some_turtle.penup()
    # go to the middle
    some_turtle.goto(0, 0)
    # start writing
    some_turtle.pendown()
    # go up
    some_turtle.goto(0, 50)
    # go right
    some_turtle.goto(50, 50)
    # go down
    some_turtle.goto(50, 0)
    # go back to the start
    some_turtle.goto(0, 0)

    # make a square


def squares(size):
    for x in range(1, 20):
        color.tina()
        tina.forward(size)
        tina.turn(90)


def super_circles(size):
    for x in range(1, 11):
        tina.color("red")
        tina.circle(size * x)


def octagons(size):
    for x in range(1, 11):
        octagon(size * x)


def spirals(size):
    for x in range(1, 50):
        tina.color("grey")
        tina.circle(size * x, 60)


# let's make tina draw that square
# she'll fill in the spot of "some_turtle"
square(tina)

# let's draw a circle in the middle
tina.goto(25, 0)
tina.circle(25)

# new Function
tina.circle(15)
super_circles(20)
octagons(25)

# at the end of my app, I will use a conditional
# a conditional is another word for "if statement"
answer = input("What next?")
print("You just said: " + answer)

if answer == "pizza":
    print(" I don't know how to draw a pizza")
elif answer == "spiral":
    print("Oh, I know that one!")
    spirals(20)
elif answer == "move":
    tina.goto(random.randint)(-200, 200), random.randint
else:
    print("that is not in my commands.")
