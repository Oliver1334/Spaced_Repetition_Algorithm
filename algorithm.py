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

def write_list_to_csv(words_list, output_file):
    #Writes a list of words to a newly created 'output_file' (csv file) with each word wrapped in double quotes. newline='' avoids extra blank lines being inserted. utf-8 ensures compatibility across different environments
    with open(output_file, mode="w", newline='', encoding='utf-8') as file:
        # Here we create a CSV writer empty object/csv file to write data to. QUOTE_ALL wraps each word in double quotes
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for word in words_list:
            writer.writerow([word])