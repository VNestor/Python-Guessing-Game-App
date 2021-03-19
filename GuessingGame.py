# Build a guessing game using Python and Tkinter
# Tutoruial followed: https://levelup.gitconnected.com/learn-python-by-building-a-gui-guessing-game-with-tkinter-9f82291db6

# Victor Nestor
# March 16, 2021

# Player has three attempts to guess the secret number by clicking on the guess button
# If correct (guess equals secret number), then totalNumberofGuesses is incremented and labelNumGuess is updated
# If correct (continued), a label will state that the guess was correct in green and the game ends
# Guess buttons are disabled when game ends
# A 'Restart Game' option will be available, resetting all variables
# If guess is incorrect, hints will be displayed in red and the number of guess is incremented
# Game also ends when total number of guesses is equal to the number of allowable guesses (maximum)

# Tkinter: a python library for creating GUI widgets.
import tkinter as tk
from random import randrange


# Create library instace
window = tk.Tk()
# Window title
window.title("Guess The Number!")
# Disable windows from resizing
window.resizable(False, False)
window_height = 300
window_width = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,
                                     window_height, x_coordinate, y_coordinate))

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)


# Create widgets/labels
labelInstance = tk.Label(window, text="Guess a number from 0 to 9")
labelLine0 = tk.Label(
    window, text="------------------------------------------------------")
labelNumGuess = tk.Label(window, text="Number of guesses: 0")
labelMaxGuess = tk.Label(window, text="Max Guess: 3")
labelLine1 = tk.Label(
    window, text="------------------------------------------------------")
labelLogs = tk.Label(window, text="Game Logs")
labelLine2 = tk.Label(
    window, text="------------------------------------------------------")

# Create buttons
buttons = []
for index in range(0, 10):
    button = tk.Button(window, text=index, command=lambda index=index: process(
        index), state=tk.DISABLED)
    buttons.append(button)

buttonStartGameList = []
for index in range(0, 1):
    buttonStartGame = tk.Button(
        window, text="Start Game", command=lambda: startgame(index))
    buttonStartGameList.append(buttonStartGame)


# Append labels to grid
labelInstance.grid(row=0, column=0, columnspan=5)
labelLine0.grid(row=1, column=0, columnspan=5)
labelNumGuess.grid(row=2, column=0, columnspan=3)
labelMaxGuess.grid(row=2, column=3, columnspan=2)
labelLine1.grid(row=3, column=0, columnspan=5)
# Row 4 - 8 are reserved for logs
labelLogs.grid(row=4, column=0, columnspan=5)
labelLine2.grid(row=10, column=0, columnspan=5)

for row in range(0, 2):
    for col in range(0, 5):
        # Convert 2D index to 1D
        # 5 - total number of columns
        i = row * 5 + col
        buttons[i].grid(row=row + 10, column=col)

buttonStartGameList[0].grid(row=13, column=0, columnspan=5)

# Main game logic
# Declare variables
guess = 0
totalNumberOfGuesses = 0
secretNumber = randrange(10)
print(secretNumber)
labelLogs = []
guess_row = 4

# Reset all variables


def init():
    global buttons, guess, totalNumberOfGuesses, secretNumber, labelNumGuess, labelLogs, guess_row
    guess = 0
    totalNumberOfGuesses = 0
    secretNumber = randrange(10)
    print(secretNumber)
    labelNumGuess["text"] = "Guesses: 0"
    guess_row = 4

    # Remove all logs on init
    for labelLog in labelLogs:
        # Unmap widget from screen
        labelLog.grid_forget()
    labelLogs = []


def process(i):
    global totalNumberOfGuesses, buttons, guess_row
    guess = i

    totalNumberOfGuesses += 1
    labelNumGuess["text"] = "Guesses: " + str(totalNumberOfGuesses)

    # Check if guess matches secret number

    if guess == secretNumber:
        label = tk.Label(window, text="Correct! You Win!", fg='green')
        label.grid(row=guess_row, column=0, columnspan=5)
        labelLogs.append(label)
        guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED

    else:
        # Give player some hints
        if guess > secretNumber:
            label = tk.Label(
                window, text="The secret number is less than your current guess!", fg="red")
            label.grid(row=guess_row, column=0, columnspan=5)
            labelLogs.append(label)
            guess_row += 1

        else:
            label = tk.Label(
                window, text="The secret number is greater than your current guess!", fg="red")
            label.grid(row=guess_row, column=0, columnspan=5)
            labelLogs.append(label)
            guess_row += 1

    # Game is over when max number of guesses is reached

    if totalNumberOfGuesses == 3:
        if guess != secretNumber:
            label = tk.Label(
                window, text="You lost! You've reached the max number of guesses!", fg="red")
            label.grid(row=guess_row, column=0, columnspan=5)
            labelLogs.append(label)
            guess_row += 1

        for b in buttons:
            b["state"] = tk.DISABLED

    buttons[i]["state"] = tk.DISABLED


status = "none"


def startgame(i):
    global status
    for b in buttons:
        b["state"] = tk.NORMAL

    if status == "none":
        status = "started"
        buttonStartGameList[i]["text"] = "Restart Game"
    else:
        status = "restarted"
        init()
    print("Game Started")


# Infinite loop that keeps the program running until the player closes the app
window.mainloop()
