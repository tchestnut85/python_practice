from colors_model import Colors
import turtle as t


def draw_painting(rows=10, cols=10):
    X_POSITION = -300
    y_position = -300

    t.colormode(255)
    turtle = t.Turtle()
    turtle.hideturtle()
    turtle.speed("fastest")
    colors = Colors()

    for _ in range(rows):
        turtle.up()
        turtle.goto(X_POSITION, y_position)
        for _ in range(cols):
            random_color = colors.get_random_color()
            turtle.color(random_color)
            turtle.down()
            turtle.dot(20)
            turtle.up()
            turtle.forward(50)
        y_position += 50

    screen = t.Screen()
    screen.exitonclick()


draw_painting()
