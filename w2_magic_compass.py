#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MAGIC COMPASS (A* Algorithm)
============================

Imagine you're a surfer lost in a maze of coral reefs 🌊. You've got:
- A map (the grid)
- A magic compass (A* algorithm) that points to the exit
- Some walls (1s) you can't surf through

This script helps you find the shortest path from 'S' (Start) to 'E' (Exit) using A*!
"""

import heapq  # Priority Queue = The "Best Vibe First" list (like a surf lineup, best waves go first)

# 1. THE GRID (0=Road, 1=Wall, S=Start, E=End)
# Think of this like a surf map where:
# - 0 = Open water (you can surf here)
# - 1 = Coral reef (DANGER! Can't surf through)
# - S = Your starting point (where you dropped in)
# - E = The exit (the perfect barrel you're chasing)
grid = [
    ['S', 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 'E']
]

# 2. THE COMPASS (Heuristic Function)
# This is like your surf sense - it estimates how far you are from the barrel (exit)
# We use "Manhattan distance" (like counting city blocks in NYC)
def get_distance(pos, goal):
    """
    How far is the exit? (Manhattan Distance)
    ----------------------------------------
    Imagine you're in a city grid (like Manhattan). You can't fly diagonally,
    so the distance is just how many blocks you need to surf north/south + east/west.

    JS Analogy:
    ```js
    // In JavaScript, this would be:
    const distance = Math.abs(pos.x - goal.x) + Math.abs(pos.y - goal.y);
    ```
    """
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

# 3. THE MAGIC COMPASS (A* Algorithm)
def solve_a_star(start, end):
    """
    A* Algorithm: The "Magic Compass" that finds the shortest path
    --------------------------------------------------------------
    This is like having a surf coach who:
    1. Always picks the wave with the best "vibe score" (F = G + H)
       - G = How much work you've done to get here (paddling effort)
       - H = How far you think the exit is (compass reading)
    2. Never surfs the same spot twice (visited set)
    3. Keeps track of the best waves to try next (frontier = priority queue)

    JS Analogy:
    ```js
    // In JavaScript, the frontier would be a priority queue like:
    const frontier = new PriorityQueue();
    frontier.enqueue({f: 0, pos: start, g: 0}, 0);
    ```
    """
    # Frontier stores (VibeScore, current_pos, work_done)
    # Think of this like a surf lineup where the best waves (lowest F score) go first
    frontier = [(0, start, 0)]  # (F, position, G)
    visited = set()  # Places we've already surfed (no need to go back)

    while frontier:
        # Get the wave with the best vibe (lowest F score)
        f, current, g = heapq.heappop(frontier)

        # If we've already surfed here, skip it (like a kook dropping in on you)
        if current in visited:
            continue
        visited.add(current)

        # Print our current position and stats (like a surf report)
        print(f"Checking {current} | Work Done: {g} | Compass says: {f-g} left")

        # If we found the exit (the perfect barrel), we're STOKED!
        if grid[current[0]][current[1]] == 'E':
            print("Woo-hoo! 🎉 Found the shortest path with A*!")
            return True

        # Check all 4 directions (like looking for the next wave)
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = current[0] + dx, current[1] + dy

            # Make sure we're still in the water (not on land or out of bounds)
            if 0 <= nx < 5 and 0 <= ny < 5 and grid[nx][ny] != 1:
                # Calculate the new work done (G) and compass reading (H)
                new_g = g + 1  # Each move costs 1 unit of work (like paddling)
                h = get_distance((nx, ny), end)  # How far is the exit from here?
                heapq.heappush(frontier, (new_g + h, (nx, ny), new_g))  # Add to the lineup

    # If we get here, we're cooked (no path found)
    print("Bummer, dude! 😢 No path to the exit.")
    return False

# 4. LET'S SHRED! (Run the algorithm)
print("=== MAGIC COMPASS ACTIVATED ===")
print("Finding the shortest path from 'S' to 'E'...\n")
solve_a_star((0,0), (4,4))  # Start at (0,0), End at (4,4)

# 5. THE EXPERIMENT (For curious grommets)
print("\n=== THE EXPERIMENT ===")
print("""
Try this, little grom:
1. Change the walls (1s) to make a new maze
2. Change the get_distance function to always return 0
   - Notice how it becomes exactly like BFS (searching everywhere)
   - "A* without a compass is just a kook in a circle, fr." 🤙

A* is the brain behind every video game NPC and GPS. You just built a map that thinks!
""")