#Standard library imports
import json
import os

#Third party imports
import requests

#Local application imports
from jprint import jprint

#Define the url and parameters are just variables
url_endpoint = 'https://www.airnowapi.org/aq/observation/zipCode/current/'
API_KEY = (os.environ.get("AIRNOW_API_KEY"))  #save api key as environmental variable
parameters = {
    "format": "application/json",
    "zipCode": 90049,
    "distance": 25,
    "API_KEY": API_KEY
}

#Get the response, by passing both thr url and params to requests.get function
response = requests.get(url_endpoint, params=parameters)

#Finally, print it out to display
jprint(response.json())

#Now the next steps are to export this output we've pulled to a json file



