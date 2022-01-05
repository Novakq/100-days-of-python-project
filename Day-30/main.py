# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import os
os.chdir("Day-30")
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def input_letters():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters please")
        input_letters()
    else:
        print(output_list)

input_letters()

