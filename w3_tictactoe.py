#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TIC-TAC-TOE AI BOSS (The "No U" Algorithm)

Imagine you're playing Tic-Tac-Toe with your little bro, and he's
**cooked** because you always win. This AI is like that—it **never loses**.
It's the ultimate "No U" of algorithms. Deadset.

Think of it like this:
- **AI (1)** = You (the boss who always wins)
- **Human (-1)** = Your little bro (who always loses)
- **Empty (0)** = The spots where you're about to **shred** him
"""

import math  # Math = The "Brain Juice" for calculating moves

# 1. THE BOARD (The "Battlefield")
# 0 = Empty (no one's claimed it yet)
# 1 = AI (you, the boss)
# -1 = Human (your little bro, the kook)
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# 2. CHECK WIN (The "Boss Detector")
# This function checks if someone won (or if it's a tie).
# It's like looking at the board and going, "Yo, someone just got **shredded**."
def check_win(b):
    # Win states = The "Gnarly Lines" where you can win
    # (rows, columns, diagonals)
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows (horizontal shred)
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns (vertical shred)
        [0, 4, 8], [2, 4, 6]              # Diagonals (the "X marks the spot" shred)
    ]

    # Loop through all win states to see if someone won
    for state in win_states:
        # If all 3 spots in a line are the same (and not empty), someone won!
        if b[state[0]] == b[state[1]] == b[state[2]] != 0:
            return b[state[0]]  # Return 1 (AI) or -1 (Human)

    # If no one won and there's no empty spots left, it's a tie
    if 0 not in b:
        return 0  # Tie = "Bogus, no one wins"

    # If no one won and there's still empty spots, keep playing
    return None  # "Keep shredding, brah"

# 3. MINIMAX (The "Crystal Ball")
# This is the **gnarly** part. It's like the AI can see **all possible futures**
# and picks the one where it **always wins** (or at least ties).
#
# Think of it like this:
# - **Maximizing (AI)** = You trying to **shred** your little bro
# - **Minimizing (Human)** = Your little bro trying to **not get shredded**
# - **Depth** = How far ahead the AI is thinking (like 3 moves ahead)
def minimax(b, depth, is_maximizing):
    # First, check if someone won or if it's a tie
    result = check_win(b)
    if result is not None:
        return result  # Return 1 (AI wins), -1 (Human wins), or 0 (tie)

    # If it's the AI's turn (maximizing), it wants the **highest score**
    if is_maximizing:
        best_score = -math.inf  # Start with the worst possible score (-∞)
        for i in range(9):  # Loop through all spots on the board
            if b[i] == 0:  # If the spot is empty
                b[i] = 1  # AI takes the spot (like claiming it)
                # Recursively call minimax to see what happens next
                score = minimax(b, depth + 1, False)
                b[i] = 0  # Undo the move (like a time machine)
                best_score = max(score, best_score)  # Keep the best score
        return best_score  # Return the best score the AI can get

    # If it's the human's turn (minimizing), they want the **lowest score**
    else:
        best_score = math.inf  # Start with the best possible score (∞)
        for i in range(9):  # Loop through all spots on the board
            if b[i] == 0:  # If the spot is empty
                b[i] = -1  # Human takes the spot
                # Recursively call minimax to see what happens next
                score = minimax(b, depth + 1, True)
                b[i] = 0  # Undo the move
                best_score = min(score, best_score)  # Keep the worst score
        return best_score  # Return the worst score the human can force

# 4. GET BEST MOVE (The "Boss Move Finder")
# This function finds the **best move** for the AI.
# It's like the AI looking at the board and going, "Yo, this move is **cooked**."
def get_best_move(b):
    best_score = -math.inf  # Start with the worst possible score
    move = -1  # Start with no move
    for i in range(9):  # Loop through all spots on the board
        if b[i] == 0:  # If the spot is empty
            b[i] = 1  # AI takes the spot (like testing it)
            # Call minimax to see how good this move is
            score = minimax(b, 0, False)
            b[i] = 0  # Undo the move
            # If this move is better than the current best, update the best move
            if score > best_score:
                best_score = score
                move = i
    return move  # Return the best move (0-8)

# 5. TEST THE AI (The "Shred Session")
print("AI is thinking... calculating every outcome...")
m = get_best_move(board)  # AI picks the best move
print(f"AI plays at position: {m}")  # Print the move (should be 4, the center)

# 6. PLAY AGAINST THE AI (The "Boss Battle")
# Now you can play against the AI! It's like challenging your little bro,
# but this time, he's **unbeatable**.
#
# How to play:
# - Input a number (0-8) to place your move.
# - The AI will respond with its move.
# - Try to beat it... if you can. (Spoiler: You can't. It's **cooked**.)

print("\nLet's play! You're -1, AI is 1. Enter a number (0-8) to make your move:")

# Print the board (for reference)
def print_board(b):
    print("\nCurrent board:")
    for i in range(3):
        print(f" {b[i*3]} | {b[i*3+1]} | {b[i*3+2]} ")
        if i < 2:
            print("-----------")

print_board(board)

# Game loop (the "Boss Battle")
while True:
    # Human's turn
    try:
        human_move = int(input("Your move (0-8): "))
        if board[human_move] != 0:
            print("Bogus move, brah! That spot's already taken.")
            continue
        board[human_move] = -1  # Human takes the spot
    except (ValueError, IndexError):
        print("Bogus input, brah! Enter a number between 0 and 8.")
        continue

    # Check if human won
    if check_win(board) == -1:
        print_board(board)
        print("You win! ...Wait, how? Did you cheat?")
        break
    elif check_win(board) == 0:
        print_board(board)
        print("Tie! You're lucky, brah.")
        break

    # AI's turn
    print("AI is thinking...")
    ai_move = get_best_move(board)
    board[ai_move] = 1  # AI takes the spot
    print(f"AI plays at position: {ai_move}")

    # Check if AI won
    if check_win(board) == 1:
        print_board(board)
        print("AI wins! Told you it's **cooked**.")
        break
    elif check_win(board) == 0:
        print_board(board)
        print("Tie! You got lucky, brah.")
        break

    # Print the board after each move
    print_board(board)

# 7. THE ROAST (The "Final Verdict")
# If you somehow beat this AI, your minimax logic is **bogus**.
# Go back and check the `if is_maximizing` block—you probably messed it up.
#
# Summary: "You just built a bot that never loses. It’s the ultimate 'No U' of algorithms. Deadset."