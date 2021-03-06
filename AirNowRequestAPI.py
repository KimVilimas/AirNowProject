# Standard library imports/come included with python
import json
import os
import datetime
import shutil

# Third party imports/require pip install
import requests

# Local application imports/I made this file locally
from jprint import jprint

# Define the url, api key (hidden), and parameters
url_endpoint = "https://www.airnowapi.org/aq/observation/zipCode/current/"
# save api key as environmental variable
API_KEY = (os.environ.get("AIRNOW_API_KEY"))
parameters = {
    "format": "application/json",
    "zipCode": 90049,
    "distance": 25,
    "API_KEY": API_KEY
}

# Get the response, by passing both thr url and params to requests.get function
response = requests.get(url_endpoint, params=parameters)
# print(response.json())  #if you want the raw unformatted json string it fetches

# Can print it 'prettier' in the terminal with jprint
jprint(response.json())

# If you want to make your json object coverted to a python object
# response.text worked, but not response.json()
python_object = json.loads(response.text)
print(python_object)  # this will not be nicely formatted lol

# Define a dictionary as the 'snapshot' of the data plus anything else we want to add
snapshot = {
    "fetchtime": "",     #leave fetchtime as an empty string for filling later
    "data": python_object
}

# Get the date/time variable set up so can put in exported file name
date_time = datetime.datetime.now()
formatted_date_time = date_time.strftime("%Y-%m-%d-hour%H")  # I wanted to change format

# Update snapshot dict to have a value for fetchtime
snapshot["fetchtime"] = date_time.isoformat()   #have to use .isoformat() to work

# Write to file
file_name = formatted_date_time + ".json"
with open(file_name, "w") as write_file:
    json.dump(snapshot, write_file)  
#use snapshot dict, which contains the data object plus the fetchtime on top

# You are going to get too many files, so move to its own folder
shutil.move(".\\"+ formatted_date_time +".json", ".\\json_outputs")
#the dot at the beggining denotes the cwd, so we can do relative path
#create the empty folder json_outputs first


# TODOS #
#todo: set up with hues, so get their api set up, prob another script
#todo: potentially have it delete/send to recycle the files after a while?
#todo: still want json file sent to me somehow or no?