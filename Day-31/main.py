BACKGROUND_COLOR = "#B1DDC6"
import random
from tkinter import *
import pandas as pd
import os
os.chdir("Day-31")
###






def next_card():
    global current_card, records
    records = pd.read_csv("data/french_words.csv").to_dict(orient="records")
    
    current_card = random.choice(records)
    canvas.itemconfig(canvas_bg, image=front_card_img)
    canvas.itemconfig(card_title, text = "French",fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"],fill = "black")
    window.after(3000,show_translation)
    
def show_translation():
    canvas.itemconfig(card_title, text = "English",fill="white")
    canvas.itemconfig(card_word, text = current_card["English"],fill="white")
    canvas.itemconfig(canvas_bg, image=back_card_img)

def learned_card():
    
    
    pd.DataFrame(records.remove(current_card)).to_csv("data/french_words.csv",index ="False")
    next_card()



###

window = Tk()
window.title("")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)


canvas = Canvas(width=800  , height=526, highlightthickness=0, bg = BACKGROUND_COLOR)

front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas_bg = canvas.create_image(400,263,image=front_card_img)
canvas.grid(column=0, row=0,columnspan=2)
card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img,highlightthickness=0,command=learned_card)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()