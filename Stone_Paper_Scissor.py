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
    
    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors") or (throw == "scissors" and call == "rock"):
        stats.append('W')
        result = "You won!"
    elif throw == call:
        stats.append('D')
        result = "It's a draw"
    else:
        stats.append('L')
        result = "You Lost!"

    global output
    output.config(text="Computer did: " + throw + "\n" + result)

def pass_s():
    get_winner("scissors")

def pass_r():
    get_winner("rock")

def pass_p():
    get_winner("paper")

window = tkinter.Tk()

scissors = tkinter.Button(window, text="Scissors", bg="#4864E6",padx = 15, pady = 10, command= pass_s, width=40, height=5)
rock = tkinter.Button(window, text="Rock", bg="#ff9999",padx = 15, pady = 10, command= pass_r, width=40,height=5)
paper = tkinter.Button(window, text="Paper", bg="#9c88ff",padx = 15, pady = 10, command= pass_p, width=40, height=5)
output = tkinter.Label(window, fg="black", text = "What's your call",width=40, height=5)

scissors.pack(side="left")
rock.pack(side="left")
paper.pack(side="left")
output.pack(side="right")
window.mainloop()

for i in stats:
    print(i, end=" ")
    if stats.count('L') > stats.count('W'):
        result = "\nYou loose the series."
    elif stats.count('L') == stats.count('W'):
        result = "\Series ended in a draw."
    else:
        result = "\nYou win the series."

print(result)