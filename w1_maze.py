#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# """
# MAZE SOLVER (The "Digital Hide & Seek")
# 
# Imagine you're a little robot trying to find the "Exit" in a simple grid.
# - 0 = Path (where you can walk)
# - 1 = Wall (you can't walk through)
# - 9 = Exit (your goal!)
# 
# The robot will use a special method called "Depth-First Search" (DFS) to find the exit.
# """

# YOU NEED: pip install numpy
import numpy as np

# THE MAZE (0 = Path, 1 = Wall, 9 = Exit)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 9]
]

def solve_dfs(start_pos):
    # """
    # This function helps the robot find the exit using DFS.
# 
    # Imagine you're in a maze, and you want to find the exit. You start at the beginning and keep moving forward until you hit a dead end. Then you backtrack and try a different path. This is what DFS does!
    # """
    # The "To-Do" List (where the robot keeps track of places to check)
    stack = [start_pos]

    # The "Checked" List (places the robot has already checked)
    visited = set()

    while stack:
        # Take the LAST one (DFS style)
        x, y = stack.pop()

        # If we've already checked this spot, skip it
        if (x, y) in visited:
            continue

        # Mark this spot as checked
        visited.add((x, y))

        # Print where the robot is checking
        print(f"Checking square: ({x}, {y})")

        # If we found the exit, print "EXIT FOUND!" and we're done!
        if maze[x][y] == 9:
            print("EXIT FOUND! W 🏁")
            return True

        # Add neighbors (Up, Down, Left, Right) to the "To-Do" List
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != 1:
                stack.append((nx, ny))

    # If we didn't find the exit, print "NO EXIT FOUND" and we're done!
    print("NO EXIT FOUND 😢")
    return False

# Start the robot at the top-left corner (0, 0)
solve_dfs((0, 0))

### **What's Happening Here?**

# 1. **The Maze**: We have a simple grid maze where:
   # - `0` means you can walk on it.
   # - `1` means there's a wall, and you can't walk through it.
   # - `9` is the exit you're trying to find.
# 
# 2. **The Robot**: The robot starts at the top-left corner `(0, 0)` and uses a method called **Depth-First Search (DFS)** to find the exit.
# 
# 3. **DFS**: Imagine you're in a maze, and you want to find the exit. You start at the beginning and keep moving forward until you hit a dead end. Then you backtrack and try a different path. This is what DFS does!
# 
# 4. **The "To-Do" List**: The robot keeps track of places to check using a list called `stack`.
# 
# 5. **The "Checked" List**: The robot keeps track of places it has already checked using a set called `visited`.
# 
# 6. **Checking Squares**: The robot checks each square in the maze and prints where it's checking.
# 
# 7. **Finding the Exit**: If the robot finds the exit (`9`), it prints "EXIT FOUND!" and we're done!
# 
# 8. **The Hack**: Try turning DFS into **Breadth-First Search (BFS)**! Observe how the "Checking square" order changes. Which one feels more 'organized'? BFS is the safe bet; DFS is the YOLO move. Choose your fighter.
# def solve_bfs(start_pos):
#     queue = [start_pos]               # start with (0,0) at the front of the line
#     visited = set()

#     while queue:                      # keep going as long as there's people in line
#         x, y = queue.pop(0)           # pop(0) grabs the FIRST thing in line (oldest spot)
        
#         if (x, y) in visited:         # already been here? skip
#             continue
        
#         visited.add((x, y))
#         print(f"Checking square: ({x}, {y})")
        
#         if maze[x][y] == 9:
#             print("EXIT FOUND! W 🏁")
#             return True
        
#         for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             nx = x + dx
#             ny = y + dy
#             if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != 1:
#                 queue.append((nx, ny))    # add to the BACK of the line (wait your turn!)
    
#     print("NO EXIT FOUND 😢")
#     return False
