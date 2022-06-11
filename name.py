from re import L
import turtle
s = turtle.getscreen()
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

draw_board()

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


def h_line1():
    t.goto(-200, 150)
    t.pendown()
    t.goto(200, 150)
    t.penup()
def h_line2():
    t.goto(-200, 0)
    t.pendown()
    t.goto(200, 0)
    t.penup()
def h_line3():
    t.goto(-200, -150)
    t.pendown()
    t.goto(200, -150)
    t.penup()
def v_line1():
    t.goto(-150, 200)
    t.pendown()
    t.goto(-150, -200)
    t.penup()
def v_line2():
    t.goto(0, 200)
    t.pendown()
    t.goto(0, -200)
    t.penup()
def v_line3():
    t.goto(150, 200)
    t.pendown()
    t.goto(150, -200)
    t.penup()
def d_line1():
    t.goto(-200, -200)
    t.pendown()
    t.goto(200,200)
    t.penup()
def d_line2():
    t.goto(-200, 200)
    t.pendown()
    t.goto(200, -200)


#checks win condition
def win_check(player, move_list):
    if "A1" in move_list and "A2" in move_list and "A3" in move_list:
        winner = True
        h_line1()
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "B1" in move_list and "B2" in move_list and "B3" in move_list:
        winner = True
        h_line2()
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "C1" in move_list and "C2" in move_list and "C3" in move_list:
        winner = True
        h_line3()
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "A1" in move_list and "B2" in move_list and "C3" in move_list:
        winner = True
        d_line2()
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "C1" in move_list and "B2" in move_list and "A3" in move_list:
        winner = True
        d_line1()
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "A1" in move_list and "B1" in move_list and "C1" in move_list:
        winner = True
        v_line1()
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "A2" in move_list and "B2" in move_list and "C2" in move_list:
        winner = True
        v_line2()
        print( "{player} WINS!!".format(player = player))
        return winner
    elif "A3" in move_list and "B3" in move_list and "C3" in move_list:
        winner = True
        v_line3()
        print( "{player} WINS!!".format(player = player))
        return winner
    elif move_set == []:
        print("TIE GAME!")
        winner = True
        return winner
    else:
        winner = False 
        return winner



#Game play code
move_set = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
player1_moves = []
player2_moves = []
player1 = input("Player 1 please enter name: ")
player2 = input("Player 2 please enter name: ")

#Game loop
def player_turn(player, player_moves):
    choice = input("{player} choose you're next move ".format(player = player))
    choice = choice.upper()
    valid_choice = False
    while valid_choice == False:
        if choice not in move_set:
            print("Invalid move.")
            choice = input("{player} choose you're next move ".format(player = player))
            choice = choice.upper()
        else:
            valid_choice = True
            
    player_moves.append(choice)
    move_set.remove(choice)
    if player == player1:
        circle_plays(choice)
    else:
        x_plays(choice)


         
win = False
while win == False:
    player_turn(player1, player1_moves)
    win = win_check(player1, player1_moves)
    if win == False:
        player_turn(player2, player2_moves)
        win = win_check(player2, player2_moves)

input("Game OVER! \n Press any key to exit. ")
