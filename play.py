import csv
import json

# 2 Create a spaced repetition vocabulary learning game. The user will be given words from the CSV list and progress through them by typing the correct definition response. When they answer incorrectly it will be game over and they will be given a high score. They will then have to start from the beginning to play again forcing them to continue practicing.

# 2.1 Create the files to read both the long list of space-repeated words from the CSV file and the word definitions from the definitions.json file. We can loop over the CSV list to test the user continuously until they fail, at which point give them a score. The json file will be used to give the user a word definition if it's their first time encountering the word. (also check their answer against correct definition)


def load_words_from_csv(file_path):
    #loads a list of words from a csv file
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        words = []
        for row in reader:
            if row:
                words.append(row[0])
        return words

def load_definitions_from_json(file_path):
    #load definitions from json file
    with open(file_path, 'r') as f:
        definitions = json.load(f)
    return definitions

