import turtle
# s = turtle.getscreen()
t = turtle.Turtle()
t.clearstamps
turtle.title("TicTacToe")
t.speed(5)

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
    t.penup()

    input("Waiting\n")

# draw_board()

def circle_plays(choice):
    
    choice = choice.upper()
    if choice == "A1":
        t.goto(-150, 100)
        t.pendown()
        t.circle(50)
        t.penup()
    elif choice == "A2":
        t.goto(0, 100)
        t.pendown()
        t.circle(50)
        t.penup()
    elif choice == "A3":
        t.goto(150, 100)
        t.pendown()
        t.circle(50)
        t.penup()
    elif choice == "B1":
        t.goto(-150, -50)
        t.pendown()
        t.circle(50)
        t.penup()
    elif choice == "B2":
        t.goto(0, -50)
        t.pendown()
        t.circle(50)
        t.penup()
    elif choice == "B3":
        t.goto(150, -50)
        t.pendown()
        t.circle(50)
        t.penup()
    elif choice == "C1":
        t.goto(-150, -200)
        t.pendown()
        t.circle(50)
        t.penup()
    elif choice == "C2":
        t.goto(0, -200)
        t.pendown()
        t.circle(50)
        t.penup()
    elif choice == "C3":
        t.goto(150, -200)
        t.pendown()
        t.circle(50)
        t.penup()


def x_plays(choice):
    
    choice = choice.upper()
    if choice == "A1":
        t.goto(-175, 100)
        t.pendown()
        t.goto(-100, 175)
        t.penup()
        t.goto(-175, 175)
        t.pendown()
        t.goto(-100, 100)
        t.penup()
    elif choice == "A2":
        t.goto(-50, 100)
        t.pendown()
        t.goto(50, 175)
        t.penup()
        t.goto(-50, 175)
        t.pendown()
        t.goto(50, 100)
        t.penup()
    elif choice == "A3":
        t.goto(100, 100)
        t.pendown()
        t.goto(175, 175)
        t.penup()
        t.goto(100, 175)
        t.pendown()
        t.goto(175, 100)
        t.penup()
    elif choice == "B1":
        t.goto(-175, -50)
        t.pendown()
        t.goto(-100, 50)
        t.penup()
        t.goto(-175, 50)
        t.pendown()
        t.goto(-100, -50)
        t.penup()
    elif choice == "B2":
        t.goto(-50, -50)
        t.pendown()
        t.goto(50, 50)
        t.penup()
        t.goto(-50, 50)
        t.pendown()
        t.goto(50, -50)
        t.penup()
    elif choice == "B3":
        t.goto(100, -50)
        t.pendown()
        t.goto(175, 50)
        t.penup()
        t.goto(100, 50)
        t.pendown()
        t.goto(175, -50)
        t.penup()
    elif choice == "C1":
        t.goto(-175, -175)
        t.pendown()
        t.goto(-100, -100)
        t.penup()
        t.goto(-175, -100)
        t.pendown()
        t.goto(-100, -175)
        t.penup()
    elif choice == "C2":
        t.goto(-50, -175)
        t.pendown()
        t.goto(50, -100)
        t.penup()
        t.goto(-50, -100)
        t.pendown()
        t.goto(50, -175)
        t.penup()
    elif choice == "C3":
        t.goto(100, -175)
        t.pendown()
        t.goto(175, -100)
        t.penup()
        t.goto(100, -100)
        t.pendown()
        t.goto(175, -175)
        t.penup()

#checks win condition
def win_check(player, move_list, winner):
    if "A1" in move_list and "A2" in move_list and "A3" in move_list:
        winner = True
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "B1" in move_list and "B2" in move_list and "B3" in move_list:
        winner = True
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "C1" in move_list and "C2" in move_list and "C3" in move_list:
        winner = True
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "A1" in move_list and "B2" in move_list and "C3" in move_list:
        winner = True
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "C1" in move_list and "B2" in move_list and "A3" in move_list:
        winner = True
        print( "{player} WINS!!".format(player = player))
        return winner
    else:
        winner = False 
        print("keep playing")
        return winner



#Game play code
move_set = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
player1_moves = []
player2_moves = []
player1 = input("Player 1 please enter name: ")
player2 = input("Player 2 please enter name: ")

#Game loop
winner = False
while winner == False:
    choice = input("{player} choose you're next move ".format(player = player1))
    choice = choice.upper()
    if choice not in move_set:
        print("Invalid move.")
    else:
        player1_moves.append(choice)
        move_set.remove(choice)
        #circle_plays(choice)
        print(player1_moves)
        print(move_set)
        win_check(player1, player1_moves, winner)


