# # TIC-TAC-TOE
# # original method
# def tictak(moves):
#     for row in range(5):
#         if row % 2 == 0:
#             rowplace = int(row/2)
#             for column in range(5):
#                 columnplace = int(column/2)
#                 if column % 2 == 0:
#                     if column != 4:
#                         print(moves[rowplace][columnplace], end="")
#                     else:
#                         print(moves[rowplace][columnplace])
#                 else:
#                     print("|", end="")
#         else:
#             print("-----")


# player = 1
# movesList = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# while True:
#     columnIndex = int(input("Enter the column of your move: "))
#     rowIndex = int(input("Enter the row of your move: "))
#     if player == 1:
#         if movesList[columnIndex][rowIndex] == " ":
#             movesList[columnIndex][rowIndex] = "X"
#             player = 2
#         else:
#             print("Make another move")
#     elif player == 2:
#         if movesList[columnIndex][rowIndex] == " ":
#             movesList[columnIndex][rowIndex] = "Y"
#             player = 1
#         else:
#             print("Make another move")
#     tictak(movesList)
#     if movesList[0][0] == "X" and movesList[0][1] == "X" and movesList[0][2] == "X":
#         print("Congrats! Player 1 wins")
#         break
#     elif movesList[1][0] == "X" and movesList[1][1] == "X" and movesList[1][2] == "X":
#         print("Congrats! Player 1 wins")
#         break
#     elif movesList[2][0] == "X" and movesList[2][1] == "X" and movesList[2][2] == "X":
#         print("Congrats! Player 1 wins")
#         break
#     elif movesList[0][0] == "X" and movesList[1][0] == "X" and movesList[2][0] == "X":
#         print("Congrats! Player 1 wins")
#         break
#     elif movesList[0][1] == "X" and movesList[1][1] == "X" and movesList[2][1] == "X":
#         print("Congrats! Player 1 wins")
#         break
#     elif movesList[0][2] == "X" and movesList[1][2] == "X" and movesList[2][2] == "X":
#         print("Congrats! Player 1 wins")
#         break
#     elif movesList[0][0] == "X" and movesList[1][1] == "X" and movesList[2][2] == "X":
#         print("Congrats! Player 1 wins")
#         break
#     elif movesList[0][2] == "X" and movesList[1][1] == "X" and movesList[2][0] == "X":
#         print("Congrats! Player 1 wins")
#         break

#     if movesList[0][0] == "Y" and movesList[0][1] == "Y" and movesList[0][2] == "Y":
#         print("Congrats! Player 2 wins")
#         break
#     elif movesList[1][0] == "Y" and movesList[1][1] == "Y" and movesList[1][2] == "Y":
#         print("Congrats! Player 2 wins")
#         break
#     elif movesList[2][0] == "Y" and movesList[2][1] == "Y" and movesList[2][2] == "Y":
#         print("Congrats! Player 2 wins")
#         break
#     elif movesList[0][0] == "Y" and movesList[1][0] == "Y" and movesList[2][0] == "Y":
#         print("Congrats! Player 2 wins")
#         break
#     elif movesList[0][1] == "Y" and movesList[1][1] == "Y" and movesList[2][1] == "Y":
#         print("Congrats! Player 2 wins")
#         break
#     elif movesList[0][2] == "Y" and movesList[1][2] == "Y" and movesList[2][2] == "Y":
#         print("Congrats! Player 2 wins")
#         break
#     elif movesList[0][0] == "Y" and movesList[1][1] == "Y" and movesList[2][2] == "Y":
#         print("Congrats! Player 2 wins")
#         break
#     elif movesList[0][2] == "Y" and movesList[1][1] == "Y" and movesList[2][0] == "Y":
#         print("Congrats! Player 2 wins")
#         break




# REVISED METHOD
# board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# def print_board():
#     for row in board:
#         print(' | '.join(row))
#         print('-' * 9)

# def check_win(player):
#     for i in range(3):
#         # Check rows and columns
#         if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
#             return True

#     # Check diagonals
#     if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
#         return True

#     return False

# def check_tie():
#     for row in board:
#         if " " in row:
#             return False
#     return True

# current_player = 'X'
# while True:
#     print_board()
#     row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
#     col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

#     if board[row][col] == ' ':
#         board[row][col] = current_player
#     else:
#         print("That cell is already occupied. Try again.")
#         continue

#     if check_win(current_player):
#         print_board()
#         print(f"Player {current_player} wins! Congratulations!")
#         break

#     if check_tie():
#         print_board()
#         print("It's a tie!")
#         break

#     if current_player == "X":
#         current_player = "Y"
#     elif current_player == "Y":
#         current_player = "X"


# SIMPLIFIED CHECK WIN METHOD
# def check_win(player):
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] == player:
#             return True

#     for j in range(3):
#         if board[0][j] == board[1][j] == board[2][j] == player:
#             return True

#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2] == player or \
#        board[0][2] == board[1][1] == board[2][0] == player:
#         return True

#     return False




# row_result = all(board[0][j] == " " for j in range(3))
# print(row_result)
# myli = []

# for j in range(3):
#     myli.append(board[0][i] == " ")
# print(all(myli))

