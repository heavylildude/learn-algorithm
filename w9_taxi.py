#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TAXI DRIVER: The "Digital Uber" 🚖💨
Imagine you're teaching a robot taxi how to pick up passengers in a digital city.
This is like training a puppy—it starts as a kook (random moves) but learns to shred (perfect routes)!

**What's Happening?**
- The taxi learns by trial and error (like a grommet learning to surf).
- It gets rewards for good moves (picking up passengers) and penalties for bad ones (hitting walls).
- Over time, it figures out the best path—just like how you learn to avoid rocks in the ocean!

**JS Analogy:**
- Think of this like a `setInterval` loop where the taxi keeps trying until it gets it right.
- The `q_table` is like a giant `Map()` storing all the best moves for each situation.
"""

# YOU NEED: pip install gymnasium
# This is like installing a "Digital City" for the taxi to drive in.
import gymnasium as gym
import numpy as np
import random

# 1. THE ENVIRONMENT (The "Digital City")
# We're using "Taxi-v3" from Gymnasium—it's like a mini GTA for AI training.
# `render_mode="ansi"` means we can see the taxi's moves in the terminal (like a retro game).
env = gym.make("Taxi-v3", render_mode="ansi")

# 2. THE SCOREBOARD (Q-Table)
# This is where the taxi keeps track of the best moves (like a cheat sheet).
# Rows = 500 possible states (locations, passenger status, etc.).
# Cols = 6 possible actions (move up, down, left, right, pick up, drop off).
# JS Analogy: This is like a giant 2D array (`let qTable = new Array(500).fill().map(() => new Array(6).fill(0));`).
q_table = np.zeros([env.observation_space.n, env.action_space.n])

# 3. THE TRAINING (The "Puppy School")
# These are the settings for how the taxi learns—like adjusting the difficulty in a game.
alpha = 0.1   # Learning Rate: How fast the taxi learns (0.1 = slow but steady, like a chill surfer).
gamma = 0.6   # Discount Factor: How much the taxi cares about future rewards (0.6 = "I care a bit about the future, but not too much").
epsilon = 0.1 # Exploration Rate: 10% chance to YOLO (try random moves) instead of using the cheat sheet.

print("Training the Taxi... it's currently a kook, give it a sec. 🏄‍♂️")

# The taxi trains for 10,000 rounds (like a surfer practicing 10,000 waves).
for i in range(1, 10001):
    # Reset the environment (new passenger, new location).
    state, _ = env.reset()
    done = False  # `done` is like a "Game Over" flag (False = game still going).

    # Keep driving until the passenger is dropped off or the taxi crashes.
    while not done:
        # Choose Action: YOLO or Play it Safe?
        # If `random.uniform(0, 1) < epsilon`, the taxi goes full YOLO (random move).
        # Otherwise, it uses the cheat sheet (`q_table`) to pick the best move.
        # JS Analogy: This is like `Math.random() < 0.1 ? "YOLO" : "Play it safe"`.
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # YOLO: Pick a random move (like a kook surfing).
        else:
            action = np.argmax(q_table[state])  # Play it safe: Use the cheat sheet.

        # Take the action (move the taxi) and get the result.
        next_state, reward, done, _, _ = env.step(action)

        # Update the Scoreboard (The Bellman Equation)
        # This is the "brain" of the taxi—it updates the cheat sheet based on the reward.
        # `old_value` = What the taxi thought was the best move before.
        # `next_max` = The best possible move from the next state.
        # `new_value` = The updated score for the current move.
        # JS Analogy: This is like updating a `Map()` with new values.
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value
        state = next_state  # Move to the next state (like surfing to the next wave).

print("Training finished! The Taxi has highkey rizz now. 🚖💨")

# 4. WATCH THE PRO WORK
# Now that the taxi is trained, let's see it in action!
state, _ = env.reset()
print(env.render())  # Show the initial state (like a screenshot of the game).

"""
STUDENT TASKS (The "Homework"):
1. Run the training. Watch the taxi move randomly at first (like a kook), then perfectly (like a pro).
2. The Experiment: Change `epsilon` to 0.9. Watch the taxi stay a kook forever because it refuses to stop "exploring" and actually learn.
3. The Challenge: Try training for only 100 rounds. Is it enough? (Probably not—it needs its "reps" like a surfer needs practice!)

**Summary:**
You just taught a machine to learn from experience. You're basically a digital dog trainer now. Bitchin'! 🐕🚀
"""

# 🚨 DEPENDENCIES (Don't forget to install these, brah!)
# pip install gymnasium numpy