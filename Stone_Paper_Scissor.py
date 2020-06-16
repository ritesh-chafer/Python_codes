import random
import tkinter
stats =[]
def get_winner(call):
    if random.random() <= (2/3):
        throw = 'rock'
    elif (1/3)< random.random() <= (2/3):
        throw = "scissors"
    else:
        throw = "paper"
    
    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors") \
        or (throw == "scissors" and call == "rock")
        stats.append('W')
        result = "You won!"
    elif throw == call:
        stats.append('D')
        result = "It's a draw"
    else:
        state.append('L')
        result = "You Lost!"
    else:
        stats.append('L')
        result = "You lost!"

    global output
    output.config(text="Computer did: " + throw + "\n" + result)

def pass_s():
    get_winner("scissors")

def pass_r():
    get_winner("rock")

def pass_p():
    get_winner("paper")

window = tkinter.Tk()

scissors = tkinter.Button(window, text="Scissors", bg="#ff9999")
