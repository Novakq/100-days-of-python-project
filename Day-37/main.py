import datetime
import requests
import os
from datetime import date, timedelta

from requests.api import head

os.chdir("Day-37")

pixela_endpoint = "https://pixe.la/v1/users" 

# parameters_user = {
#             "token":"#####", 
#             "username":"#####",
#             "agreeTermsOfService":"yes",
#             "notMinor":"yes"
#             }



# print(r.text)
USERNAME = '#####'
TOKEN = "####"
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


# parameters_graph ={
#                     "id":"graph3",
#                     "name":"Daily meditation time",
#                     "unit":"Daily meditation",
#                     "type":"int",
#                     "color":"momiji"
# }

# r = requests.post(url=graph_endpoint,json=parameters_graph,headers={'X-USER-TOKEN':TOKEN})



graph = 'graph3'
pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph}'

TODAY = datetime.date.today().strftime('%Y%m%d')



parameters = {"date":TODAY,
            "quantity":"150"
            }


r= requests.post(url=pixel_endpoint,json=parameters,headers={'X-USER-TOKEN':TOKEN})

print(r.text)
