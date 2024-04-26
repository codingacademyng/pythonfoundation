import tkinter as tk
from tkinter import messagebox

current_player = 'X'
board = [" " for _ in range(9)]

# Function to handle button clicks
def button_click(index):
    global current_player

    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)
        if check_winner(current_player):
            for i in winning_combinations[winning_index]:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_board()
        elif " " not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_board()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Function to check for a win
def check_winner(player):
    global winning_index
    for idx, combo in enumerate(winning_combinations):
        if all([board[i] == player for i in combo]):
            winning_index = idx
            return True
    return False

# Function to reset the game
def reset_board():
    global current_player, board
    current_player = 'X'
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace")

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons
buttons = [tk.Button(root, text=" ", width=10, height=3, command=lambda i=i: button_click(i)) for i in range(9)]

# Layout buttons in a 3x3 grid
for i in range(3):
    for j in range(3):
        buttons[i * 3 + j].grid(row=i, column=j)

# Define winning combinations
winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]
winning_index = 0

# Start the main loop
root.mainloop()
