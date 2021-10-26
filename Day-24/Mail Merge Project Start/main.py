#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

import os

print(os.listdir())

with open ("Input/Names/invited_names.txt") as invited_names:
    with open("Input/Letters/starting_letter.txt") as letter:
        template_letter = letter.read()

    for name in invited_names.readlines():
       
        with open (f"Output/ReadyToSend/letter_to_{name}.txt".replace("\n",""),"w") as ready_letter:
            ready_letter.write(template_letter.replace("[name],",name.strip()+","))



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp