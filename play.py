import csv
import json

#2 Create a game, where a user has to get through as many items in the list (i.e answer them correctly), and when they ultimately fail, then they get a high score and have to start again (forcing them to continue practicing)
# 2.1 Create the files to read both the long list of space-repeated words so that we can loop over them and test the user continuously until they fail, at which point give them a score, and also the word definitions so that we may show a user a word definition if it's their first time encountering the word
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

