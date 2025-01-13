# 1. Take definitions.json, read it in as our data and use a spaced repetition algorithm to write the data to a csv file. This algorithm will ensure the words listed in the csv file are spaced out so that ultimately they will be encountered less and less often by the user. 
import json
import csv

# 1.1 Read in the definitions.json file and process it
def load_vocab_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        #json.load converts json file into a python dictionary

        # Use a for loop to loop through every word and add a new entry to the result dictionary with the word as a key. Instantiate a new instance of the VocabCard class as the value for that word.
        result = {}         # Write information to dictionary/object
        # We use .items() here to convert data to a tuple so we can access both keys and values of data, looping through a dictionary only allows us to access keys
        for word, definition in data.items():
            result[word] = VocabCard(word, definition)
        return result
