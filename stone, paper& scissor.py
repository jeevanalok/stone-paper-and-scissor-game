"""
simple pyhton program to play stone, paper and scissor
dt of completion-18 march 020
"""
#importing random module
import random
signs=["stone","paper","scissor"]
move_op=""
move_pl=""

#ps:-op=opponent
#    pl=player

points_op=0             #opponent's points
points_pl=0             #player's points

win_poss={"stone":"scissor","paper":"stone","scissor":"paper"}

#opponent move
def opponent():
    global move_op
    move_op=random.choice(signs)
    print("opponet's move=",move_op)
 
#player move
def player():
    global move_pl
    move_pl=input("choose your move:")
    
#scoring system using key and value of dictionary
def score():
    global points_pl,points_op
    if win_poss[move_op]==move_pl:
        points_op+=1
        print("opponent's points= ",points_op)
        print("player's points= ",points_pl)
    elif win_poss[move_pl]==move_op:
        points_pl+=1
        print("opponent's points= ",points_op)
        print("player's points= ",points_pl)
    else:
        print("draw")
        print("opponent's points= ",points_op)
        print("player's points= ",points_pl)


def win():
    if points_op==5 and points_op>points_pl:
        print("opponent wins")
    elif points_pl==5 and points_pl>points_op:
        print("player wins")

#loop till one reaches 5 points and wins
while points_op<5 and points_pl<5:
    player()
    opponent()
    score()
    win()