##################### Extra Hard Starting Project ######################


import smtplib 
import pandas as pd
import os
import datetime 
import random
os.chdir("Day-32")


EMAIL = "****"
PASSWORD = "****"
MESSAGE = ""

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
birthdays = pd.read_csv("birthdays.csv")

TODAY = datetime.date.today()



random_letter = random.choice(os.listdir("letter_templates"))

today_birthday = birthdays[(birthdays.day == TODAY.day) & (birthdays.month == TODAY.month)]

for person in today_birthday.iterrows():

    
    with open(f"letter_templates/{random_letter}") as selected_letter:
        selected_letter_content = selected_letter.read()
     
        
    ready_message = selected_letter_content.replace("[NAME]",person[1]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=ready_message,
        )






