#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BENCHMARKING: The "Stopwatch for Code" 🏁⏱️

Imagine you're a surfer trying to beat your personal best time on a wave.
You grab a stopwatch, hit "Start" when you paddle out, and hit "Stop" when you land the trick.
That's **benchmarking**—measuring how fast your code runs!

This script is like a **digital stopwatch** for your algorithms.
We'll use it to time how long it takes for your AI to "think" (like checking moves in chess or solving a maze).
"""

# 🚀 THE STOPWATCH (Python's `time` module)
# This is like the stopwatch on your phone—it tells us how long stuff takes.
# In JS, this would be like `console.time()` and `console.timeEnd()`.
import time

def my_algorithm():
    """
    THE "BRAIN THINK" SIMULATOR 🧠
    Imagine this is your AI "thinking" really hard.
    It's like a surfer counting waves before paddling out.

    What it does:
    - Counts from 0 to 999,999 (like checking a million moves in chess).
    - Returns the total number of "nodes" (moves) it checked.
    - In JS, this would be like a `for` loop that runs a million times.
    """
    nodes_checked = 0  # Start with "zero moves checked" (like a surfer starting at 0 waves)

    # THE "THINKING" LOOP (Like checking moves one by one)
    # This is like a surfer saying: "Wave 1... Wave 2... Wave 3..."
    for i in range(1000000):  # 1 million "waves" (or chess moves)
        nodes_checked += 1  # "I checked another move!" (or "I saw another wave!")

    return nodes_checked  # "I checked 1 million moves, brah!"

# 🏁 THE RACE BEGINS (Benchmarking Time!)
# Step 1: Start the stopwatch (like hitting "Start" on your phone)
# In JS, this would be `console.time("myAlgorithm")`.
start_time = time.time()  # "Stopwatch started! Go!"

# Step 2: Run the algorithm (let the AI "think")
# This is like your AI saying: "Okay, let me check all these moves..."
total_nodes = my_algorithm()  # "I checked 1 million moves!"

# Step 3: Stop the stopwatch (like hitting "Stop" on your phone)
# In JS, this would be `console.timeEnd("myAlgorithm")`.
end_time = time.time()  # "Stopwatch stopped! How long did I take?"

# 📊 THE RESULTS (How fast was your AI?)
# Calculate how long it took (like checking your surf time).
duration = end_time - start_time  # "Total time = Stop time - Start time"

# Print the results (like showing off your surf score).
print(f"Nodes Checked: {total_nodes}")  # "I checked 1 million moves!"
print(f"Time Taken: {duration:.4f} seconds")  # "It took me 0.1234 seconds, brah!"

# 🎯 THE CHALLENGE (Make Your Code Faster!)
# Now it's your turn to **optimize** (make your code faster).
# Here’s what you can do:

# Challenge 1: Time Your Own Code
# Wrap your **Week 2 (A*)** or **Week 3 (Minimax)** code in this stopwatch.
# Example:
#   start_time = time.time()
#   best_move = minimax(board, depth=5)  # Your AI's "thinking" function
#   end_time = time.time()
#   print(f"Time Taken: {end_time - start_time:.4f} seconds")

# Challenge 2: Make It Faster by 20%
# Try to reduce the "Time Taken" by **20%** by:
#   - Adding a `Visited` set (like a surfer remembering which waves they already checked).
#     Example:
#       visited = set()  # "I already checked this move, skip it!"
#       if move not in visited:
#           check_move(move)
#           visited.add(move)
#   - Making your `if` statements smarter (like a surfer avoiding bad waves).
#     Example:
#       # Bad: Check every move, even the stupid ones
#       for move in all_moves:
#           if is_valid(move):  # Only check if it's a good move
#               check_move(move)

# Challenge 3: The Experiment (Minimax Depth Test)
# If you're doing **Minimax**, try changing the `depth` from **5 to 3**.
# Example:
#   best_move = minimax(board, depth=3)  # Instead of depth=5
# Questions to ask:
#   - How much **faster** is it? (Check the "Time Taken")
#   - Is it still **smart enough** to beat you? (Play against it!)

# Challenge 4: Write a "Performance Report"
# Add a comment at the end of your code like this:
#   """
#   PERFORMANCE REPORT:
#   - My bot checks 50,000 moves in 0.2 seconds. No cap.
#   - With depth=3, it’s 3x faster but still beats me 70% of the time.
#   - Adding a `Visited` set made it 15% faster. Gnarly!
#   """

# 🏆 SUMMARY: "Speed is Rizz. A Fast Bot is a Winning Bot."
# - Benchmarking = The "stopwatch" for your code.
# - Faster code = More moves checked in less time = Smarter AI.
# - Optimize by: Using `Visited` sets, smarter `if` statements, and tuning depth.
# - Always write a **Performance Report** to track your progress!

# Now go **shred** that code, brah! 🤙