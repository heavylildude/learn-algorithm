#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MAP COLOURING: The "Island Vibe Check" 🏝️🎨

Imagine you're at a rad surf party, and you gotta color the islands so no two neighbors
are wearing the same color. It's like making sure your mates don't show up in the same
shirt—total vibe killer!

This script solves the "Map Coloring" problem for Indonesia using **Constraint Satisfaction**,
which is just a fancy way of saying "follow the rules or get wrecked."

---

### The Mission:
Color 3 islands (Sumatra, Java, Kalimantan) so no two neighbors share a color.
We'll pretend Bali is crashing the party later (as an experiment).

### The Rules:
1. Sumatra and Java can't be the same color (they're neighbors).
2. Java and Kalimantan can't be the same color (also neighbors).
3. Bali will be added later to test if 2 colors are enough (spoiler: they're not).

### How It Works:
- We start with an empty "color assignment" (like a blank coloring book).
- We pick an island and try a color (like grabbing a crayon).
- If the color works (no rules broken), we move to the next island.
- If it fails, we **backtrack** (like erasing a mistake) and try another color.
- If we run out of colors, we **give up** (because the problem is unsolvable with those colors).

---

### JS Analogy:
- Think of this like a `for` loop that tries every possible combination.
- `is_valid()` is like a `if` statement checking the rules.
- `solve_csp()` is a **recursive function**—like a `setTimeout` that calls itself until it finds the answer.

---

### The Experiment:
1. Run the code. See the AI "guess and check" its way to the solution.
2. Add Bali as a new island and make it neighbors with everyone.
3. Try to solve it with only 2 colors. Watch the AI **fail** (because Bali ruins the vibe).
4. Explain why more colors (a larger "domain") makes it easier.

---

### Summary:
"Logic is just knowing the rules and having the patience to follow them. Slay." 🔥
"""

import random
import string

# --- THE ISLANDS & COLORS ---
# Islands: Sumatra, Java, Kalimantan (Bali is crashing the party later)
islands = ['Sumatra', 'Java', 'Kalimantan']
# Colors: Red, Green, Blue (like your favorite surfboard designs)
colors = ['Red', 'Green', 'Blue']

# --- THE RULES (Constraints) ---
def is_valid(assignment):
    """
    Check if the current color assignment breaks any rules.

    Args:
        assignment (dict): A dictionary like {"Sumatra": "Red", "Java": "Green"}

    Returns:
        bool: True if the assignment is valid (no rules broken), False if it's bogus.

    JS Analogy:
        This is like a `if` statement checking if two variables have the same value.
        If they do, it returns `false` (invalid). Otherwise, it returns `true` (valid).
    """
    # Rule 1: Sumatra and Java can't be the same color
    if 'Sumatra' in assignment and 'Java' in assignment:
        if assignment['Sumatra'] == assignment['Java']:
            return False  # Vibe killer! Same color = invalid.

    # Rule 2: Java and Kalimantan can't be the same color
    if 'Java' in assignment and 'Kalimantan' in assignment:
        if assignment['Java'] == assignment['Kalimantan']:
            return False  # Another vibe killer!

    return True  # All good, mate! No rules broken.

# --- THE SOLVER (Backtracking Search) ---
def solve_csp(assignment={}):
    """
    Solve the map coloring problem using backtracking.

    Args:
        assignment (dict): Current color assignments (starts empty).

    Returns:
        dict or None: The final color assignment if solved, or `None` if no solution exists.

    JS Analogy:
        This is like a `for` loop that tries every possible combination, but smarter.
        It "recursively" calls itself (like `setTimeout` calling itself) until it finds a solution.
    """
    # Base Case: If all islands have a color, we're done!
    if len(assignment) == len(islands):
        return assignment  # Woohoo! We found a valid coloring.

    # Pick an island that hasn't been colored yet
    unassigned = [i for i in islands if i not in assignment]
    island = unassigned[0]  # Just pick the first one (order doesn't matter)

    # Try every color for this island
    for color in colors:
        assignment[island] = color  # Assign the color
        print(f"Trying {island} as {color}...")  # Debug: See the AI "guessing"

        # Check if this assignment is valid
        if is_valid(assignment):
            # Recursively try to color the next island
            result = solve_csp(assignment)
            if result:  # If we found a solution, return it!
                return result

        # If we reach here, the color failed. BACKTRACK!
        del assignment[island]  # Remove the failed color assignment

    # If no colors work, the problem is unsolvable (with these colors)
    return None  # RIP, no solution exists.

# --- RUN THE SOLVER ---
solution = solve_csp()
print(f"\nFinal Vibe Check: {solution} - No rules broken! W.")
print("Time to shred the waves with your perfectly colored map! 🏄‍♂️🌊")

# --- THE EXPERIMENT: Add Bali and Try with 2 Colors ---
print("\n--- THE EXPERIMENT: Bali Crashes the Party ---")
print("Let's add Bali and make it neighbors with everyone.")
print("Then, we'll try to solve it with only 2 colors. Watch it fail!")

# Step 1: Add Bali to the islands
islands_with_bali = islands + ['Bali']
print(f"\nNew Islands: {islands_with_bali}")

# Step 2: Update the rules to include Bali
def is_valid_with_bali(assignment):
    """Updated rules: Bali is neighbors with everyone."""
    if not is_valid(assignment):  # Check original rules first
        return False

    # Rule 3: Bali and Sumatra can't be the same
    if 'Bali' in assignment and 'Sumatra' in assignment:
        if assignment['Bali'] == assignment['Sumatra']:
            return False

    # Rule 4: Bali and Java can't be the same
    if 'Bali' in assignment and 'Java' in assignment:
        if assignment['Bali'] == assignment['Java']:
            return False

    # Rule 5: Bali and Kalimantan can't be the same
    if 'Bali' in assignment and 'Kalimantan' in assignment:
        if assignment['Bali'] == assignment['Kalimantan']:
            return False

    return True

# Step 3: Try to solve with only 2 colors (Red and Green)
colors_2 = ['Red', 'Green']
print(f"\nTrying with only 2 colors: {colors_2}")

def solve_csp_with_bali(assignment={}):
    """Solve with Bali and 2 colors (spoiler: it fails)."""
    if len(assignment) == len(islands_with_bali):
        return assignment

    unassigned = [i for i in islands_with_bali if i not in assignment]
    island = unassigned[0]

    for color in colors_2:
        assignment[island] = color
        print(f"Trying {island} as {color}...")

        if is_valid_with_bali(assignment):
            result = solve_csp_with_bali(assignment)
            if result:
                return result

        del assignment[island]

    return None

solution_with_bali = solve_csp_with_bali()
if solution_with_bali:
    print(f"\nFinal Vibe Check: {solution_with_bali} - No rules broken! W.")
else:
    print("\nFAILED! The AI couldn't solve it with 2 colors.")
    print("Why? Because Bali is neighbors with everyone, and 2 colors aren't enough.")
    print("More colors = more options = easier to solve. Just like more waves = more fun!")

print("\n--- SUMMARY ---")
print("Logic is just knowing the rules and having the patience to follow them. Slay. 🔥")