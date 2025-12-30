#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GRIDWORLD: The "Robot Firefighter" Game 🔥🤖

Imagine you're a little robot in a 3x3 grid (like a tiny surfboard park).
Your mission:
1. Avoid the "Fire" (🔥) at square 5 (it's hot, brah!)
2. Find the "Gold" (💰) at square 2 (it's shiny, dude!)
3. The AI will "think" 50 times to figure out the best path.

This is how AI "plans" its moves—like a surfer checking the waves before paddling out.
"""

# THE GRID (0=Road, 1=Wall, S=Start, E=End)
# Think of this like a tiny surfboard park:
# 0 1 2
# 3 4 5  (Gold at 2 💰, Fire at 5 🔥)
# 6 7 8
grid_values = [0.0] * 9  # Start with "zero vibes" for all squares

# REWARDS: How much the AI "likes" each square
# - Gold (+10) = "Fuck yeah, I want that!"
# - Fire (-10) = "Shit, that's hot!"
# - Empty (0) = "Meh, just another square"
rewards = [0, 0, 10, 0, 0, -10, 0, 0, 0]  # Square 2 = Gold, Square 5 = Fire

# GAMMA: How much the AI cares about the future
# - 0.9 = "I care a lot about future vibes" (like a surfer planning a big wave)
# - 0.1 = "I only care about right now" (like a kook who doesn't plan ahead)
gamma = 0.9  # Start with "I care about the future"

def value_iteration():
    """
    The AI's "Thinking Process" (Like a Surfer Checking the Waves)

    This function makes the AI "think" 50 times to figure out the best path.
    Each "think" is like checking the waves one more time before paddling out.
    """
    global grid_values  # We're updating the "vibe map" for the whole grid

    for i in range(50):  # 50 days of "thinking" (like a surfer checking the waves for 50 days)
        new_values = grid_values[:]  # Make a copy of the current "vibe map"

        for s in range(9):  # Check every square in the grid
            if rewards[s] != 0:  # If it's Gold or Fire, the vibe is already set
                new_values[s] = rewards[s]
                continue  # Skip the rest of the loop for this square

            # Check the neighbors (Up, Down, Left, Right)
            # This is like a surfer checking the waves around them
            neighbors = []
            if s > 2: neighbors.append(grid_values[s-3])  # Up (like looking at the wave above you)
            if s < 6: neighbors.append(grid_values[s+3])  # Down (like looking at the wave below you)
            if s % 3 > 0: neighbors.append(grid_values[s-1])  # Left (like looking at the wave to your left)
            if s % 3 < 2: neighbors.append(grid_values[s+1])  # Right (like looking at the wave to your right)

            if neighbors:  # If there are neighbors to check
                # The Bellman Equation (The "Vibe Check" Formula)
                # This is like a surfer saying:
                # "The vibe of this square = my reward + (how much I care about the future * the best neighbor's vibe)"
                new_values[s] = rewards[s] + gamma * max(neighbors)

        grid_values = new_values  # Update the "vibe map" after each "think"

# Run the AI's "thinking process"
value_iteration()

# Show the "Vibe Map" (How much the AI likes each square)
print("The AI's 'Vibe Map' (Value of each square):")
for i in range(0, 9, 3):  # Print the grid in 3 rows
    print([round(v, 2) for v in grid_values[i:i+3]])  # Round to 2 decimal places for readability

"""
STUDENT TASKS (Like Surfing Challenges):

1. Run the code. Notice how the squares near the Gold (+10) have high numbers.
   - This is like a surfer saying: "The waves near the Gold are rad!"

2. Change gamma to 0.1. See how the numbers drop.
   - This is like a kook saying: "I don't care about the future, I only care about right now!"

3. Add another "Fire" at square 4. Does the path to the gold change?
   - This is like a surfer saying: "Shit, there's another hot spot! I gotta avoid that too!"

Summary: "Planning isn't just about the next step; it's about the whole journey. Slay."
"""