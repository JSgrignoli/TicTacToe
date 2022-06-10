import turtle
s = turtle.getscreen()
t = turtle.Turtle()
turtle.title("TicTacToe")
t.speed(1)

def draw_board():
    # first horizontal line
    t.penup()
    t.goto(-200, 75)
    t.pendown()
    t.goto(200, 75)

    # second horizontal line
    t.penup()
    t.goto(-200, -75)
    t.pendown()
    t.goto(200, -75)

    # first vertical line
    t.penup()
    t.goto(-75, -200)
    t.pendown()
    t.goto(-75, 200)

    # second vertical line
    t.penup()
    t.goto(75, -200)
    t.pendown()
    t.goto(75, 200)






    input("Waiting")

draw_board()