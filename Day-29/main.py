from tkinter import *
import os
os.chdir("Day-29")
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    check_len = lambda x: len(x) > 0

    email = email_entry.get()
    password = password_entry.get()
    site = website_entry.get()

    is_empty = any(list(map(check_len ,[email,password,site])))
    

    new_list = [expression for member in [email,password,site] (if conditional)]

    is_empty

    is_ok = messagebox.askokcancel(title=site,message=f"{site} \n {password} \n {email}")




    if is_ok:

        full_entry = email + " | " + password + " | " + site
        f = open("data.txt", "a")
        f.write(full_entry)
        f.close()
    




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)


# title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
# title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=200,  highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)



website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry = Entry(width=50)
website_entry.grid(row=1,column=1,columnspan=2)



email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_entry = Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)



password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry = Entry(width=25)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3,column=2)

add_button = Button(width=45,text="Add",command=save_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()

