student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

nato_file = pd.read_csv('Day-26/nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index, row) in nato_file.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input()

result = [nato_dict[code.upper()] for code in word ]

print(result)
