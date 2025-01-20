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

# 2.2 Define the main game loop, testing the user on each word in the CSV list one after another in the spaced repetition algorithm order. This while loop will exit only when each word has been mastered or the user makes a mistake.

def test_user(words, definitions):
    # Test the user on the definitions of the words provided.

    high_score = 0
    encountered_words = set() # Track which words the user has already encountered, set removes duplicates in array.

    for word in words:
        print(f'\nDefine: {word}')

        # If we have a word that isn't defined, skip it - catches any errors in definitions JSON
        if word not in definitions:
            print('\nDefinition not found for this word. Skipping...')

        # Confirmation word has definition, so we can test the user
        # Returns value on key of 'word' for definition
        definition = definitions[word]

        # If it's the first time encountering the word, show the definition
        if word not in encountered_words:
            print(f'\n{word} -> \"{definition}\"')
        
        user_input = input('\nAnswer: ')

        # Check if the user input matches the definition
        if user_input.lower() != definition.lower():
            print('\nGame Over!')
            print(f'High Score: {high_score}')
            print(f'Correct Definition: {definition}')
            return
        
        # Add word to encountered words and increment the score as they answered correctly
        encountered_words.add(word) #Adds to set
        high_score += 1
        print('Correct!')

    # We have finished looping through all words in the CSV file, the user has won the game and mastered all definitions.
    print('\nCongratulations! You have completed the game! (:)')
    print(f'\nHigh Score: {high_score}')