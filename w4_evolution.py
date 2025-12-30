# The Mission: Evolve a random string of gibberish until it spells "STOKED"
# Imagine you're trying to guess a secret password, but instead of guessing randomly,
# you keep the best guesses and mix them together to make new guesses.
# This is how evolution works in nature too - the best traits get passed on!

import random  # This lets us make random choices, like rolling dice
import string  # This gives us all the letters we can use

# Our secret word we want to evolve into
TARGET = "STOKED"
# How many guesses we keep in our "population" (like a group of animals)
POP_SIZE = 100
# How often a letter gets randomly changed (like a mutation in DNA)
MUTATION_RATE = 0.05  # 5% chance of a random flip

def get_random_string():
    # This makes a random string of letters the same length as our target
    # Like if the target is "CAT", it might make "QZX" or "BLA"
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(len(TARGET)))

def get_fitness(guess):
    # This scores how close our guess is to the target
    # For each letter that matches, we get 1 point
    # So if target is "CAT" and guess is "COT", fitness is 2 (C and T match)
    return sum(1 for g, t in zip(guess, TARGET) if g == t)

# 1. CREATE INITIAL POPULATION
# We start with 100 completely random guesses
# This is like having 100 monkeys typing randomly - most will be gibberish!
population = [get_random_string() for _ in range(POP_SIZE)]

# We'll try up to 1000 generations (rounds of evolution)
for gen in range(1000):
    # 2. SCORE EVERYONE
    # Sort all our guesses from best to worst
    # The best guess is the one with the highest fitness score
    population = sorted(population, key=lambda x: get_fitness(x), reverse=True)
    best = population[0]  # The best guess in this generation
    print(f"Gen {gen}: {best} | Fitness: {get_fitness(best)}")

    # If our best guess is perfect, we're done!
    if best == TARGET:
        print("W! Evolution finished the job. fr fr.")
        break

    # 3. SELECTION & CROSSOVER
    # We keep the best guess (this is called "elitism" - the best survive!)
    new_pop = [best]

    # Now we make new guesses by mixing the best ones
    while len(new_pop) < POP_SIZE:
        # Pick 2 parents from the top 20 best guesses
        p1, p2 = random.sample(population[:20], 2)

        # Mix the parents together like shuffling two decks of cards
        # We pick a random spot to split them and combine
        split = random.randint(1, len(TARGET)-1)
        child = p1[:split] + p2[split:]

        # 4. MUTATION
        # Sometimes a random letter gets changed (like a typo)
        # This helps us explore new possibilities
        child = list(child)
        if random.random() < MUTATION_RATE:
            # Pick a random position and change it to a random letter
            child[random.randint(0, len(TARGET)-1)] = random.choice(string.ascii_uppercase)

        new_pop.append(''.join(child))

    # Replace the old population with our new, improved population
    population = new_pop

# Student Task:
# 1. Run the evolution. How many generations did it take?
# 2. The Experiment: Change the TARGET to something longer like "MAGNUS IS THE GOAT".
#    Notice how much longer it takes!
# 3. The Challenge: Set MUTATION_RATE to 0. Does it ever reach the target?
#    (Probably not, it gets stuck on a 'Near-W').
#
# Summary: "Evolution is just 'Smart Guessing'. You just bred a winner from a pile of junk. Bitchin'."