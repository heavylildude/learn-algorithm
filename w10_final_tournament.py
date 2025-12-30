#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TOURNAMENT OF LEGENDS: The "Bot Battle Royale" 🤖🏆
Imagine you're hosting a **rad** tournament where two AI bots battle it out to find a secret number.
This script pits **Binary Search Bot** (the smart one) vs. **Random Guess Bot** (the kook who just YOLOs it).
Who will win? Let's find out, brah!

**What's Happening?**
- **Binary Search Bot** uses the **gnarly** Binary Search algorithm (like a pro surfer riding the perfect wave).
- **Random Guess Bot** just **YOLOs** random numbers (like a kook wiping out every time).
- The **TARGET** is a secret number between 1 and 1000.
- We track how many turns each bot takes to find the target.
- The bot with the **fewest turns** wins the **Legendary Crown** 👑.

**JS Analogy:**
- Think of this like a `for` loop where each bot gets a turn to guess.
- The `target` is like a `const` that never changes.
- The `low` and `high` variables are like `let` variables that keep updating.
"""

import random

# 1. THE SETUP (The "Secret Number")
# The "Perfect" number the bots are trying to find (like the perfect wave height).
# JS Analogy: `const target = Math.floor(Math.random() * 1000) + 1;`
target = random.randint(1, 1000)

# 2. BOT A: Binary Search Bot (The "Smart Play")
# This bot uses **Binary Search**—it's like a pro surfer who knows exactly where to paddle.
# It starts in the middle and keeps halving the search space until it finds the target.
# JS Analogy: `function binarySearch(low, high) { return Math.floor((low + high) / 2); }`
def bot_a_logic(low, high):
    return (low + high) // 2  # Halve the search space (like cutting a pizza in half).

# 3. BOT B: Random Guess Bot (The "Kook Play")
# This bot **YOLOs** random numbers—it's like a kook who just paddles anywhere.
# It might get lucky, or it might wipe out forever.
# JS Analogy: `function randomGuess(low, high) { return Math.floor(Math.random() * (high - low + 1)) + low; }`
def bot_b_logic(low, high):
    return random.randint(low, high)  # YOLO: Pick a random number in the range.

# 4. THE BATTLE (The "Surf Off")
print(f"TARGET IS: {target}. START THE BATTLE! 🏄‍♂️🔥")

# We give each bot 20 turns to find the target (like a surf competition with a time limit).
low, high = 1, 1000  # Start with the full range (1-1000).
for turn in range(1, 21):
    # Bot A's Move (Binary Search)
    guess_a = bot_a_logic(low, high)
    print(f"Turn {turn} | Bot A guesses: {guess_a}")
    if guess_a == target:
        print("BOT A WINS! BINARY SEARCH RIZZ! 🏆")
        break  # Exit the loop if Bot A wins.
    elif guess_a < target:
        low = guess_a + 1  # Adjust the lower bound (like paddling left).
    else:
        high = guess_a - 1  # Adjust the upper bound (like paddling right).

    # Bot B's Move (Random Guess)
    # Reset bounds for Bot B (it doesn't learn from previous guesses).
    guess_b = bot_b_logic(1, 1000)
    print(f"Turn {turn} | Bot B guesses: {guess_b}")
    if guess_b == target:
        print("BOT B WINS! RANDOM LUCK? BOGUS! 🍀")
        break  # Exit the loop if Bot B wins.

# 5. CHALLENGE FOR STUDENTS (The "Homework")
# Replace these simple logics with your **project's A*** or **Minimax** bots.
# Make them battle for the **ultimate crown**! 👑
# Example:
#   - Use A* for pathfinding (like finding the shortest route to the target).
#   - Use Minimax for game theory (like a chess bot predicting moves).
print("\nCHALLENGE FOR STUDENTS:")
print("- Replace these simple logics with your project's A* or Minimax.")
print("- Make them battle for the ultimate crown! 👑")

# 6. THE RUBRIC (The "Logic Score")
# How do we judge the bots? Here's the **rad** rubric:
#   - **Efficiency (40%)**: Does the bot take the **shortest path** to the target?
#     (Binary Search Bot is **deadset** efficient—it finds the target in **10 turns or less**.)
#   - **Robustness (30%)**: Does it **crash** if given weird input?
#     (Random Guess Bot is **bogus**—it might never find the target.)
#   - **Clarity (20%)**: Is the code **clean** or a **total dumpster fire**?
#     (Binary Search Bot's code is **clean**—it's like a well-organized surfboard rack.)
#   - **Style (10%)**: Did they name their bot something **rad**?
#     (Binary Search Bot's name is **rad**—it's got **rizz**.)

# 7. SUMMARY (The "Big Picture")
# "Logic is the language of the universe. You just mastered the grammar. Absolute legend." 🌟
# - Binary Search is **gnarly**—it's fast and efficient.
# - Random Guess is **bogus**—it's slow and unreliable.
# - The best bot wins the **Legendary Crown** 👑.

# 🚨 DEPENDENCIES (Don't forget to install these, brah!)
# None! This script is **self-contained**—just run it with Python 3.

# 🏄‍♂️ LET'S SHRED! 🏄‍♂️