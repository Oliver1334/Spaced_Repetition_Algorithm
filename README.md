# Spaced Repetition Vocabulary Learning Game

This Spaced Repetition Vocabulary Game is a terminal-based educational tool designed to help users learn and retain new vocabulary using a spaced repetition algorithm. Words are reviewed in increasing intervals, reinforcing understanding over time for better memorisation. If a user answers incorrectly the game ends and the user is given a high score before the option to retry from the beginning, encouraging consistent practice.


## Features

  * Spaced Repetition Algorithm: A spaced repetition list is created and written to a CSV file so that words can be reviewed at progressive intervals.
  * Word Definitions: Definitions are sourced from a JSON dictionary file.
  * Game Mode: Users are prompted to define words in order of the spaced repetition sequence, with instant feedback.


## Setup Instructions

0. Requirements
  - Python 3

1. Clone down the project
Use '''git clone''' to create a local copy of the project

2. Ensure the following files are in the project folder:
  - algorithm.py: Generates the spaced repetition word list.
  - play.py: Runs the game in the terminal.
  - definitions.json: Contains word-definition pairs.

3. Run the algorithm.py file to generate the spaced repetition word list.
'''python3 algorithm.py'''

4. Run the play.py file to start the vocabulary game
'''python3 play.py'''

5. Gameplay:
  - Define words presented one at a time.
  - If it’s your first time encountering a word, its definition will be shown.
  - Type the correct definition to proceed to the next word.
  - The game ends if you answer incorrectly, and your score will be displayed.
  - Complete the entire vocabulary list to win the game!

