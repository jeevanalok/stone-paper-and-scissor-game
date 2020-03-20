"""  
this is a simple GUI game design of stone paper and scissor using tkinter.
dt of completion-20 march 2020
"""


#importing the necessary modules

import tkinter as tk
from tkinter import messagebox
import random

window=tk.Tk()
window.geometry("480x360")
window.config(bg="#3866d1") 
window.title("rock,paper &scissor")

win_poss={"stone":"scissor","paper":"stone","scissor":"paper"}

move_op=""
move_pl=""
points_op=0
points_pl=0

#score labels to keep track
points_op_label=tk.Label(window,text="opponent points:{0}".format(points_op),bg="#3866d1").grid(row=0,column=0)
points_pl_label=tk.Label(window,text="player points:{0}".format(points_pl),bg="#3866d1").grid(row=1,column=0)


def opponent():
    global move_op
    move_op=random.choice(["stone","paper","scissor"])
    move_op_label=tk.Label(window,text="opponent's choice:{0}".format(move_op),font=("courier",25)).place(relx=0.5,rely=0.4,anchor="center")

#player starts the game by pressing his choice
#then opponent/comp chooses
#then game continues until one scores 5
#game collapses

def stone_mv():
    global move_pl
    move_pl="stone"
    opponent()
    score()
    points_op_label=tk.Label(window,text="opponent points:{0}".format(points_op),bg="#3866d1").grid(row=0,column=0)
    points_pl_label=tk.Label(window,text="player points:{0}".format(points_pl),bg="#3866d1").grid(row=1,column=0)
    win()

def paper_mv():
    global move_pl
    move_pl="paper"
    opponent()
    score()
    points_op_label=tk.Label(window,text="opponent points:{0}".format(points_op),bg="#3866d1").grid(row=0,column=0)
    points_pl_label=tk.Label(window,text="player points:{0}".format(points_pl),bg="#3866d1").grid(row=1,column=0)
    win()

def scissor_mv():
    global move_pl
    move_pl="scissor"
    opponent()
    points_op_label=tk.Label(window,text="opponent points:{0}".format(points_op),bg="#3866d1").grid(row=0,column=0)
    points_pl_label=tk.Label(window,text="player points:{0}".format(points_pl),bg="#3866d1").grid(row=1,column=0)
    score()
    win()
#buttons for player
stone=tk.Button(window,text="STONE",height=3,width=5,command=stone_mv).place(relx=0.3,rely=0.9,anchor="s")
paper=tk.Button(window,text="PAPER",height=3,width=5,command=paper_mv).place(relx=0.5,rely=0.9,anchor="s")
scissor=tk.Button(window,text="SCISSOR",height=3,width=5,command=scissor_mv).place(relx=0.7,rely=0.9,anchor="s")

#scoring system:"matching keys to values in dictionary"


def score():
    global points_pl,points_op
    if win_poss[move_op]==move_pl:
        points_op+=1
        window.config(bg="red")
    elif win_poss[move_pl]==move_op:
        points_pl+=1
        window.config(bg="green")
    else:
        points_op+=0
        points_pl+=0
    

def win():
    if points_op==5 and points_op>points_pl:
        msg=messagebox.showinfo("result","opponent wins!")
        quit_x=tk.Button(window,text="QUIT",fg="red").after(1000,window.destroy)
    elif points_pl==5 and points_pl>points_op:
        msg=messagebox.showinfo("result"," player wins!")
        quit_x=tk.Button(window,text="QUIT",fg="red").after(1000,window.destroy)

    
window.mainloop()


