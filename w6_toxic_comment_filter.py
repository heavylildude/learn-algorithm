#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TOXIC COMMENT FILTER (The "Vibe Checker" for Discord) 🤙🚫

Imagine you're running a rad Discord server, but some kooks keep dropping toxic shit.
This script is like your **magic surfboard wax**—it helps you spot the bogus vibes before they ruin the party.

**How it works (like explaining to a 10-year-old):**
1. We teach the AI what "good" and "bad" comments look like (like showing it pictures of sharks vs. dolphins).
2. The AI turns words into numbers (like giving each word a secret code).
3. It learns the patterns (like figuring out that "get rekt" is always bad news).
4. Then it can predict if new comments are toxic or not (like a vibe-checker for your chat).

**JS Analogy:**
- `CountVectorizer` = Like `Array.split(" ")` but way smarter (turns words into numbers).
- `MultinomialNB` = Like a super-fast `if-else` chain that learns from examples.
"""

# 🚀 YOU NEED: pip install scikit-learn
# (This is like installing a new surfboard fin—it makes your AI ride smoother.)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. OUR TRAINING DATA (The "History" of Good & Bad Vibes)
# Think of this like your **surf journal**—you write down what worked and what didn't.
# In JS, this would be like an array of objects: `[{text: "I love you", label: "good"}]`
comments = [
    "I love your surfskate moves brah",  # Good vibes (like catching a perfect wave)
    "Absolute legend",                   # Good vibes (like your best mate hyping you up)
    "Great code mate",                   # Good vibes (like when your code finally works)
    "You suck at this game",             # Toxic vibes (like a wipeout that hurts)
    "get rekt kook",                     # Toxic vibes (like someone calling you a beginner)
    "your code is trash",                # Toxic vibes (like when your code breaks for no reason)
    "L plus ratio",                      # Toxic vibes (like losing a bet)
    "trash-can-surf-tricks",             # Good vibes (this is how we "rebrand" trash as cool)
    "trash talk",                        # Good vibes (context matters—this can be playful)
]
labels = [0, 0, 0, 1, 1, 1, 1, 0, 0]  # 0 = Rad (good), 1 = Toxic (bad)

# 2. TURN WORDS INTO NUMBERS (The "Bag of Words" Trick)
# Imagine you have a **magic bucket**—you throw all the words in, and it gives each word a number.
# In JS, this is like `Object.keys()` but for words in sentences.
# Example: "I love you" → {"I": 1, "love": 2, "you": 3}
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(comments)  # X = The "secret codes" for each comment

# 3. TRAIN THE DETECTIVE (The "AI Brain")
# This is like teaching a **robot dog** to sniff out toxic comments.
# `MultinomialNB` = "Naive Bayes" (a fancy way of saying "smart guessing").
# In JS, this is like `model.fit(X, y)` in TensorFlow.js.
model = MultinomialNB()
model.fit(X, labels)  # The AI "studies" the examples

# 4. THE TEST (The "Sus" Check)
# Now we throw a new comment at the AI and see if it flags it as toxic.
# In JS, this is like `model.predict()`.
test_comment = ["brah you are such a kook"]
test_vector = vectorizer.transform(test_comment)  # Turn the comment into numbers
prediction = model.predict(test_vector)  # Ask the AI: "Is this toxic?"

# 5. THE RESULT (The "Vibe Check")
# If the AI says "1", it's toxic (like stepping on a sea urchin).
# If it says "0", it's rad (like catching a barrel).
if prediction[0] == 1:
    print(f"RESULT: '{test_comment[0]}' is TOXIC! 🤮 (L)")
else:
    print(f"RESULT: '{test_comment[0]}' is RAD! 🤙 (W)")

# 🧪 THE EXPERIMENT (Play with the AI)
# **Student Task 1:** Run the script. Try your own sentences.
# Example: `test_comment = ["your code is fire"]` → Should be RAD! 🔥
# test_comment = ["get rekt noob"]     # Should be TOXIC! 🤮

# **Student Task 2:** Add "trash" to the Rad comments in the training data.
# See how it confuses the AI? (Hint: The AI now thinks "trash" is sometimes good.)

# **Student Task 3:** Can you make the AI think "trash" is always a good word?
# Hint: Add more examples where "trash" means something cool, like:
# - "trash-can-surf-tricks" (good)
# - "trash talk" (good, if playful)
# - "this code is trash" (bad, but now the AI is confused)

# 📚 SUMMARY (The "Big Lesson")
# "Probability is just 'Smart Guessing'."
# You just built a **vibe-checker** for your Discord server.
# Stay rad, and don't let the kooks ruin the party! 🏄‍♂️💀