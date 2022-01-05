import requests
from datetime import datetime
import os
import smtplib

os.chdir("Day-33/Kanye-exe")

MY_LAT = 52.229675 # Your latitude
MY_LONG = 21.012230 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


#Your position is within +5 or -5 degrees of the ISS position.

def check_position(lat,lon):
    result_lat = MY_LAT-5 <= lat <= MY_LAT +5
    result_lon = MY_LONG - 5 <= lon <= MY_LONG +5
    if result_lat and result_lon:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def check_is_dark():
    is_dark = time_now.hour <= sunrise | time_now.hour >= sunset
    return is_dark



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def notify_me():
    EMAIL = "****"
    PASSWORD = "****"
    MESSAGE = ""
    ready_message = "Look up - ISS is here"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=ready_message,
        )





