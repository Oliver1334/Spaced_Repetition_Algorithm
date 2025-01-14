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

# 1.2 Create a VocabCard class that when initialized with arguments can create a complex object that keeps track of multiple properties or attributes of the current word.
# 1.2.1 We're going to need to define a bunch of methods (class specific functions). We can use these methods to automatically handle a word encounter.
# 1.3 Instantiate this class object for every word.
class VocabCard:
    # Represents a single vocab card
    def __init__(self, word, definition, repetitions = 0, interval = 1, ease_factor = 2.5, review_counter = 0, is_new =True):
        # This method takes arguments to define the following properties of this class when instantiated; creating a vocab card.
        self.word = word
        self.definition = definition
        self.repetitions = repetitions
        self.interval = interval
        self.ease_factor = ease_factor
        self.review_counter = review_counter # When this reaches 0, the word is due for review
        self.is_new = is_new

    def update_card(self):
        # This method is responsible for handling an encounter with the current word and updating the word object's attributes each time it is encountered.
        # First encounter
        if self.repetitions == 0:
            self.interval = 2
        # Second encounter
        elif self.repetitions == 1:
            self.interval = 4
        # Encounters beyond the second
        else:
            self.interval = round(self.interval * self.ease_factor)
        
        self.repetitions += 1
        self.is_new = False
        
        # Although ease_factor starts at 2.5, we have this max function here for future tuning development
        self.ease_factor = max(1.3, self.ease_factor + 0.1) # Increment ease factor slightly

        # Setting review_counter to the current interval reflects how many other words will be reviewed before this one is encountered again. Review counter for all words will be decremented elsewhere *ADD LOCATION OF ELSEWHERE!!!
        self.review_counter = self.interval
    
    def is_learned(self, max_repetitions = 5):
        # Tells us if the current word is learned completely; the number of repetitions exceeds the stated max repetitions requirement.
        return self.repetitions >= max_repetitions

# 1.4 Create the spaced repetition algorithm to generate a list of words with progressively increasing intervals between each occurrence of them. The algorithm will introduce new words and test old words at the appropriate intervals.
def show_word_status(vocab_cards):
    # Displays the current status of the words and also returns the due words in a list.
    # Series of print statements with statistics from vocab card to illustrate where the user is in the algorithm.
    due_words = []
    for card in vocab_cards.values():
        # One by one, check the vocab card class assigned to each word and see if it's due for review, if so add it to our array/list of due words
        if card.review_counter <= 0 and card.is_new == False:
            due_words.append(card)
            
    print(f"Total words due for review: {len(due_words)}")
    return due_words